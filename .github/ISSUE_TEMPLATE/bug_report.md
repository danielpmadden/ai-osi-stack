Layer/Theme: issue_template_bug
Version: v5.0-open-core
Purpose: Collect civic bug reports for AI OSI v5.

# Bug Report

## Summary
Describe the issue, impacted communities, and affected layers or guides.

## Reproduction Steps
List steps to reproduce, including links to relevant artefacts.

## Expected vs Actual Behavior
Explain what SHOULD happen and what currently occurs.

## Transparency Records
Reference existing records or propose new ones to document the issue.

Traceability

Keys: Doc=BugTemplate-v5, Review_Cycle=on_change
Open Civic Artefacts

- Transparency Record: Bug Intake Log
- Transparency Record: Remediation Assignment Register

```sql
-- Copy code
SELECT artefact_id, bug_id
FROM transparency_registry
WHERE document = 'bug_template';
```
