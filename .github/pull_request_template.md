Layer/Theme: pr_template
Version: v5.0-open-core
Purpose: Guide civic pull request submissions.

# Pull Request Template

## Summary
- Describe the public benefit and layers or guides affected.
- Link relevant Transparency Records.

## Testing
- Detail verification steps performed and who witnessed them.

## Participation
- Note community feedback gathered or scheduled follow-up sessions.

Traceability

Keys: Doc=PRTemplate-v5, Review_Cycle=on_change
Open Civic Artefacts

- Transparency Record: Contribution Workflow Log
- Transparency Record: PR Template Review Notes

```sql
-- Copy code
SELECT artefact_id, template_version
FROM transparency_registry
WHERE document = 'pr_template';
```
