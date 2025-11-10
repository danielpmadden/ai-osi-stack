Layer/Theme: reference_roadmap
Version: v5.0-open-core
Purpose: Define roadmap milestones and versioning policy for AI OSI v5.

# Roadmap and Versioning Policy

The roadmap SHALL guide progression toward general availability (GA) and future releases while honoring civic commitments.

## Criteria for v5 GA

- **Transparency**: All nine layers SHALL include current Traceability keys and linked Transparency Records.
- **Participation**: Civic participation metrics SHOULD show diverse engagement with documented responses.
- **Verification**: The civic verification routine SHALL run without critical findings across banned terms, links, metadata, and layer counts.
- **Attestations**: Public Attestation Steps SHALL cover mandate renewal, charter validation, data stewardship audits, and deployment readiness.
- **Accessibility**: Core artefacts SHALL be available in at least two languages or formats meeting accessibility standards.

## Release Cadence

- Minor updates (v5.x) SHALL bundle incremental improvements validated through participation loops.
- Patch updates (v5.x.y) SHALL address urgent fixes such as link corrections or incident disclosures.
- Major updates (v6.0 or beyond) SHALL undergo public consultation and new GA criteria approval before work begins.

## Versioning Policy

- Version numbers SHALL appear in metadata headers across all markdown files.
- Release notes SHALL summarize changes, cite Transparency Records, and outline participation outcomes.
- Deprecated content SHOULD remain accessible with clear sunset dates and replacement references.

Traceability

Keys: Reference=Roadmap-v5, Review_Cycle=biannual
Open Civic Artefacts

- Transparency Record: Roadmap Review Minutes
- Transparency Record: Version Policy Attestations

```sql
-- Copy code
SELECT artefact_id, milestone
FROM transparency_registry
WHERE reference = 'roadmap';
```
