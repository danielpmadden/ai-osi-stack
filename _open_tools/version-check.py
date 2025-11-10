#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Report the canonical open-core version recorded in provenance metadata."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def extract(field: str, text: str) -> str | None:
    pattern = rf"^{field}:[\t ]*\"?(?P<value>[^\"\n]+)\"?$"
    match = re.search(pattern, text, re.MULTILINE)
    if match:
        return match.group("value").strip()
    return None


def main() -> None:
    provenance_path = Path(__file__).resolve().parents[1] / "CANONICAL_PROVENANCE.yaml"
    if not provenance_path.exists():
        print("⚠️  CANONICAL_PROVENANCE.yaml not found.", file=sys.stderr)
        raise SystemExit(1)
    contents = provenance_path.read_text(encoding="utf-8")
    version = extract("canonical_version", contents) or "unknown"
    date = extract("canonical_date", contents) or "unknown date"
    print(f"✓ Canonical open-core version: {version} (dated {date})")


if __name__ == "__main__":
    main()
