---
title: L3 Model Development
title_id: layer3-model-development
edition: civic
version: 1.0
status: draft
---

# L3 Model Development

## Purpose

Layer 3 guides the creation, adaptation, or selection of models to meet civic needs. It SHALL emphasize transparency, reproducibility, and alignment with community values.

## Development Practices

- **Open Documentation.** Maintain research logs, dataset references, and parameter settings.
- **Civic Fit Testing.** Evaluate whether models serve the mandate without reinforcing inequities.
- **Collaborative Review.** Invite interdisciplinary reviewers, including community representatives.
- **Iterative Refinement.** Document changes, rationale, and expected impacts before implementation.

## Required Records

| Record | Requirement |
| --- | --- |
| **Model Cards** | Include purpose, limitations, evaluation metrics, and civic considerations. |
| **Training Protocols** | Describe data preprocessing, training steps, and validation methods. |
| **Change Logs** | Track updates, experiments, and decisions along with OEI references. |
| **Impact Assessments** | Summaries of anticipated societal effects with mitigation plans. |

## Interfaces

- Receives ethical guidance from [L1 Ethical Charter](ethical_charter.md).
- Depends on data practices from [L2 Data Stewardship](data_stewardship.md).
- Supplies information to [L4 Instruction Control](instruction_control.md) and [../guides/testing_framework.md](../guides/testing_framework.md).

## Accountability Checklist

- [ ] Model documentation published with clear licenses.
- [ ] Evaluation metrics include civic impact indicators.
- [ ] Community reviewers participated and their feedback recorded.
- [ ] Public Attestation Step completed before moving to deployment planning.
