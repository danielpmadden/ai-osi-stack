# SPDX-License-Identifier: Apache-2.0

"""Build AEIP frame manifests by aggregating existing governance artifacts."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
from typing import Any, Dict, Iterable, List

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    yaml = None

if __package__ in (None, ""):
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from tools.governance import manifest_builder
    from tools.governance.schema_utils import (
        SchemaRegistry,
        ValidationError,
        validate_manifest,
    )
else:  # pragma: no cover - executed when run as module
    from . import manifest_builder
    from .schema_utils import SchemaRegistry, ValidationError, validate_manifest

SCHEMA_DIR = pathlib.Path("schemas/aeip")
DEFAULT_FRAME_VERSION = "2025.1"


def load_manifest(path: pathlib.Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        if path.suffix == ".json" or yaml is None:
            return json.load(handle)
        return yaml.safe_load(handle)


def discover_manifests(paths: Iterable[str]) -> List[pathlib.Path]:
    expanded: List[pathlib.Path] = []
    for entry in paths:
        path = pathlib.Path(entry)
        if path.is_dir():
            expanded.extend(sorted(path.rglob("*.json")))
            if yaml is not None:
                expanded.extend(sorted(path.rglob("*.yaml")))
                expanded.extend(sorted(path.rglob("*.yml")))
        else:
            expanded.append(path)
    return expanded


def build_frame_payload(manifest_paths: Iterable[pathlib.Path]) -> Dict[str, Any]:
    artifacts: List[Dict[str, Any]] = []
    for path in manifest_paths:
        manifest = load_manifest(path)
        artifacts.append(
            {
                "artifact_type": manifest.get("artifact_type", "unknown"),
                "uuid": manifest.get("uuid", ""),
                "schema_ref": manifest.get("schema_ref", ""),
                "layer": manifest.get("layer", ""),
            }
        )
    return {"artifacts": artifacts}


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build an AEIP frame manifest")
    parser.add_argument(
        "--manifests", nargs="+", help="Manifest files or directories to include"
    )
    parser.add_argument(
        "--layer", default="L6", help="Governance layer to assign to the frame"
    )
    parser.add_argument("--custodian", required=True, help="Frame custodian")
    parser.add_argument(
        "--context-uri", required=True, help="Reference to the repository or system"
    )
    parser.add_argument(
        "--payload", required=True, help="Path to write the aggregated payload JSON"
    )
    parser.add_argument("--payload-uri", help="External URI for the payload")
    parser.add_argument(
        "--output", required=True, help="Path to write the AEIP frame manifest"
    )
    parser.add_argument("--tags", nargs="*", help="Tags to apply to the frame manifest")
    parser.add_argument("--schema-version", help="Schema version override")
    parser.add_argument(
        "--frame-version", default=DEFAULT_FRAME_VERSION, help="Frame release version"
    )
    parser.add_argument("--signature", help="Signature override")
    parser.add_argument("--signature-file", help="Read signature from file")
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> None:
    args = parse_args(argv or sys.argv[1:])
    manifest_paths = discover_manifests(args.manifests)
    payload_data = build_frame_payload(manifest_paths)
    payload_path = pathlib.Path(args.payload)
    payload_path.parent.mkdir(parents=True, exist_ok=True)
    payload_path.write_text(json.dumps(payload_data, indent=2), encoding="utf-8")

    manifest_args = argparse.Namespace(
        artifact_type="aeip-frame",
        layer=args.layer,
        custodian=args.custodian,
        context_uri=args.context_uri,
        payload=str(payload_path),
        payload_uri=args.payload_uri,
        schema_ref="aeip_frame.schema.json",
        schema_version=args.schema_version,
        tags=args.tags,
        signature=args.signature,
        signature_file=args.signature_file,
        extra_path=None,
        extra_json=json.dumps(
            {
                "artifacts": payload_data["artifacts"],
                "frame_version": args.frame_version,
            }
        ),
        output=args.output,
    )

    manifest = manifest_builder.build_manifest(manifest_args)
    registry = SchemaRegistry(SCHEMA_DIR)
    try:
        validate_manifest(manifest, registry)
    except ValidationError as exc:  # pragma: no cover - CLI surface
        raise SystemExit(f"AEIP frame validation failed: {exc}") from exc
    manifest_builder.write_manifest(manifest, pathlib.Path(args.output))
    print(f"Wrote AEIP frame manifest to {args.output}")


if __name__ == "__main__":
    main()
