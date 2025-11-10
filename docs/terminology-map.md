© 2025 Daniel P. Madden — Custodial Author
AI OSI Stack v5.0-open-core (Civic Standard Edition)

© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Terminology to AEIP Field Map

| Term | Description | AEIP Reference |
| --- | --- | --- |
| Transparency | Public visibility into obligations, logs, and remediation decisions. | `schemas/aeip/gds-schema.json` (`disclosureRegister`) |
| Audit | Independent review of artefacts, logs, and controls. | `schemas/aeip/aeip-frame-schema.json` (`auditTrail`) |
| Custodian | Steward accountable for AEIP artefacts and governance actions. | `schemas/aeip/aeip-frame-schema.json` (`custodianRecords[]`) |
| Integrity | Assurance that records remain unaltered and provenance is traceable. | `schemas/aeip/aeip-frame-schema.json` (`integrityNotes`) |
| Provenance | Documented lineage connecting civic mandate to operational evidence. | `schemas/aeip/aeip-frame-schema.json` (`provenanceBundle`) |
| Witness | Civic or institutional observer who records independent verification steps. | `schemas/aeip/aeip-frame-schema.json` (`witnessLogs[]`) |
| Advisory checksum | Guidance instructing verifiers to capture their own hash values. | `schemas/aeip/aeip-frame-schema.json` (`checksumGuidance`) |
| Ledger | Append-only record of governance events and custody changes. | `schemas/aeip/aeip-frame-schema.json` (`ledgerReference`) |
| Persona | Role-based accountability profile with mandates and permissions. | `schemas/persona/persona-manifest.jsonld` (`personaBinding`) |
| Appeal | Civic recourse mechanism for contesting AI outcomes. | `schemas/aeip/incident-report-schema.json` (`appealChannel`) |
