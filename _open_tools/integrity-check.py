#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Minimal integrity stub confirming open-core separation."""

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    private_markers = [
        root / "analytics",
        root / "backend",
        root / "briefing",
        root / "commercial",
        root / "govspine",
        root / "ml",
        root / "ops",
        root / "protocol",
        root / "tests",
        root / "tools",
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
