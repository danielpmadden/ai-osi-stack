import datetime as dt
import json
import os
from pathlib import Path
from typing import Dict, List, Optional

import httpx
import yaml
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parents[2]
GOVERNANCE_DIR = BASE_DIR / "governance"
ASSET_REGISTRY = GOVERNANCE_DIR / "assets.yaml"
METRICS_FILE = GOVERNANCE_DIR / "metrics" / "metrics.json"
SCHEMAS_DIR = BASE_DIR / "schemas"
TEMPLATES = {
    "model": ["ModelCard"],
    "dataset": ["CCM"],
    "asset": ["AEIP", "IR"],
}
SHARED_ARTIFACTS = {
    "model": ["CCM", "IR", "AEIP", "GDS"],
    "dataset": ["Provenance", "IR"],
    "asset": ["RiskAssessment", "CCM"],
}

app = FastAPI(title="Governance Control Tower API")
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"]
)


class Asset(BaseModel):
    asset_id: str
    name: str
    type: str
    owner: str
    registered_at: dt.datetime
    required_artifacts: List[str]

    def to_dict(self) -> Dict:
        data = self.dict()
        data["registered_at"] = self.registered_at.isoformat()
        return data


class AssetCreate(BaseModel):
    asset_id: str
    name: str
    type: str
    owner: str


class AssetStatus(BaseModel):
    asset_id: str
    name: str
    type: str
    owner: str
    status: str
    missing_artifacts: List[str]


class MetricsResponse(BaseModel):
    generated_at: str
    values: Dict[str, float]


SLACK_WEBHOOK = os.getenv("GOVERNANCE_SLACK_WEBHOOK")
GITHUB_WEBHOOK = os.getenv("GOVERNANCE_GITHUB_WEBHOOK")


def _load_assets() -> List[Asset]:
    if not ASSET_REGISTRY.exists():
        return []
    with ASSET_REGISTRY.open("r", encoding="utf-8") as handle:
        raw = yaml.safe_load(handle) or []
    assets = []
    for item in raw:
        try:
            registered_at = dt.datetime.fromisoformat(item["registered_at"])
        except Exception:
            registered_at = dt.datetime.utcnow()
        assets.append(
            Asset(
                asset_id=item["asset_id"],
                name=item["name"],
                type=item["type"],
                owner=item["owner"],
                registered_at=registered_at,
                required_artifacts=item.get("required_artifacts", []),
            )
        )
    return assets


def _save_assets(assets: List[Asset]) -> None:
    ASSET_REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    payload = [asset.to_dict() for asset in assets]
    with ASSET_REGISTRY.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(payload, handle, sort_keys=False)


def _artifact_path(asset: Asset, artifact_name: str) -> Optional[Path]:
    candidate = GOVERNANCE_DIR / asset.type / f"{asset.asset_id}_{artifact_name}.yaml"
    if candidate.exists():
        return candidate
    legacy = GOVERNANCE_DIR / f"{asset.asset_id}_{artifact_name}.yaml"
    if legacy.exists():
        return legacy
    return None


def _compute_status(asset: Asset) -> AssetStatus:
    expected = set(asset.required_artifacts + SHARED_ARTIFACTS.get(asset.type, []))
    missing: List[str] = []
    for artifact in expected:
        if not _artifact_path(asset, artifact):
            missing.append(artifact)
    if missing:
        status = "amber" if len(missing) < len(expected) else "red"
    else:
        status = "green"
    return AssetStatus(
        asset_id=asset.asset_id,
        name=asset.name,
        type=asset.type,
        owner=asset.owner,
        status=status,
        missing_artifacts=missing,
    )


def _notify(message: str, payload: Dict):
    if SLACK_WEBHOOK:
        try:
            httpx.post(SLACK_WEBHOOK, json={"text": message, "attachments": [payload]})
        except httpx.HTTPError:
            pass
    if GITHUB_WEBHOOK:
        try:
            httpx.post(GITHUB_WEBHOOK, json={"body": message, "metadata": payload})
        except httpx.HTTPError:
            pass


@app.get("/api/assets", response_model=List[AssetStatus])
def list_assets():
    return [_compute_status(asset) for asset in _load_assets()]


@app.post("/api/assets", response_model=AssetStatus, status_code=201)
def register_asset(asset: AssetCreate):
    assets = _load_assets()
    if any(item.asset_id == asset.asset_id for item in assets):
        raise HTTPException(status_code=400, detail="Asset already registered")
    if asset.type not in TEMPLATES:
        raise HTTPException(status_code=400, detail="Unsupported asset type")
    required = TEMPLATES[asset.type]
    record = Asset(
        asset_id=asset.asset_id,
        name=asset.name,
        type=asset.type,
        owner=asset.owner,
        registered_at=dt.datetime.utcnow(),
        required_artifacts=required,
    )
    assets.append(record)
    _save_assets(assets)
    status = _compute_status(record)
    _notify(
        f"Registered {asset.type} {asset.asset_id}",
        {
            "owner": asset.owner,
            "status": status.status,
            "missing": status.missing_artifacts,
        },
    )
    return status


@app.get("/status/{asset_id}", response_model=AssetStatus)
def status(asset_id: str):
    for asset in _load_assets():
        if asset.asset_id == asset_id:
            status_payload = _compute_status(asset)
            if status_payload.status == "red":
                _notify(
                    f"Compliance alert for {asset.asset_id}",
                    {"missing": status_payload.missing_artifacts, "owner": asset.owner},
                )
            return status_payload
    raise HTTPException(status_code=404, detail="Asset not found")


@app.get("/api/metrics", response_model=MetricsResponse)
def metrics():
    if not METRICS_FILE.exists():
        raise HTTPException(status_code=404, detail="Metrics unavailable")
    with METRICS_FILE.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return MetricsResponse(
        generated_at=payload["generated_at"], values=payload["values"]
    )


@app.get("/api/templates")
def list_templates():
    entries: List[Dict[str, str]] = []
    for path in sorted(SCHEMAS_DIR.glob("*.template.*")):
        entries.append({"name": path.name, "path": f"/schemas/{path.name}"})
    return entries


@app.get("/api/tasks")
def outstanding_tasks():
    assets = [_compute_status(asset) for asset in _load_assets()]
    tasks = []
    for asset in assets:
        for artifact in asset.missing_artifacts:
            tasks.append(
                {
                    "asset_id": asset.asset_id,
                    "artifact": artifact,
                    "owner": asset.owner,
                    "status": asset.status,
                }
            )
    return tasks
