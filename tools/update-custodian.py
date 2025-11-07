#!/usr/bin/env python3
"""Rotate custodian keys and update the governance registry."""

import argparse
import datetime as dt
import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "governance" / "custodian_registry.yaml"
ROSTER_PATH = REPO_ROOT / "docs" / "custodian-roster.md"


def parse_registry() -> List[Dict[str, Any]]:
    if not REGISTRY_PATH.exists():
        return []
    entries: List[Dict[str, Any]] = []
    current: Dict[str, Any] | None = None
    for line in REGISTRY_PATH.read_text(encoding="utf-8").splitlines():
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


def dump_registry(entries: List[Dict[str, Any]]) -> None:
    lines: List[str] = []
    for entry in entries:
        lines.append("- layer: " + entry["layer"])
        lines.append(f"  role: {entry['role']}")
        lines.append(f"  holder: {entry['holder']}")
        lines.append(f"  key_id: {entry['key_id']}")
        lines.append(f"  last_rotation: {entry['last_rotation']}")
    REGISTRY_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def render_roster(entries: List[Dict[str, Any]]) -> None:
    ROSTER_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Custodian Roster",
        "",
        "| Layer | Role | Holder | Key ID | Last Rotation |",
        "| --- | --- | --- | --- | --- |",
    ]
    for entry in entries:
        lines.append(
            f"| {entry['layer']} | {entry['role']} | {entry['holder']} | {entry['key_id']} | {entry['last_rotation']} |"
        )
    ROSTER_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def rotate_entry(
    entries: List[Dict[str, Any]], layer: str, role: str, holder: str, key_id: str
) -> None:
    now = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    for entry in entries:
        if (
            entry["layer"].lower() == layer.lower()
            and entry["role"].lower() == role.lower()
        ):
            entry["holder"] = holder
            entry["key_id"] = key_id
            entry["last_rotation"] = now
            return
    entries.append(
        {
            "layer": layer,
            "role": role,
            "holder": holder,
            "key_id": key_id,
            "last_rotation": now,
        }
    )


def commit_changes(message: str, sign: bool) -> None:
    cmd = ["git", "commit", "-am", message]
    if sign:
        cmd.insert(2, "-S")
    subprocess.check_call(cmd, cwd=REPO_ROOT)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("layer", help="Layer identifier, e.g., L1")
    parser.add_argument("role", help="Custodian role")
    parser.add_argument("holder", help="New holder name")
    parser.add_argument("key_id", help="New signing key fingerprint")
    parser.add_argument(
        "--sign", action="store_true", help="Sign the git commit with -S"
    )
    parser.add_argument(
        "--commit", action="store_true", help="Create git commit for the rotation"
    )
    args = parser.parse_args()

    entries = parse_registry()
    rotate_entry(entries, args.layer, args.role, args.holder, args.key_id)
    dump_registry(entries)
    render_roster(entries)

    payload = {
        "layer": args.layer,
        "role": args.role,
        "holder": args.holder,
        "key_id": args.key_id,
        "rotated_at": dt.datetime.utcnow().isoformat() + "Z",
    }
    print(json.dumps(payload, indent=2))

    if args.commit:
        try:
            commit_changes(
                f"chore: rotate custodian {args.layer} {args.role}", args.sign
            )
        except subprocess.CalledProcessError as exc:
            raise SystemExit(f"git commit failed: {exc}")


if __name__ == "__main__":
    main()
