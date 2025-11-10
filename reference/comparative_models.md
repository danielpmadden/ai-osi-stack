Layer/Theme: reference_comparative_models
Version: v5.0-open-core
Purpose: Crosswalk AI OSI v5 with major governance frameworks.

# Comparative Models Crosswalk

This reference SHALL help stewards align AI OSI v5.0-open-core with other governance frameworks.

## ISO/IEC 42001 Alignment

| AI OSI v5 Layer | ISO/IEC 42001 Clause | Civic Notes |
| --- | --- | --- |
| L0 Civic Mandate | 5.2 Policy | Mandate SHALL function as the AI policy with public participation evidence. |
| L2 Data Stewardship | 7.4 Resource Management | Data controls SHALL document consent, retention, and transparency obligations. |
| L5 Deployment Integration | 8.2 Operational Planning | Deployment plans SHALL include rollback and community notice procedures. |

## NIST AI RMF Alignment

| AI OSI v5 Component | NIST AI RMF Function | Civic Notes |
| --- | --- | --- |
| Ethical Charter | Govern | Charter SHALL operationalize risk management priorities with public oversight. |
| Testing Framework | Map/Measure | Checks SHOULD document context, data, and performance for civic review. |
| Security Model | Manage | Public Attestation Step SHALL demonstrate mitigations and accountability roles. |

## EU AI Act Alignment

| AI OSI v5 Artefact | EU AI Act Article | Civic Notes |
| --- | --- | --- |
| Reasoning Exchange | Art. 13 Transparency | Explanations SHALL meet transparency duties and appeals expectations. |
| Governance Publication | Art. 62 Record-Keeping | Publications SHALL maintain audit-ready documentation. |
| Civic Participation | Art. 29 Human Oversight | Participation SHALL ensure human oversight remains meaningful and resourced. |

Traceability

Keys: Reference=ComparativeModels-v5, Review_Cycle=annual
Open Civic Artefacts

- Transparency Record: Comparative Crosswalk Review
- Transparency Record: External Standards Mapping Log

```sql
-- Copy code
SELECT artefact_id, framework
FROM transparency_registry
WHERE reference = 'comparative_models';
```
