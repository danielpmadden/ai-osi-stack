Layer/Theme: issue_template_feature
Version: v5.0-open-core
Purpose: Gather civic feature proposals for AI OSI v5.

# Feature Request

## Summary
Outline the proposed change, public benefit, and impacted layers or guides.

## Motivation
Describe why the change is needed and who requested it.

## Proposed Approach
Share initial ideas, required Transparency Records, and attestation needs.

## Participation Plan
List engagement steps with affected communities and how feedback will be recorded.

Traceability

Keys: Doc=FeatureTemplate-v5, Review_Cycle=on_change
Open Civic Artefacts

- Transparency Record: Feature Intake Log
- Transparency Record: Participation Planning Register

```sql
-- Copy code
SELECT artefact_id, feature_id
FROM transparency_registry
WHERE document = 'feature_template';
```
