#!/usr/bin/env python3
"""Notify Slack webhook when assets reach red compliance state."""

import json
import os
from pathlib import Path
import urllib.request

REPO_ROOT = Path(__file__).resolve().parents[1]
ASSET_FILE = REPO_ROOT / "governance" / "assets.yaml"


def parse_assets():
    assets = []
    current = None
    for line in ASSET_FILE.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("- ") and ":" in stripped:
            if current:
                assets.append(current)
            current = {}
            key, value = [part.strip() for part in stripped[2:].split(":", 1)]
            current[key] = value
        elif ":" in line and current is not None:
            key, value = [part.strip() for part in line.split(":", 1)]
            current[key] = value
    if current:
        assets.append(current)
    return assets


def find_missing(asset):
    asset_id = asset.get("asset_id")
    expected = {"ModelCard", "CCM", "IR", "AEIP", "GDS"}
    missing = []
    for item in expected:
        if (
            not list(REPO_ROOT.glob(f"governance-spine/**/*{asset_id}_{item}.yaml"))
            and item != "GDS"
        ):
            missing.append(item)
        if item == "GDS" and not list(
            (REPO_ROOT / "governance" / "deployment").glob("gds_*.md")
        ):
            missing.append("GDS")
    return missing


def send_slack(message: str):
    webhook = os.getenv("SLACK_WEBHOOK")
    if not webhook:
        print(message)
        return
    data = json.dumps({"text": message}).encode("utf-8")
    req = urllib.request.Request(
        webhook, data=data, headers={"Content-Type": "application/json"}
    )
    urllib.request.urlopen(req)


def main():
    if not ASSET_FILE.exists():
        return
    for asset in parse_assets():
        missing = find_missing(asset)
        if len(missing) >= 3:
            message = f"🚨 {asset['asset_id']} is RED. Missing artifacts: {', '.join(missing)}"
            send_slack(message)


if __name__ == "__main__":
    main()
