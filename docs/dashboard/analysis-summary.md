© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# AI OSI Stack Repository Analysis — Dashboard Readiness

## 1. Layered Governance Landscape
- **Canonical Scope:** AI OSI Stack establishes seven operational layers plus optional civic mandate and policy overlays, with AEIP as transport spine.【F:docs/architecture-overview.md†L13-L37】【F:docs/ai-osi-protocol-spec.md†L14-L48】
- **Ethical Triad:** Every layer inherits mandatory dignity, epistemic integrity, and accountable stewardship constraints.【F:docs/architecture-overview.md†L39-L54】
- **Governance Risks & Controls:** Layer-to-control matrix enumerates primary risks, sentinel indicators, and required evidence, informing dashboard risk visualizations.【F:docs/governance-map.md†L13-L35】【F:docs/risk-taxonomy.md†L13-L64】
- **AEIP Crosswalk:** Cross-layer relationships map AEIP artifacts to Persona Architecture controls and Epistemology by Design checkpoints, ensuring bidirectional traceability.【F:docs/aeip-crosswalk-matrix.md†L15-L63】

## 2. Normative Clauses & Principles
- **Normative Language:** Repeated "SHALL/SHOULD/MAY" instructions bind interpretations to authorial intent, enforcing layered accountability and dignity.【F:docs/architecture-overview.md†L1-L20】【F:docs/risk-taxonomy.md†L1-L13】
- **Right-to-Opacity & Transparency Safeguards:** Update Plan lineage introduces anti-surveillance transparency doctrine and dignity constraints for publication interfaces.【F:versions/historical/update-plan-8.md†L1-L93】
- **Temporal Integrity:** AEIP handshake requires temporal seals; ledger artifacts store provenance and compliance flags for dashboard integrity indicators.【F:docs/ai-osi-protocol-spec.md†L49-L90】【F:ledger/gds.json†L1-L24】

## 3. Core Artifact Inventory
- **Governance Disclosure Statement (GDS), Decision Rationale Record (DRR), Interpretive Trace Package (ITP), Integrity Ledger Entries (ILE), Oversight Audit Memos (OAM):** Present in `/ledger` with dignity compliance flags and temporal seals; inform evidence widgets.【F:ledger/gds.json†L1-L21】【F:ledger/drr.json†L1-L18】【F:ledger/itp.json†L1-L20】
- **Civic Charter & Mandate:** `docs/charter/charter.md` anchors Layer 0 civic legitimacy, feeding civic summary panel.【F:docs/charter/charter.md†L1-L6】
- **Update Plans:** Historical plans encode contextual clauses, integration mandates (e.g., Update Plan 8 human-rights safeguards, Update Plan 11 version declaration) and future federation requirements, guiding version timeline component.【F:versions/historical/update-plan-8.md†L1-L93】【F:versions/historical/update-plan-11.txt†L1-L66】【F:versions/historical/update-plan-13.txt†L1-L6】

## 4. Cross-Layer Relationships & Dependencies
- **Persona & AEIP Alignment:** AEIP artifacts reference persona identifiers, epistemic models, and governance contexts across all layers, supporting persona-aware dashboard filters.【F:docs/aeip-artifact-schema-templates.md†L29-L113】
- **Governance Publication (Layer 7) depends on upstream evidence:** Publication controls require GDS & ILE outputs aggregated from operational layers.【F:docs/governance-map.md†L13-L35】
- **Versioning:** Ledger notices and Update Plans sequence changes, enabling version timeline linking to canonical v5 references.【F:ledger/integrity/notices/integrity-notice.txt†L12-L18】【F:versions/readme.md†L1-L120】

