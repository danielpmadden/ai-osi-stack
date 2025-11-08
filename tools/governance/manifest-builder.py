# SPDX-License-Identifier: Apache-2.0

"""Generate Governance Spine manifests and update registry files."""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import uuid
from datetime import datetime, timezone
from typing import Any, Dict

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    yaml = None


if __package__ in (None, ""):
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from tools.governance.schema_utils import (
        SchemaRegistry,
        ValidationError,
        validate_manifest,
    )
else:
    from .schema_utils import SchemaRegistry, ValidationError, validate_manifest

SCHEMA_DIR = pathlib.Path("schemas/aeip")
DEFAULT_SCHEMA_VERSION = "1.0.0"


def load_extra(extra_path: str | None, extra_json: str | None) -> Dict[str, Any]:
    if extra_path:
        path = pathlib.Path(extra_path)
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    if extra_json:
        return json.loads(extra_json)
    return {}


def resolve_signature(args: argparse.Namespace) -> str:
    if args.signature:
        return args.signature
    if args.signature_file:
        return pathlib.Path(args.signature_file).read_text(encoding="utf-8").strip()
    return os.environ.get("GOVERNANCE_SIGNATURE", "UNSIGNED")


def ensure_output_dir(path: pathlib.Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def write_manifest(manifest: Dict[str, Any], output_path: pathlib.Path) -> None:
    ensure_output_dir(output_path)
    if output_path.suffix == ".json" or yaml is None:
        output_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    else:
        with output_path.open("w", encoding="utf-8") as handle:
            yaml.safe_dump(manifest, handle, sort_keys=False)


def build_manifest(args: argparse.Namespace) -> Dict[str, Any]:
    payload_path = pathlib.Path(args.payload)
    manifest: Dict[str, Any] = {
        "uuid": str(uuid.uuid4()),
        "layer": args.layer,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "custodian": args.custodian,
        "context_uri": args.context_uri,
        "evidence_hash": "ADVISORY-CHECKSUM-RECORD-LOCALLY",
        "signature": resolve_signature(args),
        "tags": args.tags or [],
        "artifact_type": args.artifact_type,
        "schema_version": args.schema_version or DEFAULT_SCHEMA_VERSION,
        "payload_uri": args.payload_uri or str(payload_path),
        "schema_ref": args.schema_ref,
    }
    manifest.update(load_extra(args.extra_path, args.extra_json))
    return manifest


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate governance manifests")
    parser.add_argument(
        "--artifact-type", required=True, help="Artifact type identifier"
    )
    parser.add_argument("--layer", required=True, help="Governance layer (e.g., L0)")
    parser.add_argument("--custodian", required=True, help="Manifest custodian")
    parser.add_argument(
        "--context-uri", required=True, help="Link to the relevant system or repo"
    )
    parser.add_argument("--payload", required=True, help="Path to the evidence payload")
    parser.add_argument("--payload-uri", help="External URI for the payload")
    parser.add_argument(
        "--schema-ref", required=True, help="Schema filename under schemas/aeip/"
    )
    parser.add_argument("--schema-version", help="Schema version string")
    parser.add_argument("--tags", nargs="*", help="Tags to include in the manifest")
    parser.add_argument("--signature", help="Explicit signature value")
    parser.add_argument("--signature-file", help="Read signature from file")
    parser.add_argument(
        "--extra-path", help="JSON file containing extra fields to merge"
    )
    parser.add_argument("--extra-json", help="JSON string of extra fields")
    parser.add_argument(
        "--output", required=True, help="Output manifest path (.json or .yaml)"
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv or sys.argv[1:])
    manifest = build_manifest(args)
    registry = SchemaRegistry(SCHEMA_DIR)
    try:
        validate_manifest(manifest, registry)
    except ValidationError as exc:  # pragma: no cover - CLI surface
        raise SystemExit(f"Manifest validation failed: {exc}") from exc
    output_path = pathlib.Path(args.output)
    write_manifest(manifest, output_path)
    print(f"Wrote manifest to {output_path}")


if __name__ == "__main__":
    main()
