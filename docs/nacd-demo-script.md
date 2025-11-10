© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
# AI OSI Stack Dashboard Demo Script for NACD Cyber Risk Advisor

## 1. Demo Script (15-20 minutes)
*Estimated word count: 1,420 words*

### Opening Frame (30 seconds) — ~95 words
[SHOW TITLE SLIDE]
"Good afternoon, and thank you for making time. Boards are inheriting accountability for AI outcomes faster than governance tools are evolving. Right now, most directors are offered model metrics and risk heat maps, but not the infrastructure to demonstrate fiduciary oversight. I am not pitching a product. I built a reference architecture that aligns AI operations with board governance. What you will see is a production-quality dashboard wired to schemas and controls, using static exemplars. I am here to validate the design and confirm whether it closes the accountability gap you are experiencing."

### Component-by-Component Walkthrough (6 minutes)

#### a) Navigation & Layer Structure — ~180 words
[CLICK THROUGH] [SHOW COMPONENT]
- **What you show:** Highlight the 9-layer sidebar, open the shortcuts panel, and demonstrate keyboard navigation.
- **What you say:** "The stack starts at Layer 0 with civic mandate and progresses to Layer 8 civic participation. Each layer has direct shortcuts to artifacts, policies, and logs. Accessibility features—skip links, ARIA labels—matter because auditors, not developers, will use this."
- **Board value:** "Directors see the full chain of accountability without traversing engineering backlogs. The nine layers map to the lifecycle responsibilities you already hold."
- **Anticipated question:** "Is nine layers too complex for a board dashboard?" **Response:** "We surfaced all layers, but role-based views can collapse them. The structure is fixed so auditors can certify completeness without wondering what was hidden."

#### b) LayerCard with Triple Register — ~170 words
[CLICK THROUGH] [SHOW COMPONENT]
- **What you show:** Open a LayerCard and switch between Narrative, Normative, and Plain tabs.
- **What you say:** "Every layer keeps a triple register. Narrative is the story executives tell. Normative is the policy text cited to legal standards. Plain is the plain-language summary for public transparency. Boards can compare these on the same screen and catch gaps early."
- **Board value:** "It operationalizes your duty of candor. You can test whether management’s narrative matches formal obligations and what stakeholders will read."
- **Anticipated question:** "Who maintains all three views?" **Response:** "The architecture expects stewardship assignments per tab. Narrative from product, normative from legal/risk, plain from civic communications. The dashboard enforces schema completeness so missing tabs surface as governance exceptions."

#### c) Governance Facets — ~170 words
[SHOW COMPONENT]
- **What you show:** Scroll to the risk and safeguard summaries, toggle filters.
- **What you say:** "Facets summarize quantified risk, declared safeguards, and accountable owners. Filters let directors drill into unresolved items."
- **Board value:** "It transforms risk reporting into an auditable ledger. You see not just residual risk scores, but the named control owner and linked evidence."
- **Anticipated question:** "Where do these risk scores originate?" **Response:** "Today they are schema-validated entries. In production, they bind to your GRC system via API. The model ensures you can trace every score back to a documented assessment."

#### d) ArtifactGallery — ~170 words
[SHOW COMPONENT]
- **What you show:** Open ArtifactGallery, point to artifact counts, schema paths, and provenance placeholders.
- **What you say:** "Every artifact—impact assessment, DPIA, training dataset—has a schema path and provenance hash. Counts show what’s expected, what’s present, and which items are overdue."
- **Board value:** "Directors can confirm completeness before approving spend or go-live. This is your audit trail."
- **Anticipated question:** "What if artifacts live in SharePoint or a DMS?" **Response:** "The gallery ingests metadata only. Links point to your existing repositories, keeping source systems intact while giving you oversight."

#### e) VersionTimeline — ~150 words
[SHOW COMPONENT]
- **What you show:** Step through the chronological timeline with color-coded changes.
- **What you say:** "Every control change, risk reassessment, or model update lands on a timeline. Color coding flags policy changes versus technical patches."
- **Board value:** "You can answer ‘what changed since last quarter’ in seconds, supporting SEC disclosure expectations about material cyber events."
- **Anticipated question:** "How far back does the history go?" **Response:** "The schema can ingest legacy data if you have it, and from first deployment forward the ledger keeps a tamper-evident sequence."

#### f) IntegrityBadge — ~140 words
[SHOW COMPONENT]
- **What you show:** Hover over the integrity badge displaying DOI, checksums, and review dates.
- **What you say:** "Every layer carries an integrity badge. It references a DOI, the latest checksum, the review date, and an integrity notice."
- **Board value:** "You get instant clarity on whether evidence is current and tamper-evident—critical for attestations."
- **Anticipated question:** "Is the DOI live or internal?" **Response:** "Today it’s deterministic hashing. The next step is binding to your PKI or notarization service so the DOI is verifiable externally."

