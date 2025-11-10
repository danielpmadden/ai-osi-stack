Layer/Theme: layer_model_development
Version: v5.0-open-core
Purpose: Direct model creation under civic obligations.

# L3 Model Development

Model development SHALL adhere to the mandate, ethical charter, and data stewardship commitments. Experimentation, selection, and deployment readiness SHALL be documented for public review.

## Development Expectations

- Define the civic problem statement and target outcomes prior to experimentation.
- Document training configurations, evaluation metrics, and human oversight roles.
- Engage community reviewers to assess fairness, accessibility, and unintended effects.
- Publish evaluation summaries, including limitations and mitigations.

## Stewardship Actions

1. Conduct design reviews with stakeholders before finalizing model architecture.
2. Test models against scenarios surfaced by impacted communities.
3. Secure a Public Attestation Step confirming charter compliance before integration.

## Interfaces

- Consumes approved datasets from [L2 Data Stewardship](data_stewardship.md).
- Provides technical documentation to [L4 Instruction Control](instruction_control.md) and [../guides/testing_framework.md](../guides/testing_framework.md).
- Receives governance directives from [L6 Governance Publication](governance_publication.md).

## What Good Looks Like

- Transparent documentation showing why specific models were selected or rejected.
- Evidence of co-designed evaluation metrics with community representatives.
- Clear articulation of model limits and fallback procedures.

## Common Failure Modes

- Choosing models solely for performance without civic justification.
- Poor documentation preventing public understanding of trade-offs.
- Neglecting community-defined scenarios during testing.

## Worked Example

A civic benefits office designs an eligibility triage model. Stewards document the training data review, involve beneficiary advocates in setting fairness thresholds, and publish evaluation notebooks with plain language summaries. A Public Attestation Step confirms that manual review remains available for contested decisions.

Traceability

Keys: Layer=L3, Model_Record=MD-2024
Open Civic Artefacts

- Transparency Record: Model Review Docket
- Transparency Record: Evaluation Summary Publication

```sql
-- Copy code
SELECT artefact_id, evaluation_date
FROM transparency_registry
WHERE layer = 'L3';
```
