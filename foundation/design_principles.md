Layer/Theme: foundation_design_principles
Version: v5.0-open-core
Purpose: Codify civic design principles for AI OSI v5.

# Design Principles

These principles SHALL guide every layer and artefact in AI OSI v5.0-open-core. They exist to uphold dignity, transparency, and democratic oversight.

## Principles

1. **Public Benefit First** — All decisions SHALL demonstrate measurable public value.
2. **Explainable by Default** — Documentation SHALL be understandable by non-specialists.
3. **Participation over Convenience** — Processes SHOULD err on the side of inclusive deliberation rather than speed.
4. **Reparability** — Stewards SHALL plan for remediation and retroactive correction of harms.
5. **Data Minimization** — Only necessary data SHALL be collected, retained, and explained.
6. **Accessibility** — Materials SHOULD be accessible to people with varying abilities and languages.

## Applying the Principles

- Reference these principles when evaluating new tools or processes.
- Reject proposals that fail to meet public benefit or reparability requirements.
- Document any deviations in the Transparency Record with justification and mitigation steps.

Traceability

Keys: Principle_Set=DP-v5, Enforcement_Status=active
Open Civic Artefacts

- Transparency Record: Principle Review Outcomes
- Transparency Record: Deviation Log Entries

```sql
-- Copy code
SELECT artefact_id, deviation_approved
FROM transparency_registry
WHERE component = 'foundation_design_principles';
```
