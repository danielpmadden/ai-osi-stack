#!/usr/bin/env python3
"""Validate an artifact against the AI OSI schemas."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict

from src.common.artifacts import Artifact
from src.common.schema import load_schema

SCHEMA_FILES = {
    "ITP": "schemas/itp_schema.json",
    "DRR": "schemas/drr_schema.yaml",
    "GDS": "schemas/gds_schema.json",
    "OAM": "schemas/oam_schema.yaml",
    "ILE": "schemas/ile_schema.json",
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact_file", type=Path)
    parser.add_argument("artifact_type", choices=SCHEMA_FILES.keys())
    args = parser.parse_args()

    if args.artifact_file.suffix in {".yaml", ".yml"}:
        try:
            import yaml  # type: ignore

            data = yaml.safe_load(args.artifact_file.read_text())
        except Exception:
            from src.common.schema import _simple_yaml_load  # type: ignore

            data = _simple_yaml_load(args.artifact_file.read_text())
    else:
        data: Dict[str, object] = json.loads(args.artifact_file.read_text())
    schema = load_schema(SCHEMA_FILES[args.artifact_type])
    artifact = Artifact(schema=schema, payload=data)  # type: ignore[arg-type]
    artifact.validate()
    if not artifact.verify_signature():
        print("Warning: artifact is unsigned; signature validation skipped")
    print(f"{args.artifact_file} conforms to {schema.name} v{schema.version}")


if __name__ == "__main__":
    main()
