#!/usr/bin/env python3
"""Compute governance metrics based on repository state."""

import datetime as dt
import glob
import json
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
GOV_DIR = REPO_ROOT / "governance-spine"
METRICS_DIR = GOV_DIR / "metrics"
METRICS_DIR.mkdir(parents=True, exist_ok=True)
METRICS_FILE = METRICS_DIR / "metrics.json"
HISTORY_FILE = METRICS_DIR / "history.json"

ARTIFACT_PATTERNS: Dict[str, List[str]] = {
    "CCM": ["governance-spine/**/*_CCM.yaml"],
    "ModelCard": ["governance-spine/**/*_ModelCard.yaml"],
    "IR": ["governance-spine/**/*_IR.yaml"],
    "AEIP": ["governance-spine/aeip/*.json"],
    "GDS": ["governance-spine/deployments/gds_*.md"],
    "Provenance": ["governance-spine/**/*_Provenance.yaml"],
}


def parse_assets() -> List[Dict[str, str]]:
    path = GOV_DIR / "assets.yaml"
    if not path.exists():
        return []
    entries: List[Dict[str, str]] = []
    current: Dict[str, str] | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
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


def count_artifact(artifact: str) -> int:
    total = 0
    for pattern in ARTIFACT_PATTERNS.get(artifact, []):
        total += len(glob.glob(str(REPO_ROOT / pattern), recursive=True))
    return total


def compute_completion_ratio(artifact: str, total: int) -> float:
    if total == 0:
        return 0.0
    return min(count_artifact(artifact) / total, 1.0)


def update_history(
    timestamp: str, metrics: Dict[str, float]
) -> List[Dict[str, object]]:
    if HISTORY_FILE.exists():
        history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
    else:
        history = []
    history.append({"timestamp": timestamp, "values": metrics})
    history = history[-12:]
    HISTORY_FILE.write_text(json.dumps(history, indent=2), encoding="utf-8")
    return history


def build_trends_markdown(
    timestamp: str, metrics: Dict[str, float], history: List[Dict[str, object]]
):
    md_path = REPO_ROOT / "docs" / "metrics-trends.md"
    lines = ["# Governance Metrics Trends", "", f"_Generated at {timestamp}_.", ""]
    for key, value in metrics.items():
        lines.append(f"- **{key}**: {value:.2%}")
    lines.append("")
    lines.append('<div id="metrics-trend-chart"></div>')
    lines.append('<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>')
    lines.append("<script>")
    lines.append("const history = " + json.dumps(history) + ";")
    lines.append("const timestamps = history.map(point => point.timestamp);")
    for metric in metrics.keys():
        lines.append(
            "const series_"
            + metric.lower()
            + " = {"
            + f"x: timestamps, y: history.map(point => point.values['{metric}']), name: '{metric}', mode: 'lines+markers'"
            + "};"
        )
    series_list = ", ".join([f"series_{metric.lower()}" for metric in metrics.keys()])
    lines.append(
        f"Plotly.newPlot('metrics-trend-chart', [{series_list}], {{title: 'Governance Metric Trends', yaxis: {{tickformat: '.0%'}}}});"
    )
    lines.append("</script>")
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    assets = parse_assets()
    total_assets = len(assets)
    metrics = {
        "PCI": compute_completion_ratio("CCM", total_assets or 1),
        "CVR": compute_completion_ratio("ModelCard", total_assets or 1),
        "DDR": 1.0 - compute_completion_ratio("IR", total_assets or 1),
        "AES": compute_completion_ratio("AEIP", total_assets or 1),
        "BMC": compute_completion_ratio("GDS", 1),
        "SLGI": compute_completion_ratio("Provenance", total_assets or 1),
    }

    timestamp = dt.datetime.utcnow().isoformat() + "Z"
    payload = {
        "generated_at": timestamp,
        "values": metrics,
    }
    METRICS_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    history = update_history(timestamp, metrics)
    build_trends_markdown(timestamp, metrics, history)


if __name__ == "__main__":
    main()
