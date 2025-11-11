<!-- SPDX-License-Identifier: CC-BY-NC-ND-4.0 -->

# Heartwood Core Specification

## Overview
The Heartwood Core coordinates persona orchestration, Layer 04 instruction controls, and Layer 05 reasoning exchanges. It establishes the civic trunk that all persona branches connect to, ensuring every intervention is logged through AEIP evidence linked to the clause registry (`reference/clause_index.yaml`).

## The Eight Stabilizing Rings
1. **Mandate Integrity Ring** — Aligns governance intents with Clauses L00-C001 through L00-C003 and validates quorum events before Layer 04 policy propagation.
2. **Compute Custody Ring** — Monitors hardware attestations from Clauses L01-C001 to L01-C003 to ensure physical substrate readiness before persona activation.
3. **Data Stewardship Ring** — Verifies Clauses L02-C001 to L02-C003, blocking persona interactions when provenance or consent envelopes lapse.
4. **Model Alignment Ring** — Applies Clauses L03-C001 to L03-C003 to guarantee persona prompts inherit approved use cases and traceable datasets.
5. **Instruction Control Ring** — Couples with Layer 04 Clauses L04-C001 to L04-C003, mediating safeguard overrides and red team feedback before release.
6. **Reasoning Assurance Ring** — Couples with Layer 05 Clauses L05-C001 to L05-C003, confirming transcript fidelity and persona hand-offs during deliberations.
7. **Deployment Cohesion Ring** — Implements Clauses L06-C001 to L06-C003 so that integrations and rollbacks preserve civic transparency.
8. **Resilience Resonance Ring** — Maps Clauses L12-C001 to L12-C003 and related higher-layer obligations, ensuring adaptive learning cycles inform future persona conduct.

## Persona Interfaces
- **Custodial Persona Interface** — Governs editorial personas interacting with Layer 04; all requests must include AEIP envelopes referencing Clauses L04-C001 and L11-C001 for auditability.
- **Deliberative Persona Interface** — Coordinates Layer 05 observers and facilitators; transcripts and context retention are validated against Clauses L05-C001 and L05-C002.
- **Community Liaison Interface** — Handles participatory inputs from Layer 08 assemblies; responses must cite Clauses L08-C001 to L08-C003 to certify accessibility and feedback loops.

Each interface enforces persona role definitions from the Persona Architecture and ensures escalations invoke Clause L09-C003 for epistemic challenges.

Persona definitions SHALL embed AEIP logging hooks that automatically capture the active `clause_id` and `timestamp` prior to any instruction, ensuring parity with Clauses L04-C001, L05-C002, and L08-C003.

## AEIP Hooks
- **Envelope Composition** — Every persona action composes AEIP envelopes including `clause_id`, `timestamp`, and `persona_id` fields, referencing clauses such as L04-C001, L05-C003, and L07-C003.
- **Routing Registry** — Heartwood maintains a registry mapping AEIP routes to clause families, ensuring manifest pointers like `aeip.layer04.control.policyRegistry` resolve without ambiguity.
- **Ledger Sync** — Successful envelopes trigger Integrity Ledger entries that reuse the hashes sealed in `audits/Integrity_Ledger.md` and validate against the active canonical commit recorded therein.

## Safety Logic
- **Pre-Instruction Checks** — Before any Layer 04 instruction is executed, Heartwood verifies stabilization rings 1–5 and confirms AEIP hooks referencing Clauses L04-C001 to L04-C003 are present.
- **Reasoning Guardrails** — During Layer 05 exchanges, the core enforces persona hand-off logging (Clause L05-C002) and halts interactions if transcripts are missing AEIP receipts.
- **Escalation Triggers** — Breaches of Clauses L02-C003, L06-C002, or L12-C002 automatically route to civic stewards through AEIP alerts flagged for immediate review.

## Decommissioning Procedures
1. **Persona Sunset Review** — Evaluate persona performance against Clauses L03-C002, L05-C003, and L08-C003; publish findings via AEIP notices.
2. **Asset and Data Hygiene** — Confirm that hardware, data, and model artefacts linked to the persona satisfy Clauses L01-C002, L02-C001, and L03-C003 before retirement.
3. **Ledger Closure** — Issue a final AEIP envelope referencing Clause L11-C002 with a timestamped summary, then record the associated hash in `audits/Integrity_Ledger.md`.
4. **Community Notification** — Disseminate decommissioning statements citing Clauses L07-C001 and L10-C003 to affected civic partners.
