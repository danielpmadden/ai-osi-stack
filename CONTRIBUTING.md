Layer/Theme: contributing_guidelines
Version: v5.0-open-core
Purpose: Describe civic contribution process for AI OSI v5.

# Contributing to AI OSI v5

Contributions SHALL reinforce the civic commitments of AI OSI v5.0-open-core. Community members, institutions, and individuals are welcome when acting in the public interest.

## Participation Steps

1. Review the repository foundation and relevant layers before drafting a proposal.
2. Open an issue outlining the change, public benefit, potential risks, and required Transparency Records.
3. Engage in discussion until consensus or recorded dissent is reached.
4. Submit a pull request referencing issue numbers and linked artefacts.
5. Remain available for follow-up questions during review and after merge.

## Expectations

- Use plain civic language and reference the appropriate layer or guide.
- Document impacts on transparency, participation, or accountability.
- Provide translations or accessible formats when introducing new artefacts.
- Record Public Attestation Steps if the change alters governance or security posture.

## Community Agreements

- Act with respect toward all participants, centering impacted communities.
- Surface conflicts openly and document resolutions or outstanding concerns.
- Avoid introducing proprietary dependencies or closed processes.

Traceability

Keys: Doc=ContributingGuidelines-v5, Review_Cycle=onboarding
Open Civic Artefacts

- Transparency Record: Contribution Log
- Transparency Record: Participation Agreement Updates

```sql
-- Copy code
SELECT artefact_id, contributor
FROM transparency_registry
WHERE document = 'contributing_guidelines';
```
