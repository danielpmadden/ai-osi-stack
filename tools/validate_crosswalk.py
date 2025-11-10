#!/usr/bin/env python3
"""Validate that crosswalk mappings reference existing Version 5 files."""
from __future__ import annotations

import argparse
from pathlib import Path

LICENSE_NOTICE = """Creative Commons Attribution–NonCommercial–NoDerivatives 4.0 International"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate v4→v5 crosswalk file references")
    parser.add_argument(
        "root",
        nargs="?",
        default=Path(__file__).resolve().parents[1],
        type=Path,
        help="Repository root containing the reference directory.",
    )
    return parser.parse_args()


def validate_crosswalk(root: Path) -> int:
    crosswalk_path = root / "reference" / "crosswalk_v4_v5.md"
    if not crosswalk_path.exists():
        print(f"error: crosswalk file not found at {crosswalk_path}")
        return 1

    missing = []
    for line in crosswalk_path.read_text().splitlines():
        if not (line.startswith("| V4-") or line.startswith("| V4-App")):
            continue
        parts = [segment.strip() for segment in line.split("|")]
        if len(parts) < 5:
            print(f"warning: skipping malformed row: {line}")
            continue
        mapped = parts[3]
        candidate = (root / mapped).resolve()
        if not candidate.exists():
            missing.append(mapped)

    if missing:
        print("Missing mapped files:")
        for item in missing:
            print(f" - {item}")
        return 2

    print("All crosswalk mappings resolve to existing files.")
    print(f"License notice: {LICENSE_NOTICE}")
    return 0


def main() -> None:
    args = parse_args()
    exit_code = validate_crosswalk(args.root)
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
