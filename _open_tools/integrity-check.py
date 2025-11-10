#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Minimal integrity stub confirming open-core separation."""

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    private_markers = [
        root / "govspine",
        root / "ops",
        root / "analytics",
        root / "backend",
    ]
    missing = [str(path) for path in private_markers if path.exists()]
    if missing:
        print("⚠️  Unexpected private directories present:")
        for path in missing:
            print(f" - {path}")
    else:
        print("✓ Integrity check: no private runtime directories detected.")


if __name__ == "__main__":
    main()
