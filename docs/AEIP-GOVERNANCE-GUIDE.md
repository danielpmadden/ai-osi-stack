<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# AEIP Governance Guide

This guide connects AEIP receipts, governance schemas, and the dashboard representation used for transparency reporting.

## AEIP Lifecycle

1. **Intent** — Civic mandate establishing authority.
2. **Justify** — Ethical rationale referencing deliberation outcomes.
3. **CounterSign** — Oversight confirmation with risk analysis.
4. **Commit** — Deployment authorization and rollback preparedness.
5. **Update** — Post-deployment telemetry and accountability loops.

Receipts for each stage live in [`examples/aeip/`](../examples/aeip/). Validators enforce lifecycle continuity via `tests/aeip-lifecycle-validator.py`.

## Schema Expectations

- Schemas are stored under [`schemas/aeip/`](../schemas/aeip/).
- `ops/aeip/validate-aeip.ts` validates lifecycle receipts against dedicated schemas (`aeip-*.schema.json`).
- `ops/aeip/validate-governance.ts` validates civic charter, governance decision summaries, and incident reports, confirming canonical metadata and layer alignment.

### Required Fields

Each receipt includes:

- `lifecycle.current`, `previous`, `next`, `timestamp`
- `privacy.scope` (public, restricted, deidentified, internal)
- `provenance.source`, `provenance.method`, `jurisdiction`
- `uncertainty.score` in range `[0, 1]`
- `signatures` array with redacted placeholder values pending key ceremony
- `hashes.sha512` (128 hex characters)
- `linked_artifacts` referencing prior receipts or ledger URIs

## Dashboard Normalization

`ops/aeip/convert-for-dashboard.ts` converts receipts into a simplified structure consumed by static dashboards. The resulting JSON contains:

- `id`, `artifactType`, `layer`
- Lifecycle stage and timestamp
- Privacy scope and provenance source
- Uncertainty score and signature redaction status
- Hash and linked artifacts for cross-referencing

Use `npm run convert:dashboard` to produce `dist/dashboard-receipts.json` for dashboards or governance portals.

## Governance Ledger Integration

`ops/release/mk-dist.sh` and `ops/release/sign.sh` ensure ledger entries reference signed artifacts. Update `INTEGRITY_NOTICE.md` and `CANONICAL_PROVENANCE.yaml` whenever new AEIP receipts become canonical.

## Compliance Checklist

- [ ] AEIP receipts validated via Node/TypeScript scripts.
- [ ] Lifecycle integrity confirmed via pytest.
- [ ] SBOM and vulnerability scans archived.
- [ ] Signed artifacts have matching hashes recorded in `INTEGRITY_NOTICE.md`.
- [ ] Governance dashboard updated with normalized receipts.