#### g) AEIPLogViewer — ~170 words
[SHOW COMPONENT]
- **What you show:** Open the AEIP log viewer, scroll through receipt entries with countersignatures.
- **What you say:** "This is the AEIP—Accountable Event Interface Protocol—log. Every governance action produces a receipt countersigned by both system and human steward."
- **Board value:** "It removes ambiguity about who authorized what. Directors can trace consent and oversight down to the exact change."
- **Anticipated question:** "Are these signatures enforceable?" **Response:** "In the reference build they’re placeholders. Integrating with your IAM or hardware security modules would make them binding signatures."

#### h) GlossaryDrawer — ~140 words
[SHOW COMPONENT]
- **What you show:** Open the glossary drawer, search for ‘civic mandate.’
- **What you say:** "To keep everyone aligned, the glossary provides civic terminology definitions with jurisdictional notes."
- **Board value:** "It standardizes language across legal, technical, and civic audiences, reducing misunderstanding in board minutes."
- **Anticipated question:** "Who curates the glossary?" **Response:** "The governance office owns it. The dashboard flags stale definitions and supports versioning so updates are auditable."

### Complete Scenario Walkthrough (3 minutes) — ~430 words
[CLICK THROUGH]
"Let me show you what end-to-end accountability looks like."

1. **Layer 0 – Authorization** [SHOW L0 LayerCard & IntegrityBadge]
   - "Layer 0 documents who authorized this system—the City Services Committee—and under which civic mandate. The LayerCard’s normative tab cites the municipal AI ordinance; the IntegrityBadge shows the authorization DOI and review date. ArtifactGallery reveals the signed resolution and community impact assessment receipts."

2. **Layer 2 – Data Governance** [SHOW Governance Facets & ArtifactGallery]
   - "On Layer 2, governance facets show data collection rights, lawful basis, and privacy safeguards. The ArtifactGallery lists DPIAs, consent records, and schema paths to the rights catalog. The triple register highlights the plain-language explanation—useful for public transparency reports."

3. **Layer 3 – Model Provenance** [SHOW ArtifactGallery filtered + VersionTimeline]
   - "Layer 3 captures model lineage. The gallery includes dataset provenance statements, training logs, and third-party supplier attestations. VersionTimeline shows when the model was retrained, what data sources changed, and which review board approved it."

4. **Layer 4 – Control Policies** [SHOW Governance Facets + AEIPLogViewer]
   - "Layer 4 lists behavioral constraints—guardrails, escalation playbooks, bias thresholds. Governance facets note unresolved policy exceptions. The AEIP log shows a countersigned record where the Chief Risk Officer approved new response limits after an incident review."

5. **Layer 6 – Deployment Oversight** [SHOW VersionTimeline + IntegrityBadge]
   - "Layer 6 covers deployment approvals. The timeline indicates a green-coded ‘deployment freeze lifted’ event with board concurrence. IntegrityBadge tells us the last deployment check was reviewed 14 days ago, still inside the required window."

6. **Layer 8 – Civic Feedback Loop** [SHOW GlossaryDrawer + LayerCard Plain Tab]
   - "Layer 8 aggregates civic feedback. The LayerCard plain tab includes excerpts from community listening sessions. The glossary ensures terms like ‘algorithmic redress’ are uniform. AEIP receipts show how feedback triggered a policy review back at Layer 4, closing the loop."

"In four clicks we answered: who authorized the system, which rights are protected, how the model was trained, what policies bind behavior, who approved deployment, and how civic feedback feeds governance. That is the audit trail directors need for fiduciary duty and regulatory confidence."

### Standards Alignment Moment (1 minute) — ~210 words
[SHOW STANDARDS OVERLAY]
"The architecture is deliberately mapped to emerging obligations."
- "ISO 42001: The dashboard’s nine layers align with the management system clauses—context, leadership, planning, support, operation, performance evaluation, improvement—so auditors can trace compliance evidence per clause."
- "NIST AI RMF: Each component is tagged to Govern, Map, Measure, Manage. For example, Layer 0 artifacts sit under Govern; Layer 3 provenance feeds Map; the risk facets align to Measure; AEIP logs represent Manage."
- "EU AI Act Annex IV: The ArtifactGallery schema matches required documentation—intended purpose, design specs, data governance, technical documentation, post-market monitoring. Directors can demonstrate readiness for Article 52 disclosures."
- "SEC cyber disclosure: VersionTimeline and IntegrityBadge provide the audit trail regulators expect for material incident reporting and board oversight narratives."
"When auditors or regulators ask for documentation, they click the same evidence trail."

### Transparency About Limitations (1 minute) — ~210 words
[SHOW TODO OVERLAY]
"Transparency is part of the governance model."
- "Current data is static JSON/JSON-LD exemplars. AEIP receipts, provenance modals, and ledger playback are placeholders until wired to operational systems."
- "TODO banners mark translation fidelity checks, tooltip content, and accessibility audits scheduled."
- "Cryptography today uses deterministic hashing. Production would integrate with your PKI or distributed ledger for non-repudiation."
- "To move from reference implementation to production we need: system integrations with IAM, GRC, and CI/CD; attestation workflows; and change-management alignment with your governance cadence."
"This proves the architecture works. What it needs are real systems to govern."

