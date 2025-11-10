© 2025 Daniel P. Madden — Custodial Author
AI OSI Stack v5.0-open-core (Civic Standard Edition)

© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
# Layer 1 – Ethical Charter

- **Layer/Theme:** Obligations and Red Lines
- **Version:** v5.0-rc
- **Source Reference:** `layer_structure.layers[1]`
- **Last Generated:** 2025-11-20T00:00:00Z

## Purpose
Layer 1 translates civic values into enforceable obligations, red lines, and review cycles. It SHALL operationalize mandates into language consumable by legal, technical, and civic teams.

## Core Functions
- Define personas, duty of care statements, and refusal logic for [Layer 4 – Instruction & Control](./08_Layer_4_Instruction_Control.md).
- Specify risk registries feeding [Layer 2 – Data Stewardship](./06_Layer_2_Data_Stewardship.md) and [Layer 3 – Model Development](./07_Layer_3_Model_Development.md).
- Establish oversight cadence, including mandatory review intervals and escalation triggers.

## Dependencies
This layer references mandate identifiers from [Layer 0](./04_Layer_0_Civic_Mandate.md). All obligations MUST be versioned and hashed before distribution via AEIP.

## Required Artefacts
- **Ethical Charter Manifest:** SHALL outline duties, prohibited uses, and appeal pathways.
- **Persona Governance Briefs:** SHOULD define behavioral boundaries and refusal statements.
- **Review Cycle Calendar:** MUST align oversight dates with civic renewal triggers.

## Governance Controls
- AEIP payloads SHALL reject instructions violating charter prohibitions.
- Charter updates SHOULD trigger downstream checks in [Layer 2](./06_Layer_2_Data_Stewardship.md) and [Layer 5 – Reasoning Exchange](./09_Layer_5_Reasoning_Exchange.md).

## AEIP Schema Alignment
- **Governance Justification Receipt:** [`schemas/aeip/aeip-justify.schema.json`](../../schemas/aeip/aeip-justify.schema.json) SHALL document the rationale for each charter clause before it propagates to dependent layers.
- **Trusted Ethical Charter Ledger (TECL):** [`schemas/aeip/tecl-schema.json`](../../schemas/aeip/tecl-schema.json) MUST capture signed charter manifests and review cadence metadata for audit replay.

---
Traceability
- JSON: `layer_structure.layers[1].name`, `layer_structure.layers[1].function`, `layer_structure.layers[1].dependencies`
- AEIP Artefacts & Schemas: Ethical Charter Manifest, Persona Governance Briefs, Review Cycle Calendar; governed through [`schemas/aeip/aeip-justify.schema.json`](../../schemas/aeip/aeip-justify.schema.json) and [`schemas/aeip/tecl-schema.json`](../../schemas/aeip/tecl-schema.json)
---
