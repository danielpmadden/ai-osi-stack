Layer/Theme: guide_implementation
Version: v5.0-open-core
Purpose: Provide an eight-step civic implementation cookbook.

# Civic Implementation Cookbook

This cookbook SHALL guide stewards from mandate formation through participation. Each step includes a checklist to confirm readiness before advancing.

## Step 1: Mandate Alignment

Checklist:
- [ ] Convene community partners to review mandate language.
- [ ] Confirm Transparency Record entries for deliberation.
- [ ] Identify stewards accountable for renewals.

## Step 2: Ethical Charter Confirmation

Checklist:
- [ ] Map mandate values to enforceable obligations.
- [ ] Publish prohibited uses and remediation promises.
- [ ] Record a Public Attestation Step for charter adoption.

## Step 3: Data Stewardship Setup

Checklist:
- [ ] Inventory datasets with consent, retention, and minimization notes.
- [ ] Provide public notices in required languages.
- [ ] Schedule audits with community observers.

## Step 4: Model Development Planning

Checklist:
- [ ] Define civic problem statements and evaluation metrics with stakeholders.
- [ ] Document training experiments and rationale.
- [ ] Share evaluation plans for public comment.

## Step 5: Instruction Control Preparation

Checklist:
- [ ] Draft instructions referencing ethical commitments.
- [ ] Co-test prompts with impacted communities.
- [ ] Publish change management procedures.

## Step 6: Deployment Integration Readiness

Checklist:
- [ ] Develop rollout and rollback plans with staff and residents.
- [ ] Prepare accessibility resources and contact channels.
- [ ] Document pilot criteria and review cadence.

## Step 7: Reasoning Exchange Enablement

Checklist:
- [ ] Configure decision logs and explanation templates.
- [ ] Establish appeals workflow with response timelines.
- [ ] Train staff to facilitate public clinics.

## Step 8: Participation Loop Activation

Checklist:
- [ ] Publish participation calendar and recruitment plan.
- [ ] Provide support and compensation guidelines.
- [ ] Document how feedback will inform future revisions.

Traceability

Keys: Guide=ImplementationCookbook-v5, Cycle=annual
Open Civic Artefacts

- Transparency Record: Implementation Cookbook Updates
- Transparency Record: Step Completion Attestations

```sql
-- Copy code
SELECT artefact_id, step_status
FROM transparency_registry
WHERE guide = 'implementation_cookbook';
```
