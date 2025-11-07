#!/usr/bin/env python3
"""Verify custodian registry freshness and vacancy constraints."""

import datetime as dt
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY = REPO_ROOT / "governance" / "custodian_registry.yaml"
MAX_AGE_DAYS = 90


def parse_registry():
    entries = []
    current = None
    for line in REGISTRY.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- ") and ":" in stripped:
            if current:
                entries.append(current)
            current = {}
            key, value = [part.strip() for part in stripped[2:].split(":", 1)]
            current[key] = value
        elif ":" in line and current is not None:
            key, value = [part.strip() for part in line.split(":", 1)]
            current[key] = value
    if current:
        entries.append(current)
    return entries


def main() -> int:
    if not REGISTRY.exists():
        print("custodian registry missing", file=sys.stderr)
        return 1
    entries = parse_registry()
    if not entries:
        print("custodian registry empty", file=sys.stderr)
        return 1
    now = dt.datetime.now(dt.timezone.utc)
    for entry in entries:
        if entry.get("holder", "").strip().lower() == "vacant":
            print(f"{entry['layer']} {entry['role']} is vacant", file=sys.stderr)
            return 1
        raw = entry.get("last_rotation")
        try:
            ts = dt.datetime.fromisoformat(raw.replace("Z", "+00:00")).astimezone(
                dt.timezone.utc
            )
        except Exception:
            print(
                f"invalid timestamp for {entry['layer']} {entry['role']}",
                file=sys.stderr,
            )
            return 1
        age = (now - ts).days
        if age > MAX_AGE_DAYS:
            print(
                f"registry entry {entry['layer']} {entry['role']} is {age} days old (> {MAX_AGE_DAYS})",
                file=sys.stderr,
            )
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
