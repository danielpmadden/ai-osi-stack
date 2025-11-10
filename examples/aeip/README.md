© 2025 Daniel P. Madden — Custodial Author
AI OSI Stack v5.0-open-core (Civic Standard Edition)

© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
# AEIP Receipt Examples

This directory provides synthetic AEIP receipts illustrating the governance lifecycle. Each JSON-LD file includes the required metadata for downstream validators and dashboards.

## Files

- `intent.jsonld` — Civic mandate establishing the initiative.
- `justify.jsonld` — Governance justification linking to evidence.
- `countersign.jsonld` — Oversight countersignature confirming readiness.
- `commit.jsonld` — Deployment commitment with production controls.
- `update.jsonld` — Post-deployment update referencing telemetry.

## Shared Fields

All receipts include:

- `lifecycle` — The current AEIP stage.
- `privacy.scope` — Declares whether personal data is present.
- `provenance.source` — System or process responsible for the record.
- `uncertainty.score` — Normalized risk score (0–1) for residual uncertainty.
- `signatures` — Placeholder signature blocks; values are redacted pending key ceremonies.
- `hashes` — Deterministic SHA-512 placeholders for cross-referencing the ledger.

Use `ops/aeip/convert-for-dashboard.ts` to normalize these receipts for static dashboards and `ops/aeip/validate-aeip.ts` to ensure schema compliance.
