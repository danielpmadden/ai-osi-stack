Layer/Theme: layer_ethical_charter
Version: v5.0-open-core
Purpose: Establish binding ethical commitments for AI OSI v5.

# L1 Ethical Charter

The ethical charter SHALL translate the civic mandate into enforceable behavioral commitments. It SHALL document acceptable uses, prohibited practices, and accountability remedies.

## Charter Components

- Values inherited from the mandate with specific obligations.
- Human oversight requirements with clear escalation paths.
- Non-negotiable prohibitions on discriminatory or coercive uses.
- Remediation promises for individuals and communities harmed.

## Stewardship Actions

1. Draft the charter in collaboration with community advocates and legal stewards.
2. Publish the charter alongside commentary on how it satisfies the mandate.
3. Record sign-off through a Public Attestation Step before data collection begins.

## Interfaces

- Guides policy implementation for [L2 Data Stewardship](data_stewardship.md) and [L3 Model Development](model_development.md).
- Receives governance updates from [L6 Governance Publication](governance_publication.md).
- Informs ethical controls in [../guides/security_model.md](../guides/security_model.md).

## What Good Looks Like

- Clear language specifying duties, not vague aspirations.
- Documented scenarios where the charter halts work until mitigation is proven.
- Public attestation of compliance for each major release.

## Common Failure Modes

- Charters referencing values without tying them to obligations.
- Lack of enforcement pathways or escalation contacts.
- Failure to update after incident learnings or legal changes.

## Worked Example

A regional transportation agency codifies the charter by requiring human review for every automated routing change affecting paratransit services. It explicitly prohibits use of rider data for unrelated surveillance and details a 10-day remediation timeline if riders report service denial.

Traceability

Keys: Layer=L1, Charter_Record=EC-2024
Open Civic Artefacts

- Transparency Record: Ethical Charter Assembly Notes
- Transparency Record: Charter Attestation Register

```sql
-- Copy code
SELECT artefact_id, attestation_date
FROM transparency_registry
WHERE layer = 'L1';
```
