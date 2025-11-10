Layer/Theme: layer_instruction_control
Version: v5.0-open-core
Purpose: Regulate prompts and human guidance for AI OSI v5 services.

# L4 Instruction Control

Instruction control SHALL ensure that system prompts, workflows, and human oversight guard against misuse. All instructions SHALL remain transparent and adjustable through civic feedback.

## Control Components

- Documented instruction sets with rationale tied to the ethical charter.
- Guardrails preventing harmful or discriminatory outputs.
- Escalation procedures for ambiguous or high-risk requests.
- Public change log capturing updates to prompts or workflows.

## Stewardship Actions

1. Review instructions with community observers to confirm clarity and fairness.
2. Test instructions using diverse scenarios, especially edge cases raised by impacted people.
3. Publish a Public Attestation Step before rolling out significant instruction updates.

## Interfaces

- Receives model capabilities from [L3 Model Development](model_development.md).
- Coordinates with [../guides/philosophy_ethics.md](../guides/philosophy_ethics.md) for refusal logic and dignity guidelines.
- Provides operational context to [L5 Deployment Integration](deployment_integration.md).

## What Good Looks Like

- Instructions explicitly cite civic principles and intended user protections.
- Feedback loops exist for users to report confusing or harmful behaviors.
- Updates are versioned with timestamps and steward endorsements recorded in public logs.

## Common Failure Modes

- Hidden instruction changes without public notice.
- Instructions focusing on efficiency over civic safeguards.
- Lack of human review for escalated or sensitive scenarios.

## Worked Example

A social services chatbot maintains a library of prompts that require empathy, multilingual support, and automatic referral to human caseworkers for crisis situations. Stewards test instructions with advocacy groups quarterly and publish revisions with rationale.

Traceability

Keys: Layer=L4, Instruction_Record=IC-2024
Open Civic Artefacts

- Transparency Record: Instruction Review Minutes
- Transparency Record: Instruction Update Attestations

```sql
-- Copy code
SELECT artefact_id, version_tag
FROM transparency_registry
WHERE layer = 'L4';
```
