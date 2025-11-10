#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Validate JSON and JSON-LD files for syntax compliance."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable


def iter_json_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".json", ".jsonld"}:
            yield path


def main() -> None:
    errors: list[str] = []
    root = Path(__file__).resolve().parents[1]
    for file_path in sorted(iter_json_files(root)):
        try:
            with file_path.open(encoding="utf-8") as handle:
                json.load(handle)
        except Exception as exc:  # pragma: no cover - defensive path
            errors.append(f"{file_path}: {exc}")
    if errors:
        print("⚠️  JSON syntax issues detected:")
        for message in errors:
            print(f" - {message}")
    else:
        print("✓ All JSON and JSON-LD files parsed without syntax errors.")


if __name__ == "__main__":
    main()
