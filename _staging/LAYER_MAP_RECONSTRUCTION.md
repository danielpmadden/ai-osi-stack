# Layer Map Reconstruction — v5.0-open-core

## Overview
This reconstruction refreshes the conceptual map between the AI OSI Stack layers and their governing AEIP schemas. All layer documents in `docs/AI_OSI_Stack/` now reference the definitive schemas that validate artefacts, restoring traceability promised in the v5.0-open-core documentation set.

## Layer-to-Schema Matrix
| Layer | Documentation | AEIP Schema References | Notes |
| --- | --- | --- | --- |
| Layer 0 – Civic Mandate | `docs/AI_OSI_Stack/04_Layer_0_Civic_Mandate.md` | `schemas/aeip/aeip-intent.schema.json`, `schemas/aeip/civic-charter-schema.json` | Intent receipts and charter manifests anchor democratic authority.
| Layer 1 – Ethical Charter | `docs/AI_OSI_Stack/05_Layer_1_Ethical_Charter.md` | `schemas/aeip/aeip-justify.schema.json`, `schemas/aeip/tecl-schema.json` | Governance justifications and TECL manifests enforce charter fidelity.
| Layer 2 – Data Stewardship | `docs/AI_OSI_Stack/06_Layer_2_Data_Stewardship.md` | `schemas/aeip/ccm-schema.json` | CCM validates consent, retention, and fiduciary handling.
| Layer 3 – Model Development | `docs/AI_OSI_Stack/07_Layer_3_Model_Development.md` | `schemas/aeip/modelcard-schema.json` | Model card schema preserves lineage and evaluation evidence.
| Layer 4 – Instruction & Control | `docs/AI_OSI_Stack/08_Layer_4_Instruction_Control.md` | `schemas/aeip/instruction-log-schema.json`, `schemas/aeip/aeip-frame-schema.json` | Instruction logs and AEIP frames govern prompt routing and custody.
| Layer 5 – Reasoning Exchange | `docs/AI_OSI_Stack/09_Layer_5_Reasoning_Exchange.md` | `schemas/aeip/aeip-countersign.schema.json`, `schemas/aeip/aeip-frame-schema.json` | Countersignature receipts and frames sustain multi-party reasoning integrity.
| Layer 6 – Deployment & Integration | `docs/AI_OSI_Stack/10_Layer_6_Deployment_Integration.md` | `schemas/aeip/aeip-commit.schema.json`, `schemas/aeip/gds-schema.json`, `schemas/aeip/incident-report-schema.json`, `schemas/aeip/aeip-frame-schema.json` | Commit receipts, governance decision summaries, incident reports, and frames cover release to remediation controls.
| Layer 7 – Governance Publication | `docs/AI_OSI_Stack/11_Layer_7_Governance_Publication.md` | `schemas/aeip/aeip-update.schema.json`, `schemas/aeip/gds-schema.json`, `schemas/aeip/aeip-frame-schema.json` | Update receipts and decision summaries document public disclosures.
| Layer 8 – Civic Participation | `docs/AI_OSI_Stack/12_Layer_8_Civic_Participation.md` | `schemas/aeip/aeip-update.schema.json`, `schemas/integrity-ledger-entry.jsonld` | Update receipts and Integrity Ledger entries certify renewal loops.

## Verification Notes
- Each layer chapter now includes a **“AEIP Schema Alignment”** section with explicit links to the relevant schema files.
- Traceability blocks were updated to cite the governing schemas so auditors can navigate from documentation to validation assets without ambiguity.
- Cross-layer links were reviewed to confirm upstream/downstream references (e.g., Charter → Data Stewardship → Model Development) remain intact after the regeneration.

## IP Boundary Confirmation
- No proprietary runtime code, deployment scripts, or closed-source dependencies were added or modified. Changes are confined to documentation and staging notes within the open-core boundary.
