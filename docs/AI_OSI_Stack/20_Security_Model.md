# Security Model

- **Layer/Theme:** Sealing, Signatures, and Deferred Signing
- **Version:** v5.0-rc
- **Source Reference:** `philosophy_ethics.responsible_usage`, `technology_base.dependencies`
- **Last Generated:** 2025-11-10T00:00:49Z

## Security Objectives
- Preserve provenance through deferred signing ceremonies.
- Ensure AEIP artefacts are cryptographically sealed and tamper-evident.
- Enforce least privilege across APIs and dashboards.

## Controls
1. **Deferred Signing:** SHALL withhold production keys until stewardship conditions are satisfied.
2. **Temporal Seals:** SHOULD timestamp AEIP payloads to maintain audit trails.
3. **mTLS and Token Enforcement:** SHALL protect Developer APIs detailed in [Developer API Guide](./18_Developer_API.md).
4. **Supply Chain Hygiene:** SHOULD run Syft, Trivy, and Gitleaks scans before deployment as outlined in [Testing Framework](./19_Testing_Framework.md).

## Incident Response
Security incidents SHALL trigger rollback procedures in [Layer 6 – Deployment & Integration](./10_Layer_6_Deployment_Integration.md). Governance teams MUST publish incident disclosures through [Layer 7 – Governance Publication](./11_Layer_7_Governance_Publication.md) and convene civic review panels per [Layer 8](./12_Layer_8_Civic_Participation.md).

---
Traceability
- JSON: `philosophy_ethics.responsible_usage`, `technology_base.dependencies`
- AEIP Artefacts: Deferred Signing Ledger, Temporal Seal Records, Security Incident Reports
---
