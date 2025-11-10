Layer/Theme: layer_governance_publication
Version: v5.0-open-core
Purpose: Publish governance decisions and oversight artefacts.

# L6 Governance Publication

Governance publication SHALL ensure that all oversight decisions, audits, and community findings remain accessible. It SHALL maintain living records that demonstrate compliance and invite scrutiny.

## Publication Responsibilities

- Maintain a schedule for releasing meeting minutes, audit summaries, and attestation steps.
- Provide translation and accessibility accommodations for all published materials.
- Cross-reference artefacts with layers and guides for straightforward navigation.
- Document dissenting opinions alongside majority decisions.

## Stewardship Actions

1. Consolidate artefacts into a public index updated after every governance session.
2. Verify that each publication links to relevant Transparency Records and contact channels.
3. Issue a Public Attestation Step confirming completeness of the release package.

## Interfaces

- Receives operational updates from [L5 Deployment Integration](deployment_integration.md) and [L7 Reasoning Exchange](reasoning_exchange.md).
- Supplies artefact references to [../reference/crosswalk_index.md](../reference/crosswalk_index.md) and [../reference/roadmap.md](../reference/roadmap.md).
- Informs civic feedback loops documented in [L8 Civic Participation](civic_participation.md).

## What Good Looks Like

- Timely publication of decisions with contextual summaries and supporting data.
- Clear indexing that helps residents trace a topic across layers.
- Inclusion of remediation status for previously identified issues.

## Common Failure Modes

- Publishing partial updates without cross-links.
- Allowing accessibility gaps that exclude impacted communities.
- Omitting dissent or remediation progress from public records.

## Worked Example

A national oversight body maintains a public portal where every meeting packet, vote tally, and attestation is published within five working days. Artefacts reference relevant layers and include remediation trackers so residents can monitor follow-up actions.

Traceability

Keys: Layer=L6, Governance_Record=GP-2024
Open Civic Artefacts

- Transparency Record: Governance Publication Log
- Transparency Record: Oversight Attestation Archive

```sql
-- Copy code
SELECT artefact_id, publication_date
FROM transparency_registry
WHERE layer = 'L6';
```
