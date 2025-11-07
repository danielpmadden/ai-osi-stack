# Governance Control Tower — Scaffold

The Control Tower pairs a FastAPI back-end with a React dashboard to register governance spine assets, manage AEIP manifests, and visualise compliance metrics.

## Architecture Overview

- **FastAPI service (`apps/control_tower/api`)**
  - REST endpoints for `POST /asset`, `POST /manifest`, and `GET /audit`.
  - SQLite persistence via SQLModel with tables for assets, manifests, and audit events.
  - Background tasks publish integrity summaries to `govspine/` manifests.
- **React dashboard (`apps/control_tower/dashboard`)**
  - Vite + TypeScript scaffold with components for asset registry, manifest crosswalk, and risk metrics timeline.
  - Consumes the FastAPI endpoints using the shared schema definitions in `apps/control_tower/api/schemas.ts`.
  - Includes reusable cards for Appendix cross-references and AEIP validation status.

## FastAPI Bootstrap

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi[all] sqlmodel uvicorn pydantic-settings
cd apps/control_tower/api
uvicorn main:app --reload --host 0.0.0.0 --port 8082
```

### Route Contract

- `POST /asset`
  - Request: `{ "asset_id": "charter.l4.ethics", "asset_type": "charter", "owner": "Civic Mandate Custodians" }`
  - Response: Stored asset row with timestamps and layer metadata.
- `POST /manifest`
  - Request body mirrors the AEIP manifest schema; payloads are versioned and linked to registered assets.
  - Side-effect: writes the manifest JSON to the appropriate `govspine/<type>/` directory via `tools/governance_manifest.py` helpers.
- `GET /audit`
  - Returns paginated audit events including ledger receipt references, AEIP validation summaries, and outstanding remediation tasks.

## React Dashboard Bootstrap

```bash
cd apps/control_tower
npm create vite@latest dashboard -- --template react-ts
cd dashboard
npm install
npm install @tanstack/react-query recharts axios
npm run dev -- --host --port 5176
```

### Core Views

1. **Asset Registry** — Table component backed by `react-query` that surfaces lifecycle state, risk tier, and last ledger receipt.
2. **Manifest Crosswalk** — Visual alignment grid between AEIP fields, Appendix references, and control mappings. Supports CSV export for audits.
3. **Resilience Metrics** — Chart suite for incident response timing, ledger drift deltas, and community witness confirmations sourced from `/audit`.

## Automation Hooks

- Add `apps/control_tower/api/cli.py` with commands to sync database tables, run integrity tests, and invoke `tools/integrity_check.py`.
- Configure pre-commit hooks to lint both Python (`ruff`, `black`) and React (`eslint`, `prettier`).
- Extend `Makefile` with targets `control-tower-api` and `control-tower-dashboard` for common dev workflows.

## Next Steps

1. Implement SQLModel models (`Asset`, `Manifest`, `AuditEvent`) with ALEMBIC migrations.
2. Integrate AEIP signature validation by calling `tools/verify_aeip_signatures.py` before persisting manifests.
3. Add OpenAPI schema export to `docs/governance-dashboard/static/openapi.json` for downstream tooling.
