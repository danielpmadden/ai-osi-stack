Layer/Theme: layer_civic_mandate
Version: v5.0-open-core
Purpose: Define the public mandate that anchors AI OSI v5.

# L0 Civic Mandate

The civic mandate SHALL articulate the community need, intended benefits, and red lines for the intelligence service. Renewal SHALL occur through open deliberation with affected parties.

## Required Elements

- A mission statement written in plain language.
- Documented participation from impacted communities.
- Authorities and limits grounded in law, policy, or community agreements.
- Wellbeing-oriented success measures with review cadence.

## Stewardship Actions

1. Convene an open forum with published agenda and accessible materials.
2. Record deliberation outcomes and opposing views in the Transparency Record.
3. Issue a Public Attestation Step confirming readiness to proceed to the ethical charter.

## Interfaces

- Feeds governing intent to [L1 Ethical Charter](ethical_charter.md) and [L2 Data Stewardship](data_stewardship.md).
- Receives feedback cycles from [L8 Civic Participation](civic_participation.md).
- Informs mandate-specific tasks in [../guides/implementation_guide.md](../guides/implementation_guide.md).

## What Good Looks Like

- Communities recognize their priorities in the mandate language.
- Review dates are published with responsible stewards named.
- Transparency Records show consensus and dissent side by side.

## Common Failure Modes

- Mandates written without direct input from impacted communities.
- Unclear authority boundaries leading to unchecked expansion.
- Missing renewal timelines or undocumented review outcomes.

## Worked Example

A municipal data office drafts a civic intelligence service. Stewards run neighborhood assemblies, translate materials, and publish deliberation notes. The resulting mandate states the service SHALL support housing stability metrics, prohibits surveillance uses, and sets a six-month review schedule aligned with council hearings.

Traceability

Keys: Layer=L0, Mandate_Record=CM-2024
Open Civic Artefacts

- Transparency Record: Civic Mandate Forum Minutes
- Transparency Record: Mandate Renewal Attestation

```sql
-- Copy code
SELECT artefact_id, renewal_date
FROM transparency_registry
WHERE layer = 'L0';
```
