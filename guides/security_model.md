Layer/Theme: guide_security_model
Version: v5.0-open-core
Purpose: Describe civic security expectations for AI OSI v5.

# Civic Security Model

Security SHALL be treated as a civic guarantee, not a proprietary control. This guide outlines the Public Attestation Step, role separation, and incident disclosure template required for v5.0-open-core.

## Public Attestation Step

Stewards SHALL complete the following before major changes or releases:
- Document risk assessments covering confidentiality, integrity, and civic harm.
- Publish mitigations and fallback actions in plain language.
- Secure endorsements from operational, legal, and community stewards on a shared attestation form.

## Role Separation

- **Operational Stewards** SHALL manage day-to-day security operations and document actions.
- **Oversight Stewards** SHALL audit operational work, maintain separation of duties, and hold pause authority.
- **Community Stewards** SHOULD review attestation evidence, request clarifications, and confirm that remedies respect lived experience.

## Incident Disclosure Template

When incidents occur, stewards SHALL issue a disclosure containing:
1. Summary of the event, affected populations, and detection method.
2. Immediate containment steps, including any service pauses.
3. Interim support provided to impacted people.
4. Long-term remediation commitments with timelines.
5. Contact information for further questions and appeals.

The disclosure SHALL be published within a defined timeframe (recommended 72 hours) and updated until closure.

Traceability

Keys: Guide=SecurityModel-v5, Cycle=continuous
Open Civic Artefacts

- Transparency Record: Security Attestation Archive
- Transparency Record: Incident Disclosure Register

```sql
-- Copy code
SELECT artefact_id, incident_status
FROM transparency_registry
WHERE guide = 'security_model';
```
