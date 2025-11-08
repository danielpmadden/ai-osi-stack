# SPDX-License-Identifier: Apache-2.0

#!/usr/bin/env python3
"""Generate standards crosswalk tables from schema metadata."""

import collections
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = REPO_ROOT / "schemas"
OUTPUT_DIR = REPO_ROOT / "docs" / "crosswalks"

TARGET_ORDER = ["GDPR", "NIST AI RMF", "ISO 27001", "EU AI Act"]


def parse_external_refs(path: Path) -> List[Dict[str, str]]:
    refs: List[Dict[str, str]] = []
    current: Dict[str, str] | None = None
    capture = False
    base_indent = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if raw_line.strip().startswith("external_refs:"):
            capture = True
            continue
        if not capture:
            continue
        if raw_line.strip() == "":
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        if base_indent is None and raw_line.lstrip().startswith("-"):
            base_indent = indent
        if indent < (base_indent or 0):
            break
        line = raw_line.strip()
        if line.startswith("-"):
            if current:
                refs.append(current)
            current = {}
            line = line[1:].strip()
            if ":" in line:
                key, value = [part.strip() for part in line.split(":", 1)]
                current[key] = value
        else:
            if ":" in line and current is not None:
                key, value = [part.strip() for part in line.split(":", 1)]
                current[key] = value
    if current:
        refs.append(current)
    return [ref for ref in refs if ref.get("framework")]


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    mapping: Dict[str, List[Dict[str, str]]] = collections.defaultdict(list)

    for path in SCHEMA_DIR.glob("*.template.yaml"):
        refs = parse_external_refs(path)
        for ref in refs:
            framework = ref.get("framework")
            mapping[framework].append(
                {
                    "framework": framework,
                    "artifact": path.stem.split(".")[0].upper(),
                    "control": ref.get("control", ""),
                    "notes": ref.get("notes", ""),
                }
            )

    lines = ["# Standards Crosswalk", ""]
    lines.append("| External Standard | AI OSI Artifact | Notes |")
    lines.append("| --- | --- | --- |")

    for framework in TARGET_ORDER:
        entries = mapping.get(framework, [])
        if not entries:
            lines.append(f"| {framework} | _No mapping detected_ | |")
            continue
        for entry in entries:
            notes = entry["control"] or entry["notes"]
            lines.append(f"| {framework} | {entry['artifact']} | {notes} |")

    (OUTPUT_DIR / "framework-crosswalk.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
