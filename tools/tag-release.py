#!/usr/bin/env python3
"""Create semantic GDS tags for the current quarter."""

import argparse
import datetime as dt
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
GDS_DIR = REPO_ROOT / "governance" / "deployment"


def determine_quarter(date: dt.date) -> str:
    quarter = (date.month - 1) // 3 + 1
    return f"{date.year}Q{quarter}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", help="ISO date for tagging (defaults to today)")
    parser.add_argument(
        "--dry-run", action="store_true", help="Print tag without creating it"
    )
    args = parser.parse_args()

    today = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    quarter = determine_quarter(today)
    tag_name = f"GDS_{quarter}"
    target_file = GDS_DIR / f"gds_{quarter}.md"

    if not target_file.exists():
        raise SystemExit(f"expected {target_file} to exist before tagging")

    if args.dry_run:
        print(tag_name)
        return

    try:
        subprocess.check_call(["git", "tag", tag_name])
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"failed to create tag: {exc}")

    print(f"Created tag {tag_name}")


if __name__ == "__main__":
    main()
