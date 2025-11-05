#!/usr/bin/env python3
"""Synthesize CRO dashboard from metrics and registries."""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
METRICS_FILE = REPO_ROOT / "governance" / "metrics" / "metrics.json"
REGISTRY_FILE = REPO_ROOT / "governance" / "custodian_registry.yaml"
OUTPUT = REPO_ROOT / "docs" / "cro-dashboard.md"

ROWS = [
    ("Evidence Automation", "Compliance decay", "Governance Spine", "🟢"),
    ("Human Ownership", "Role ambiguity", "Custodian Registry", "🟢"),
    ("Version/Time", "Policy drift", "CCR tagging", "🟡"),
    ("Legal Crosswalk", "Regulatory shock", "Framework mapping", "🟢"),
    ("Learning Loop", "Repeat incidents", "GDS retros", "🟢"),
    ("Communication", "Mistrust spiral", "Public AEIP keys", "🟢"),
]


def load_registry_summary() -> str:
    if not REGISTRY_FILE.exists():
        return "No registry available"
    entries = [line.strip() for line in REGISTRY_FILE.read_text(encoding="utf-8").splitlines() if line.strip().startswith("holder:")]
    return f"Custodians on file: {len(entries)}"


def load_metrics_summary() -> str:
    if not METRICS_FILE.exists():
        return "Metrics unavailable"
    data = json.loads(METRICS_FILE.read_text(encoding="utf-8"))
    return ", ".join(f"{key} {(value*100):.1f}%" for key, value in data["values"].items())


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# CRO Risk Dashboard", "", f"_Metrics_: {load_metrics_summary()}.", f"_Custodians_: {load_registry_summary()}.", ""]
    lines.append("| Domain | Risk | Control | Status |")
    lines.append("| --- | --- | --- | --- |")
    for row in ROWS:
        lines.append("| " + " | ".join(row) + " |")
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
