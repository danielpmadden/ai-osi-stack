© 2025 Daniel P. Madden — Custodial Author
AI OSI Stack v5.0-open-core (Civic Standard Edition)

© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
# Technology Base

- **Layer/Theme:** Tooling and Integration Stack
- **Version:** v5.0-rc
- **Source Reference:** `technology_base`
- **Last Generated:** 2025-11-10T00:00:49Z

## Languages and Frameworks
- **Python Runtime (`govspine/`):** Utilizes pytest and jsonschema for AEIP and layer validation. Teams SHALL maintain reproducible virtual environments.
- **TypeScript/Node Toolchain:** Employs AJV, Vitest, Vite, and linting suites. Developers SHOULD keep schema definitions synchronized with Python validators.
- **FastAPI + SQLModel Backend:** Provides APIs for the Governance Control Tower, backed by a React dashboard. Integrators SHALL enforce authenticated access to governance artefacts.

## Dependencies
- **Python Packages:** pytest, jsonschema.
- **Node Dependencies:** ajv, ajv-formats, @typescript-eslint, prettier, vitest, tsx, typescript.
- **Operational CLIs:** Syft, Trivy, Gitleaks, jq, Docker for reproducible validation.

## Integration Points
1. **AEIP Handshake Pipelines:** SHALL enforce Intent→Justify→CounterSign→Commit→Update flows across layers.
2. **Governance Control Tower API:** SHOULD manage asset registries, manifest ingestion, and audit telemetry synchronization with `govspine/` artefacts.
3. **Dashboard Visualizations:** SHALL align AEIP manifests with standards crosswalks for regulators and auditors, linking to [Comparative Models](./23_Comparative_Models.md).

## Implementation Notes
- Use containerized builds to ensure deferred signing constraints are respected.
- Configure CI pipelines to generate [Testing Framework](./19_Testing_Framework.md) reports and feed results into the Integrity Ledger.

---
Traceability
- JSON: `technology_base.languages_frameworks`, `technology_base.dependencies`, `technology_base.integration_points`
- AEIP Artefacts: AEIP Handshake Pipelines, Governance Control Tower API Specs, Dashboard Registry Exports
---
