---
title: L4 Instruction Control
title_id: layer4-instruction-control
edition: civic
version: 1.0
status: draft
---

# L4 Instruction Control

## Purpose

Layer 4 governs how instructions, prompts, and interventions are crafted and moderated. It SHALL maintain alignment between human intentions and model behavior.

## Control Measures

- **Instruction Libraries.** Maintain open repositories of approved prompts, decision trees, and facilitation guides.
- **Context Windows.** Define what background information may be provided to models and who approves it.
- **Feedback Loops.** Collect user and staff feedback on instruction effectiveness and risks.
- **Override Protocols.** Provide manual interruption procedures when model outputs deviate from mandate or charter requirements.

## Documentation

| Document | Description |
| --- | --- |
| **Prompt Catalogue** | Versioned set of prompts with intended use, risk notes, and escalation contacts. |
| **Instruction Playbooks** | Scenario-based guides for frontline teams. |
| **Monitoring Logs** | Records of interventions, overrides, and lessons learned. |
| **Accessibility Notes** | Adaptations for different languages, abilities, and contexts. |

## Interfaces

- Receives model specifications from [L3 Model Development](L3_Model_Development.md).
- Supplies usage data and issues to [L5 Reasoning Exchange](L5_Reasoning_Exchange.md).
- Coordinates with [../20_GUIDES/Implementation_Guide.md](../20_GUIDES/Implementation_Guide.md) for deployment training.

## Accountability Checklist

- [ ] Prompt catalogue published with civic licensing.
- [ ] Override protocol tested and documented.
- [ ] Feedback loop includes community participants.
- [ ] Accessibility requirements verified through Public Attestation Steps.
