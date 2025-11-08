# SPDX-License-Identifier: Apache-2.0

# SPDX-License-Identifier: Apache-2.0
#!/usr/bin/env python3
"""Ensure datasets and models carry required governance artifacts."""

from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
GOV_DIR = REPO_ROOT / "governance"
ASSET_FILE = GOV_DIR / "assets.yaml"

REQUIREMENTS: Dict[str, List[str]] = {
    "model": ["ModelCard", "CCM", "IR", "AEIP"],
    "dataset": ["CCM", "Provenance", "IR"],
    "asset": ["AEIP", "IR"],
}


def parse_assets() -> List[Dict[str, str]]:
    if not ASSET_FILE.exists():
        return []
    assets: List[Dict[str, str]] = []
    current: Dict[str, str] | None = None
    for line in ASSET_FILE.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped:
            continue
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


def has_artifact(asset_id: str, artifact: str) -> bool:
    candidates = list(GOV_DIR.glob(f"**/{asset_id}_{artifact}.yaml"))
    return bool(candidates)


def main() -> int:
    assets = parse_assets()
    failures = []
    for asset in assets:
        required = REQUIREMENTS.get(asset.get("type", ""), [])
        for artifact in required:
            if not has_artifact(asset.get("asset_id"), artifact):
                failures.append(f"{asset['asset_id']} missing {artifact}")
    if failures:
        for failure in failures:
            print(failure)
        return 1
    print("Integrity check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
