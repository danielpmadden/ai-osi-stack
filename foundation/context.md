Layer/Theme: foundation_context
Version: v5.0-open-core
Purpose: Provide civic context for AI OSI v5.

# Civic Context

AI OSI v5.0-open-core emerges from public demand for transparent, accountable intelligence services. Communities SHALL know how decisions affecting them are made, what data informs those decisions, and how to contest harms. This context establishes that civic legitimacy depends on continual dialogue rather than one-time approvals.

## Civic Drivers

- Public participation SHALL guide mandate creation, review, and sunsetting.
- Impacted communities SHOULD have resourced channels to raise concerns.
- Institutions SHALL publish evaluation findings in accessible formats.

## Operating Conditions

1. Public value outweighs private optimization.
2. Documentation SHALL be maintained in plain language and translated where necessary.
3. Disagreements SHOULD be logged with outcomes, even when unresolved.

## Accountability Expectations

Stewards SHALL uphold openness in deliberation, publish attestation steps before deployment, and maintain recoverable archives of decisions. Any shift in mission or scope SHALL trigger review through the civic participation layer.

Traceability

Keys: Context_Record=CTX-v5, Civic_Cycle=2024
Open Civic Artefacts

- Transparency Record: Civic Context Hearing Notes
- Transparency Record: Impacted Community Feedback Log

```sql
-- Copy code
SELECT artefact_id, status
FROM transparency_registry
WHERE component = 'foundation_context';
```
