"""Build the static governance dashboard from manifest files."""
from __future__ import annotations

import argparse
import json
import pathlib
import textwrap

import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from collections import defaultdict
from datetime import datetime
from typing import Any, Dict, Iterable

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    yaml = None

from tools.governance.schema_utils import SchemaRegistry, ValidationError, validate_manifest

SCHEMA_DIR = pathlib.Path("schemas/aeip")
GOVERNANCE_ROOT = pathlib.Path("governance")
OUTPUT_PATH = pathlib.Path("docs/governance-dashboard/index.md")


def iter_manifest_paths(root: pathlib.Path) -> Iterable[pathlib.Path]:
    yield from root.rglob("*.json")
    if yaml is not None:
        for path in root.rglob("*.yaml"):
            yield path
        for path in root.rglob("*.yml"):
            yield path


def load_manifest(path: pathlib.Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        if path.suffix == ".json" or yaml is None:
            return json.load(handle)
        return yaml.safe_load(handle)


def render_section(manifests: Iterable[Dict[str, Any]]) -> str:
    lines = []
    for manifest in manifests:
        payload_uri = manifest.get("payload_uri", "(no payload)")
        timestamp = manifest.get("timestamp", "unknown")
        title = manifest.get("artifact_type", manifest.get("uuid"))
        lines.append(f"### {title}")
        lines.append("")
        lines.append(f"- UUID: `{manifest['uuid']}`")
        lines.append(f"- Timestamp: `{timestamp}`")
        lines.append(f"- Custodian: `{manifest.get('custodian', 'n/a')}`")
        lines.append(f"- Payload: `{payload_uri}`")
        tags = ", ".join(manifest.get("tags", [])) or "(none)"
        lines.append(f"- Tags: {tags}")
        lines.append(f"- Evidence Hash: `{manifest.get('evidence_hash', 'n/a')}`")
        lines.append("")
    if not lines:
        lines.append("No manifests recorded for this layer yet.")
        lines.append("")
    return "\n".join(lines)


def build_dashboard(output: pathlib.Path) -> None:
    registry = SchemaRegistry(SCHEMA_DIR)
    manifests_by_layer: Dict[str, list[Dict[str, Any]]] = defaultdict(list)

    for manifest_path in iter_manifest_paths(GOVERNANCE_ROOT):
        manifest = load_manifest(manifest_path)
        try:
            validate_manifest(manifest, registry)
        except ValidationError as exc:  # pragma: no cover - surfaced in CLI use
            raise RuntimeError(f"Validation failed for {manifest_path}: {exc}") from exc
        manifests_by_layer[manifest["layer"]].append(manifest)

    header = textwrap.dedent(
        """
        # Governance Evidence Dashboard

        _Last updated: {timestamp}_

        This file is generated. Run `python docs/governance-dashboard/build_dashboard.py`
        to refresh the contents after new manifests are produced.

        ## Usage

        - `python docs/governance-dashboard/build_dashboard.py` regenerates this page.
        - `python docs/governance-dashboard/search.py --tag model` queries manifests.
        - All manifests must conform to the schemas stored in `schemas/aeip`.
        """
    ).format(timestamp=datetime.utcnow().isoformat(timespec="seconds") + "Z")

    sections = []
    for layer in sorted(manifests_by_layer):
        sections.append(f"## Layer {layer}")
        sections.append("")
        sections.append(
            render_section(
                sorted(manifests_by_layer[layer], key=lambda m: m.get("timestamp", ""), reverse=True)
            )
        )
        sections.append("")

    content = header + "\n\n" + "\n".join(sections)
    output.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rebuild the governance dashboard")
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        default=OUTPUT_PATH,
        help="Path to the markdown file to write",
    )
    args = parser.parse_args()
    build_dashboard(args.output)
