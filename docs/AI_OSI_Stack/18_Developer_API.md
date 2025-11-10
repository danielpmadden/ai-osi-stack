© 2025 Daniel P. Madden — Custodial Author
AI OSI Stack v5.0-open-core (Civic Standard Edition)

© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
# Developer API Guide

- **Layer/Theme:** AEIP and Control Tower Interfaces
- **Version:** v5.0-rc
- **Source Reference:** `technology_base.integration_points`
- **Last Generated:** 2025-11-10T00:00:49Z

## API Surfaces
1. **AEIP Handshake Endpoints:** SHALL accept JSON payloads for Intent, Justify, CounterSign, Commit, and Update stages. Each endpoint MUST validate mandate IDs and charter obligation hashes.
2. **Governance Control Tower API:** SHOULD expose REST and WebSocket channels for asset registries, manifest ingestion, and telemetry streaming.
3. **Dashboard Integration Hooks:** SHALL deliver standards crosswalk views referencing [Governance Publication](./11_Layer_7_Governance_Publication.md).

## Example AEIP Handshake Payload
```json
{
  "mandate_id": "CM-2025-001",
  "layer": 5,
  "stage": "Commit",
  "obligation_hash": "sha256-...",
  "justification_ref": "aeip://intent/12345",
  "countersignatures": ["civic-custodian", "model-owner"],
  "timestamp": "2025-11-10T00:00:49Z"
}
```
Payloads SHALL include countersignatures from relevant custodians before acceptance.

## Authentication and Security
- APIs SHALL enforce mTLS and token-based access with deferred signing constraints.
- Audit logs SHOULD be exported to the Integrity Ledger for end-to-end traceability.

## Developer Workflow
- Use `govspine` Python client to simulate AEIP exchanges prior to deployment.
- Align schema definitions with AJV validators in the TypeScript toolchain.
- Reference [Testing Framework](./19_Testing_Framework.md) to automate payload validation.

---
Traceability
- JSON: `technology_base.integration_points`
- AEIP Artefacts: AEIP Handshake Payloads, Governance Control Tower API Contracts, Dashboard Integration Hooks
---
