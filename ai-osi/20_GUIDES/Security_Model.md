---
title: Security Model
title_id: guide-security
edition: civic
version: 1.0
status: draft
---

# Security Model

## Purpose

This model outlines non-proprietary security practices that protect people, data, and infrastructure while honoring transparency commitments.

## Security Principles

- **Proportionality.** Security controls SHALL match the sensitivity of services and data.
- **Openness.** Document controls in plain language; avoid secrecy that prevents accountability.
- **Shared Responsibility.** Security is a collective practice across all layers.
- **Community Assurance.** Residents SHOULD understand and influence security decisions.

## Control Domains

| Domain | Description | Linked Layers |
| --- | --- | --- |
| **Governance Controls** | Policies and oversight mechanisms that enforce mandates and charters. | [L0](../10_LAYERS/L0_Civic_Mandate.md), [L1](../10_LAYERS/L1_Ethical_Charter.md) |
| **Data Protections** | Access management, encryption-at-rest, and minimization strategies. | [L2](../10_LAYERS/L2_Data_Stewardship.md) |
| **Model Integrity** | Safeguards against tampering, backdoors, or unapproved updates. | [L3](../10_LAYERS/L3_Model_Development.md) |
| **Instruction Safety** | Controls to prevent malicious or unsafe prompts. | [L4](../10_LAYERS/L4_Instruction_Control.md) |
| **Operational Resilience** | Backup, incident response, and continuity planning. | [L6](../10_LAYERS/L6_Deployment_Integration.md) |
| **Transparency Assurance** | Measures ensuring publication accuracy and accessibility. | [L7](../10_LAYERS/L7_Governance_Publication.md) |
| **Participation Safeguards** | Protecting participants from retaliation or harm. | [L8](../10_LAYERS/L8_Civic_Participation.md) |

## Incident Response Workflow

1. **Detection.** Identify potential incidents through monitoring, community reports, or audits.
2. **Assessment.** Evaluate impact, affected layers, and immediate risks.
3. **Notification.** Inform stakeholders via the Civic Oversight Interface within predetermined timeframes.
4. **Remediation.** Execute corrective actions, documenting steps and responsible parties.
5. **Review.** Conduct a public debrief, update policies, and log outcomes in the Transparency Record.

## Tools and Practices

- Use open-source security checklists and share them publicly.
- Conduct tabletop exercises with community observers.
- Publish security posture summaries alongside annual stewardship reports.
- Avoid jargon; explain trade-offs and invite questions.
