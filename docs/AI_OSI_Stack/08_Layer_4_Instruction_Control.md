# Layer 4 – Instruction & Control

- **Layer/Theme:** Prompt Governance and Intent Management
- **Version:** v5.0-rc
- **Source Reference:** `layer_structure.layers[4]`
- **Last Generated:** 2025-11-10T00:00:49Z

## Purpose
Layer 4 manages prompts, control policies, persona briefs, and AEIP intent preparation for runtime governance. It SHALL ensure that all instructions align with ethical constraints and are logged for downstream reasoning audits.

## Core Functions
- Curate instruction templates and persona briefs derived from [Layer 1 – Ethical Charter](./05_Layer_1_Ethical_Charter.md).
- Translate model capabilities from [Layer 3](./07_Layer_3_Model_Development.md) into runtime control levers.
- Emit instruction logs and policy fingerprints for [Layer 5 – Reasoning Exchange](./09_Layer_5_Reasoning_Exchange.md).

## Dependencies
This layer relies on model outputs and persona architectures, producing artefacts consumed by reasoning and deployment layers. AEIP SHALL enforce the Intent→Justify handshake before any instruction is executed.

## Required Artefacts
- **Instruction Control Policy:** MUST define allowed prompt classes, guardrails, and escalation steps.
- **Persona Briefs:** SHALL document persona intent, refusal logic, and oversight contacts.
- **Instruction Log Ledger:** SHOULD capture timestamped instructions, policy checks, and outcomes.

## Governance Controls
- Control policies SHALL reject prompts that violate charter prohibitions or data restrictions.
- Instruction logs SHOULD be hashed and shared with [Layer 6](./10_Layer_6_Deployment_Integration.md) for monitoring alignment.

---
Traceability
- JSON: `layer_structure.layers[4].name`, `layer_structure.layers[4].function`, `layer_structure.layers[4].dependencies`
- AEIP Artefacts: Instruction Control Policy, Persona Briefs, Instruction Log Ledger
---
