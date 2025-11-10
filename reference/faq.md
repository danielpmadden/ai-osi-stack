Layer/Theme: reference_faq
Version: v5.0-open-core
Purpose: Provide concise answers to common AI OSI v5 questions.

# Frequently Asked Questions

## 1. What is AI OSI v5.0-open-core?
AI OSI v5.0-open-core is a civic operating framework for responsible intelligence services. It offers public, non-commercial guidance organized into nine layers plus supporting foundation, guides, and reference materials.

## 2. Who is the intended audience?
Civic technologists, public interest advocates, institutional stewards, and community members who oversee or evaluate AI services SHALL use this repository.

## 3. How does open-core differ from open source?
Open-core prioritizes freely accessible civic knowledge while allowing optional extensions elsewhere. All essential governance content SHALL remain public without licensing fees.

## 4. How are updates governed?
Changes SHALL follow documented participation processes, including public issues, deliberation, and Transparency Record entries before merging.

## 5. What are Transparency Records?
They are public logs capturing deliberations, decisions, and follow-up actions. Every layer SHOULD reference relevant records for traceability.

## 6. How often is the civic mandate reviewed?
Stewards SHALL schedule mandate renewals at least annually or sooner if participation feedback demands adjustment.

## 7. Can private entities use this framework?
Yes, provided they honor the civic commitments, maintain transparency, and do not restrict access to derived public artefacts.

## 8. How is community input incorporated?
Participation loops in L8 Civic Participation require published calendars, inclusive formats, and documented responses to every issue raised.

## 9. What happens when harms occur?
Stewards SHALL activate incident disclosure protocols, pause operations if necessary, and follow remediation commitments documented in security and governance guides.

## 10. How are datasets approved?
L2 Data Stewardship requires consent documentation, minimization, and community oversight before any dataset is used downstream.

## 11. How can people appeal decisions?
L7 Reasoning Exchange mandates accessible appeals workflows with guaranteed human review and timely responses logged publicly.

## 12. Who maintains the ethical charter?
Designated stewards working with community advocates SHALL review and update the charter whenever laws, harms, or participation feedback warrant change.

## 13. What is the Public Attestation Step?
It is a documented confirmation that safeguards are in place before advancing to the next milestone. Attestations SHALL be published with steward endorsements.

## 14. How is accessibility ensured?
Every publication SHOULD provide multiple formats, translations, and accommodations, and participation budgets SHALL cover these needs.

## 15. How does the framework handle refusal?
Guides specify refusal logic requiring systems to decline harmful requests with clear explanations and human escalation paths.

## 16. How do I contribute improvements?
Follow the README contribution steps: open an issue, engage in deliberation, reference Transparency Records, and remain available through review.

## 17. Are metrics standardized?
Layers encourage wellbeing metrics tailored to community context. Stewards SHOULD document rationale and invite feedback before adoption.

## 18. What ensures accountability after deployment?
Governance Publication and Testing Framework guides require ongoing reporting, manual checks, and community verification cycles.

## 19. How are version changes communicated?
Reference roadmap policies mandate publishing release notes, traceability keys, and participation summaries for every version increment.

## 20. Where can I find verification tools?
Visit the `tools/` directory for the civic verification checklist, ensuring compliance with banned term scans, link validation, and metadata checks.

Traceability

Keys: Reference=FAQ-v5, Review_Cycle=quarterly
Open Civic Artefacts

- Transparency Record: FAQ Update Log
- Transparency Record: Community Inquiry Register

```sql
-- Copy code
SELECT artefact_id, question_number
FROM transparency_registry
WHERE reference = 'faq';
```
