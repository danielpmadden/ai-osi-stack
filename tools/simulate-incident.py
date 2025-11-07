#!/usr/bin/env python3
"""Generate synthetic incident reports for drills."""

import argparse
import datetime as dt
import json
import random
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
INCIDENT_DIR = REPO_ROOT / "governance" / "postmortems"
IR_DIR = REPO_ROOT / "governance" / "incidents"
IR_DIR.mkdir(parents=True, exist_ok=True)

SCENARIOS = {
    "data_breach": {
        "summary": "Unauthorized access detected in partner dataset bucket.",
        "containment_minutes": (30, 120),
        "transparency_minutes": (60, 240),
    },
    "model_error": {
        "summary": "Model drift triggered high false-negative rate for civic alerts.",
        "containment_minutes": (45, 180),
        "transparency_minutes": (90, 360),
    },
    "civic_complaint": {
        "summary": "Civic coalition raised fairness complaint about deployment.",
        "containment_minutes": (120, 480),
        "transparency_minutes": (180, 600),
    },
}


def simulate(scenario: str) -> dict:
    today = dt.date.today()
    config = SCENARIOS[scenario]
    containment = random.randint(*config["containment_minutes"])
    transparency = random.randint(*config["transparency_minutes"])
    record = {
        "incident_id": f"SIM-{scenario.upper()}-{today.isoformat()}",
        "date": today.isoformat(),
        "scenario": scenario,
        "summary": config["summary"],
        "time_to_containment_minutes": containment,
        "time_to_transparency_minutes": transparency,
    }
    return record


def persist(record: dict) -> Path:
    path = IR_DIR / f"{record['incident_id']}.yaml"
    lines = [
        f"incident_id: {record['incident_id']}",
        f"date: {record['date']}",
        f"scenario: {record['scenario']}",
        f"summary: {record['summary']}",
        f"time_to_containment_minutes: {record['time_to_containment_minutes']}",
        f"time_to_transparency_minutes: {record['time_to_transparency_minutes']}",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def update_dashboard(record: dict) -> None:
    report_path = INCIDENT_DIR / f"incident_{record['date']}.md"
    if not report_path.exists():
        report_path.write_text(
            "\n".join(
                [
                    f"# Incident {record['date']}",
                    "",
                    "## Summary",
                    f"- **Impact:** Simulation",
                    f"- **Root Cause:** {record['summary']}",
                    f"- **Time to Containment:** {record['time_to_containment_minutes']} minutes.",
                    f"- **Time to Transparency:** {record['time_to_transparency_minutes']} minutes.",
                    "",
                    "## Timeline",
                    "- Simulated scenario executed automatically.",
                    "",
                    "## Lessons Learned",
                    "- Drill captured automatically via simulate-incident.py.",
                    "",
                    "## Actions",
                    "- Review synthetic drill outcomes in CRO dashboard.",
                ]
            )
            + "\n",
            encoding="utf-8",
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "scenario", choices=list(SCENARIOS.keys()), help="Incident scenario to simulate"
    )
    args = parser.parse_args()

    record = simulate(args.scenario)
    path = persist(record)
    update_dashboard(record)
    print(json.dumps({"saved": str(path), "record": record}, indent=2))


if __name__ == "__main__":
    main()
