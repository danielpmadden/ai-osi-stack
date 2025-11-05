#!/usr/bin/env python3
"""Append recent postmortem findings into the next Governance Deployment Summary."""

import argparse
import datetime as dt
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).resolve().parents[1]
POSTMORTEM_DIR = REPO_ROOT / "governance" / "postmortems"
GDS_DIR = REPO_ROOT / "governance" / "deployment"


def list_postmortems() -> List[Path]:
    return sorted(POSTMORTEM_DIR.glob("incident_*.md"))


def extract_lessons(path: Path) -> List[str]:
    lessons: List[str] = []
    capture = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip().lower().startswith("## lessons learned"):
            capture = True
            continue
        if capture and line.startswith("## "):
            break
        if capture and line.strip().startswith("- "):
            lessons.append(line.strip()[2:])
    return lessons


def determine_quarter(date: dt.date) -> str:
    return f"{date.year}Q{(date.month - 1) // 3 + 1}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", help="ISO date for determining target quarter", default=dt.date.today().isoformat())
    args = parser.parse_args()

    quarter = determine_quarter(dt.date.fromisoformat(args.date))
    gds_path = GDS_DIR / f"gds_{quarter}.md"
    if not gds_path.exists():
        raise SystemExit(f"GDS file {gds_path} does not exist")

    lessons = []
    for path in list_postmortems():
        lessons.extend(extract_lessons(path))

    if not lessons:
        print("No lessons to append")
        return

    content = gds_path.read_text(encoding="utf-8")
    if "## Incident Lessons" not in content:
        content += "\n\n## Incident Lessons\n"
    content_lines = content.splitlines()

    insertion_index = next((i for i, line in enumerate(content_lines) if line.strip() == "## Incident Lessons"), None)
    if insertion_index is None:
        content_lines.extend(["## Incident Lessons", "- " + lessons[0]])
        for item in lessons[1:]:
            content_lines.append(f"- {item}")
    else:
        insertion_index += 1
        while insertion_index < len(content_lines) and content_lines[insertion_index].startswith("-"):
            insertion_index += 1
        for item in lessons:
            if f"- {item}" not in content_lines:
                content_lines.insert(insertion_index, f"- {item}")
                insertion_index += 1

    gds_path.write_text("\n".join(content_lines), encoding="utf-8")
    print(f"Appended {len(lessons)} lessons to {gds_path}")


if __name__ == "__main__":
    main()