## 5. Visual Requirements by Layer
| Layer | Key Story | Dashboard Focus | Evidence Sources |
| --- | --- | --- | --- |
| L0 Civic Mandate | Legitimacy, charter status | Civic Charter snippet, community commitments | `docs/charter/charter.md`, Update Plans 1,4,7 references in source narratives【F:source/chapters/chapter-03-layer0-civic-mandate.tex†L4-L70】 |
| L1 Physical Substrate | Supply integrity, facility audits | Risk indicators, facility attestations | Governance map matrix, risk taxonomy, GDS sections【F:docs/governance-map.md†L16-L20】【F:docs/risk-taxonomy.md†L15-L24】 |
| L2 Data Stewardship | Consent & provenance | Consent ledger status, risk scenarios | Risk taxonomy, DRR artifacts, AEIP schema references【F:docs/risk-taxonomy.md†L25-L40】【F:docs/aeip-artifact-schema-templates.md†L114-L163】 |
| L3 Model Development | Evaluation integrity | Evaluation cadence timeline, persona controls | Risk taxonomy, Update Plan 4/7 directives, OAM placeholder【F:docs/risk-taxonomy.md†L41-L56】【F:versions/historical/update-plan-4.md†L1-L160】 |
| L4 Instruction & Control | Persona governance | Persona briefs, refusal logic coverage, AEIP intents | Risk taxonomy, Update Plan 8 rights clauses, ITP metadata【F:docs/risk-taxonomy.md†L57-L72】【F:versions/historical/update-plan-8.md†L1-L93】 |
| L5 Reasoning Exchange | AEIP handshake health | AEIP log viewer, packet replay detection | AEIP protocol spec, ILE artifacts【F:docs/ai-osi-protocol-spec.md†L49-L90】【F:ledger/ile.json†L1-L200】 |
| L6 Deployment & Integration | Runtime assurance | Change manifests, incident reports | Risk taxonomy, TRR/OAM placeholders, ledger metadata【F:docs/risk-taxonomy.md†L73-L88】 |
| L7 Governance Publication | Transparency cadence | Disclosure schedule, public releases, maturity scores | Governance map, GDS ledger, Update Plan 9 alignment |【F:docs/governance-map.md†L31-L35】【F:versions/historical/update-plan-9.md†L1-L120】
| L8 Policy Overlay | Civic partnerships | Federation readiness, partnership registry | Update Plan 13, AEIP crosswalk, governance ledger notices【F:versions/historical/update-plan-13.txt†L1-L6】【F:docs/aeip-crosswalk-matrix.md†L15-L63】 |
| AEIP Spine | Handshake lifecycle | Log viewer timeline, AEIP compliance flags | `docs/aeip-spec-v1-3.md`, AEIP schemas |【F:docs/aeip-spec-v1-3.md†L1-L200】
| Governance Artifacts | Evidence completeness | Artifact gallery, integrity badge | `/ledger` JSON, `docs/aeip-artifact-schema-templates.md` |

## 6. Potential Data Models
- **Layer:** id, name, purpose, obligations, risks, primary artifacts, stewardship personas, maturity score, contextual transparency posture.
- **Artifact:** id, type (ITP, DRR, GDS, ILE, Charter, Clarity Package, Model Card, Solomon Brief, Integrity Ledger, AEIP Receipt), layer linkage, hash, temporalSeal, dignityCompliance.
- **Actor:** personaId, role (Custodian, Auditor, Civic Partner), obligations, contact window, AEIP credentials reference.
- **Risk:** riskId, layer, description, sentinelIndicators, controls, residualRiskScore, relatedArtifacts.
- **Evidence:** evidenceId, artifactRef, verificationStatus, sourcePath, lastUpdated, reviewerPersona.
- **Standard Alignment:** standardId, externalFramework (ISO/IEC 42001, NIST AI RMF, EU AI Act), clauses, mappedLayers, evidencePointers.

## 7. Key Cross-Layer Narratives for Dashboard Storytelling
1. **Integrity Chain:** AEIP handshake events (Layer 5) produce ILE artifacts that anchor Layer 6 assurance reports and Layer 7 disclosure cadence.【F:docs/ai-osi-protocol-spec.md†L49-L90】
2. **Persona Stewardship:** Persona Architecture controls govern Layer 3–5 operations, with dignity compliance flags gating artifact publishing.【F:docs/aeip-crosswalk-matrix.md†L15-L63】
3. **Rights Safeguards:** Update Plan 8’s “Transparency ≠ Surveillance” clause modulates Layer 7 publication, requiring Right-to-Opacity toggles in dashboard views.【F:versions/historical/update-plan-8.md†L1-L93】
4. **Version Governance:** Update Plan 11 declares v5 canonical integration, informing top-bar canonical version metadata and version timeline component.【F:versions/historical/update-plan-11.txt†L1-L66】

## 8. Visual & Interaction Implications
- **Contextual Transparency:** Provide layered summaries with privacy toggles for sensitive fields to honor Right-to-Opacity mandates.【F:versions/historical/update-plan-8.md†L1-L93】
- **Dignity as Constraint:** Display refusal logic and persona safeguard status prominently within Layer 4 cards; integrate dignity compliance badges using ledger data.【F:ledger/itp.json†L1-L20】
- **Temporal Accountability:** Embed timeline controls showing AEIP seals and Update Plan milestones across layers.【F:ledger/gds.json†L1-L24】【F:ledger/drr.json†L1-L18】

