#!/usr/bin/env python3
"""Validate AEIP artifacts contain signature metadata."""

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
AEIP_FILES = list(REPO_ROOT.glob("governance/**/*_AEIP.yaml"))


def main() -> int:
    missing = []
    for path in AEIP_FILES:
        content = path.read_text(encoding="utf-8")
        if "hash:" not in content or "signed_at:" not in content:
            missing.append(str(path))
    if missing:
        print("Missing signatures for:")
        for item in missing:
            print(f" - {item}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
