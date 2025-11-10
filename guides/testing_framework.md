Layer/Theme: guide_testing_framework
Version: v5.0-open-core
Purpose: Define manual Transparency Record checks for AI OSI v5.

# Transparency Record Testing Framework

This framework SHALL equip community members to verify compliance without specialized tooling. Each check produces evidence stored in Transparency Records.

## Check 1: Mandate Integrity Review

- Confirm the civic mandate is current and publicly accessible.
- Note whether renewal dates and responsible stewards are documented.

## Check 2: Ethical Charter Alignment

- Verify prohibited uses and remediation paths remain unchanged or publicly justified.
- Ensure a recent Public Attestation Step exists for the charter.

## Check 3: Data Stewardship Audit

- Inspect dataset inventories for consent basis, retention limits, and deletion proofs.
- Record any missing notices or accessibility barriers.

## Check 4: Model Evaluation Transparency

- Review evaluation summaries for clarity on metrics, limitations, and community input.
- Confirm that decisions referencing models cite relevant Transparency Records.

## Check 5: Deployment Accountability

- Validate that rollout schedules, rollback triggers, and contact channels are up to date.
- Confirm training materials for frontline staff remain accessible.

## Check 6: Participation Responsiveness

- Compare recent community feedback with documented responses.
- Note whether participation support commitments (stipends, accessibility) were fulfilled.

Traceability

Keys: Guide=TestingFramework-v5, Cycle=semiannual
Open Civic Artefacts

- Transparency Record: Transparency Check Logs
- Transparency Record: Community Verification Reports

```sql
-- Copy code
SELECT artefact_id, check_type
FROM transparency_registry
WHERE guide = 'testing_framework';
```