### The Ask & Next Steps (30 seconds) — ~115 words
[SHOW NEXT STEPS]
1. **Minimum ask:** "I’d value candid feedback on whether this addresses the governance gap you are seeing."  
2. **Medium ask:** "If it resonates, an introduction to NACD members grappling with AI oversight would help validate adoption paths."  
3. **Maximum ask:** "If you see promise, I’m seeking partners to pilot this with two to three organizations to test live integrations."  
"I will follow up with the architecture deck, a standards crosswalk, and the repository link so your team can review it asynchronously."

## 2. Anticipated Q&A
*Estimated word count: 430 words*

1. **How is this different from an MLOps platform or model monitoring tool?**  
   "Those tools manage model performance. This stack governs accountability layers—from civic mandate to civic participation. The dashboard sits above model ops, ingesting their data as artifacts but adding board-facing schema validation, integrity badges, and AEIP receipts."

2. **What’s the implementation lift for our organization?**  
   "Initial lift is integration with identity, document management, and risk systems. The front end is production-ready React with i18n and accessibility. Implementation becomes connecting APIs, defining stewardship roles, and populating artifacts."

3. **Who else is using this?**  
   "It’s a reference implementation to demonstrate architecture. I’m lining up pilot partners. The components mirror requirements we hear from municipal coalitions, financial services, and higher education governance offices."

4. **What happens when regulations change?**  
   "The schema-driven design lets us update requirements centrally. Layer definitions and artifact templates version like code. Directors see change impact immediately via VersionTimeline and governance facets."

5. **How does this integrate with existing compliance tools?**  
   "ArtifactGallery stores metadata only and links to your existing compliance repositories. Governance facets can pull control status from ServiceNow, Archer, or your preferred GRC system via API."

6. **Why would we adopt something built by one person?**  
   "The value is the architecture blueprint. The repository is open for review, and the implementation references industry standards. A pilot would include knowledge transfer and documentation so your internal team or partner can take ownership."

7. **What about security of the evidence?**  
   "The reference build shows integrity badges and hashing. Production requires integrating with your PKI, access controls, and storage policies. The design isolates sensitive content to your systems; the dashboard presents metadata."

## 3. Strategic Questions to Ask Them
*Estimated word count: 190 words*

"Before I continue, I’d value your perspective on..."
1. "Where do you see the board’s fiduciary duty most exposed in AI oversight today?"
2. "Which governance artifacts are hardest for directors to access or trust right now?"
3. "How do your auditors currently validate AI risk controls, and where do they get stuck?"
4. "What integration points—GRC, IAM, model registries—are non-negotiable for a pilot?"
5. "What cultural or change-management barriers would slow adoption in your member organizations?"
6. "Which upcoming regulatory milestones are creating urgency for your directors?"
7. "If you were to sponsor a pilot, what success metrics would the board need to see in 90 days?"

## 4. One-Page Leave-Behind (Markdown Outline)
*Estimated word count: 260 words*

```markdown
# AI OSI Stack Governance Dashboard

## Problem Statement
- Boards are accountable for AI impacts without an auditable system to evidence oversight.
- Regulatory regimes (ISO 42001, NIST AI RMF, EU AI Act, SEC disclosures) demand traceable documentation across the AI lifecycle.
- Current tools focus on model performance, leaving directors with fragmented, non-fiduciary reports.

## Solution Architecture
- Nine-layer AI OSI Stack from Civic Mandate (L0) to Civic Participation (L8) with role-based navigation.
- Triple Register LayerCards (narrative / normative / plain) enforcing schema completeness and accountability assignments.
- AEIP protocol logs for countersigned governance receipts, IntegrityBadges for DOI + checksum assurance, and ArtifactGallery metadata linking to existing repositories.
- Production-ready React 18 + TypeScript front end with accessibility, i18n, and Zod-validated schemas.

## Current Status & What’s Needed
- Reference implementation with static JSON/JSON-LD exemplars, Storybook catalog, and standards crosswalks.
- TODO: Integrate AEIP API, provenance modals, ledger playback, translation QA, and tooltips with operational systems.
- Path to production: connect IAM/GRC/document systems, layer stewardship assignments, enable PKI-backed integrity services, and run joint change-management.

## Standards Alignment
- ISO 42001 clauses mapped per layer; NIST AI RMF functions tagged (Govern, Map, Measure, Manage).
- EU AI Act Annex IV documentation schema embedded; SEC cyber disclosure audit trail supported via VersionTimeline and IntegrityBadge.

## Contact & Repository
- Architect: [Your Name], Solo Maintainer & Civic Tech Architect.
- Contact: [email@example.com] | +1-XXX-XXX-XXXX
- Repository: https://github.com/your-org/ai-osi-stack
```
