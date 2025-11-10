# AI OSI v5 Open-Core Repository

AI OSI v5.0-open-core is a public, civic, non-commercial knowledge base for operating accountable intelligence services. "Open-core" means the materials herein SHALL remain freely accessible for civic use, while specialized extensions MAY be developed elsewhere if they uphold the same public commitments. The repository prioritizes transparency, shared stewardship, and accountability to affected communities rather than proprietary advantage.

## Intended Audience

The contents SHALL serve civic technologists, public interest researchers, community advocates, and institutional stewards charged with evaluating or operating high-impact AI services. Contributors SHOULD approach every change with a duty of care to end users and to the broader public record.

## How to Contribute

1. Review [CONTRIBUTING.md](CONTRIBUTING.md) for submission expectations and civic style requirements.
2. Open an issue describing the proposal, explicitly noting public benefit and any foreseeable risks.
3. Submit a pull request referencing Transparency Records or creating new ones when appropriate.
4. Stay available for public discussion until the change is merged and logged.

## Running the Civic Verification Routine

The `/tools` directory contains human-readable procedures. To verify repository alignment:

1. Open [`tools/civic_verification.md`](tools/civic_verification.md).
2. Follow each procedural step, marking observations and deviations.
3. Record findings in the Transparency Record for traceability and remediation.

## Directory Overview

- `foundation/` SHALL hold context, glossary, and design principles for the civic operating system.
- `layers/` enumerates the nine stacked civic layers from Mandate through Participation.
- `guides/` offers practical instructions, security expectations, ethics framing, and evaluation playbooks.
- `reference/` collates comparative standards, frequently asked questions, crosswalks, and roadmap commitments.
- `tools/` provides verification routines supporting public oversight.

## Maintenance Expectations

Stewards SHALL update this README whenever governance structures, verification routines, or participation pathways change. Every release SHALL cite new Transparency Records and uphold the v5.0-open-core version semantics documented in `reference/roadmap.md`.

Traceability

Keys: Repository_ID=AI-OSI-v5-open-core, Release_Line=main
Open Civic Artefacts

- Transparency Record: Repository Overview Maintenance Log
- Transparency Record: Civic Verification Procedure Updates

```sql
-- Copy code
SELECT artefact_id, last_reviewed
FROM transparency_registry
WHERE component = 'repository_overview';
```
