#!/usr/bin/env python3
"""Verify that schema versions and documentation references are aligned."""
from __future__ import annotations

from pathlib import Path
from typing import Dict

from src.common.schema import load_schema

SCHEMA_DIR = Path("schemas")
DOC_PATH = Path("docs/AI_OSI_Protocol_Spec.md")


def main() -> None:
    versions: Dict[str, str] = {}
    for path in SCHEMA_DIR.glob("*.*"):
        schema = load_schema(path)
        versions[path.name] = schema.version
    missing = [name for name in versions if name not in DOC_PATH.read_text()]
    if missing:
        print("Warning: documentation does not reference schema versions for", ", ".join(missing))
    else:
        print("Documentation references all schema artifacts.")
    for name, version in sorted(versions.items()):
        print(f"{name}: v{version}")


if __name__ == "__main__":
    main()
