Layer/Theme: foundation_overview
Version: v5.0-open-core
Purpose: Outline the AI OSI v5 foundation and its civic commitments.

# Foundation Overview

The foundation SHALL orient every steward to the civic rationale, expected benefits, and accountability pathways of AI OSI v5.0-open-core. It frames how the nine layers interlock, provides shared vocabulary, and positions transparency as the binding practice across all work.

## Core Commitments

- The system SHALL prioritize community wellbeing over institutional expediency.
- Decisions SHOULD be documented in accessible Transparency Records.
- Public oversight SHALL remain possible without proprietary tools.

## Relationship to Layers

Each foundational document supplies context that SHALL inform layer-specific obligations:

1. `context.md` explains the societal impetus.
2. `design_principles.md` codifies civic design guardrails.
3. `glossary.md` maintains shared terminology for plain language deliberation.

Stewards SHOULD reference these before proposing changes to any layer or guide.

## Using the Foundation

- Begin every new initiative by validating alignment with the civic mandate and ethical charter.
- Reference the glossary to avoid exclusionary jargon.
- Cross-link Transparency Records whenever definitions evolve.

Traceability

Keys: Foundation_Set=v5-baseline, Stewardship_Cycle=current
Open Civic Artefacts

- Transparency Record: Foundation Overview Review Notes
- Transparency Record: Glossary Alignment Log

```sql
-- Copy code
SELECT artefact_id, check_date
FROM transparency_registry
WHERE section = 'foundation_overview';
```
