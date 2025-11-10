Layer/Theme: foundation_glossary
Version: v5.0-open-core
Purpose: Maintain shared civic terminology for AI OSI v5.

# Glossary

This glossary SHALL ensure plain language definitions for recurring civic terms.

## Terms

- **Transparency Record**: A publicly accessible log of deliberations, decisions, and follow-up actions.
- **Public Attestation Step**: A formal statement confirming compliance with required safeguards before advancing.
- **Open Civic Artefact**: Any document, dataset, or tool released for community oversight under the open-core commitment.
- **Steward**: A person or group responsible for maintaining a layer, guide, or artefact.
- **Participation Loop**: The recurring process of inviting, recording, and responding to public input.

## Maintenance Guidance

Stewards SHOULD update definitions when new civic concepts emerge, ensuring prior records remain interpretable. Any retired term SHALL retain its definition with a sunset note to preserve auditability.

Traceability

Keys: Glossary_Version=v5-open-core, Editorial_Cycle=quarterly
Open Civic Artefacts

- Transparency Record: Glossary Change Log
- Transparency Record: Terminology Review Sessions

```sql
-- Copy code
SELECT artefact_id, revision_note
FROM transparency_registry
WHERE component = 'foundation_glossary';
```
