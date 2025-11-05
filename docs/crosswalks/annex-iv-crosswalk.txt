Annex IV Crosswalk — AI OSI v4.3 Formal Alignment Draft

File: /docs/Annex IV Crosswalk.md
Purpose: Show direct evidence mapping between EU AI Act Annex IV technical documentation requirements and AI OSI Stack artifacts.

AI OSI – EU AI Act Annex IV Crosswalk (Draft v1.0)

“Accountability must be reconstructable.”

Annex IV Requirement	AI OSI / AEIP Artifact	Layer Reference	Notes
(a) System Overview	Clarity Package, Model Card, Reasoning Map	L3–L5	Matches AI system description and functionality
(b) Design & Development Process	Model Ledger, Data Lineage Registry	L2–L3	Tracks datasets, training context, and design rationale
(c) Risk Management	Risk Ledger, Decision Insurance Logs	L6	Compatible with ISO 23894 & NIST RMF “Manage” function
(d) Data Governance	Data Stewardship Record, CCMs, Provenance Registry	L2	GDPR Art. 5–6 principles; proportionality tests
(e) Technical Documentation	AEIP Frame, System Spec, Self-Audit Form	L5–L7	JSON-LD schema ensures traceability
(f) Logging & Record-Keeping	Instruction Ledger, AEIP Logs, SLGI	L4–L6	Immutable, cryptographically sealed
(g) Transparency	Governance Publication, Appendix N – HR Safeguards	L7	Satisfies arts 13–15 AIA transparency obligations
(h) Human Oversight	Instruction & Control Plan, Human Override Record	L4	Enforces human-in-the-loop boundaries
(i) Accuracy, Robustness, Cybersecurity	Validation Report, Model Assurance Ledger	L3–L6	Map to ISO 27001 & ENISA AI security
(j) Post-Market Monitoring	Audit Loop, Governance Publication Log	L7	Equivalent to post-market surveillance system

✅ Outcome: Every Annex IV obligation has a direct AI OSI artifact capable of evidentiary export.

⚖️ 2. EU Charter & GDPR Consistency Matrix

File: /docs/EU Rights Consistency Matrix.md
Purpose: Demonstrate how the AI OSI normative clauses and AEIP schema uphold EU fundamental rights and GDPR principles.

EU Charter / GDPR → AI OSI Mapping

“Transparency bounded by consent.”

Right / Principle	Source	AI OSI Clause / Mechanism	Layer / Artifact
Privacy & Data Protection	Charter Arts 7–8 / GDPR Art 5(1)(a–c)	Right-to-Opacity Clause 3.1; AEIP privacy.metadata fields; Necessity & Proportionality checklist	L2, L7
Freedom of Expression & Information	Charter Art 11	Preface Amendment (“no suppression of expression”), Dual-Transparency Rule 3.2	L7–L8
Non-Discrimination	Charter Art 21	Bias Metrics Registry, Decision Insurance logs, Civic Participation feedback	L2, L8
Fair Trial / Effective Remedy	Charter Art 47	Governance Publication + Appeal Trail; Citizen Ombuds Channels	L7–L8
Consent & Autonomy	GDPR Art 6–7	Renewable Consent Requirement (L0); Opt-Out Channels (L8)	L0, L8
Accountability & Lawfulness	GDPR Art 5(2)	Self-Audit Checklist; Custodial Integrity Notice	L7
Data Minimization & Storage Limits	GDPR Art 5(1)(c–e)	Redaction Fields; Retention Policies in AEIP	L2
Purpose Limitation	GDPR Art 5(1)(b)	Contextual Consent Manifests (CCMs)	L2
Data Portability / Access	GDPR Art 20	Citizen Access Interface (L8)	L8

✅ Outcome: Stack satisfies all GDPR core principles and aligns with the Charter’s privacy, expression, equality, and remedy articles.

🔒 3. Security Controls Bridge

File: /docs/Security Controls Bridge.md
Purpose: Map AI OSI technical and procedural controls to ISO/IEC 27001 Annex A and ENISA AI Cybersecurity domains.

AI OSI Security Control Mapping (v1.0)
Security Domain	ISO 27001 / ENISA Reference	AI OSI Control / Artifact	Layer
Identity & Access Management	A.5 Access Control	Operator Credential Ledger + Role Manifest	L4–L6
Supply Chain Integrity	ENISA SCM.1 / A.15	Provenance Registry + Vendor Attestations	L2
Logging & Monitoring	A.12 / ENISA LOG.1	Immutable AEIP Logs + Event Hashes	L5–L7
Vulnerability Management	A.12.6 / ENISA VM.1	Incident Registry + Patch Notices	L6
Cryptographic Controls	A.10 / ENISA CRY.1	AEIP Signatures + Reasoning Attestations	L5
Operational Continuity	A.17	Rollback Protocols + Recovery Artifacts	L6
Human Security	A.7 / ENISA HUM.1	Operator Training Ledger + Human Override Log	L4
Physical Security	A.11	Compute Substrate Access Registry	L1
Secure Development Lifecycle	A.14 / ENISA SDLC.1	Development Pipeline Ledger + Peer Review Records	L3
AI-Specific Model Integrity	ENISA AI.IN 1	Model Assurance Ledger + Tamper Seals	L3–L5

✅ Outcome: AI OSI controls provide full coverage of ENISA AI security domains and ISO 27001 Annex A.

🪶 4. Liability Bridge Note

File: /docs/Liability Bridge Note.md
Purpose: Explain how AI OSI evidence artifacts satisfy disclosure and burden-of-proof duties in EU AI Liability Directive / Product Liability Directive.

“Proof must be reconstructable by design.”

Directive Clause	Required Evidence	AI OSI Artifact	Result
Duty to disclose training and testing data	Design docs, logs	Data Stewardship Registry, Provenance Logs	Meets
Presumption of defect — evidence of fault	System logs, audit trail	AEIP Logs, Instruction Ledger	Meets
Burden of proof reversal	Operator accountability records	Self-Audit Checklist + Governance Publication	Meets
Preservation of evidence	Secure logging, non-tamper	AEIP immutable hashes	Meets
Risk mitigation evidence	Documentation of risk controls	Risk Ledger + Decision Insurance	Meets

✅ Outcome: AI OSI produces evidentiary artifacts sufficient for EU liability compliance and legal rebuttal.