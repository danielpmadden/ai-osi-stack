<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# AI OSI Stack v5 — Repository-Wide Integrity Audit (v5.0)

## Summary of Findings

| Category | Severity | Key Issues |
| --- | --- | --- |
| Authorship & Provenance | Critical | Canonical authorship statement missing from numerous distributed assets (HTML, JSON, YAML) such as `dashboard/index.html` and AEIP schemas, risking provenance drift.【F:dashboard/index.html†L1-L12】【F:schemas/aeip/aeip-frame-schema.json†L1-L10】 |
| Legal & Licensing | Major | Dual-license requirement is not fully met—`meta/license.txt` only carries CC BY-SA 4.0 text, and many non-commentable assets lack SPDX metadata or alternative license declaration channels.【F:meta/license.txt†L1-L14】 |
| Standards & Policy Alignment | Major | Standards references state alignment without clause numbers and overuse "implied" designations, reducing verifiability (e.g., ISO 42001 references in standards brief and README).【F:docs/standards-alignment-brief.md†L5-L37】【F:README.md†L32-L35】 |
| Reproducibility & Manifest Integrity | Major | `meta/v5-manifest.yaml` omits cryptographic hashes for canonical artifacts; `meta/INTEGRITY_NOTICE.md` provides advisory guidance but no concrete values, preventing deterministic verification.【F:meta/v5-manifest.yaml†L1-L36】【F:meta/INTEGRITY_NOTICE.md†L1-L46】 |
| Terminology & Normative Consistency | Major | Appendix O contains malformed macros (e.g., `arrative{`, `ormative{`) that break ISO-2119 modal clarity and risk LaTeX build failures, undermining the normative vocabulary bridge.【F:source/appendices/appendix-o-canonical-provenance-and-signature-metadata.tex†L1-L80】 |
| Ethics, Data, and Privacy | Minor | High-level data ethics commitments exist, but Layer 2 control tables and obligation summaries do not cite Appendix E safeguards directly, weakening traceability between privacy duties and canonical safeguards.【F:DATA-ETHICS.md†L1-L11】【F:meta/layer-control-tables.json†L1-L60】 |
| Security & Cryptography | Major | AEIP signing guidance reduced to advisory notice without replacement key-generation/verification procedures, leaving ledger integrity unverifiable.【F:tools/verify-aeip-signatures.py†L1-L20】 |
| Accessibility & Interface Compliance | Minor | vitest-axe tests exist for App and glossary, yet repository lacks the mandated `docs/accessibility-checklist.md` deliverable enumerating WCAG findings.【F:dashboard/src/__tests__/a11y.spec.tsx†L1-L22】【d29b9e†L1-L1】 |
| Academic & Research Readiness | Minor | References bibliography is present, but repository does not map originality claims to version history or change plans beyond historical notes, leaving methodology traceability incomplete.【F:source/backmatter/references.bib†L1-L20】【F:README.md†L16-L18】 |
| Governance & Civic Oversight | Major | Generated control tables exist, yet Appendix O’s corruption and lack of explicit AEIP schema linkage for custodianship evidence jeopardise continuity across Appendices H, O, and P.【F:source/chapters/generated/layer1-control-table.tex†L1-L23】【F:source/appendices/appendix-o-canonical-provenance-and-signature-metadata.tex†L1-L80】 |
| Commercial & Community Readiness | Minor | Required commercial documents exist, but README lacks the mandated audit completion note linking to offerings with explicit non-endorsement language.【F:commercial/OFFERINGS.md†L1-L40】【F:README.md†L200-L238】 |
| Security of Language / Hallucination Control | Minor | No fabricated institutions detected, yet Appendix O typographical errors create anthropomorphic ambiguity (e.g., missing control keywords) that could mislead legal interpretation.【F:source/appendices/appendix-o-canonical-provenance-and-signature-metadata.tex†L1-L80】 |

## Standards Reference Crosswalk

| Standard | Repository Location | Reference Style | Notes |
| --- | --- | --- | --- |
| ISO/IEC 42001 | `README.md` (Benefits bullet) | "aligned with" (no clause) | Needs clause references for verifiability.【F:README.md†L32-L35】 |
| ISO/IEC 42001 | `docs/standards-alignment-brief.md` | "ISO 42001 (implied)" | Replace "implied" with explicit clause citations (e.g., §6.2).【F:docs/standards-alignment-brief.md†L5-L37】 |
| IEEE 7000 Series | `README.md` (Benefits bullet) | "aligned with" | Add series member and clause numbers.【F:README.md†L32-L35】 |
| NIST AI RMF | `README.md`; `docs/standards-alignment-brief.md` | "aligned" / "contextual" | Provide function IDs (Govern/Map/Measure/Manage).【F:README.md†L32-L35】【F:docs/standards-alignment-brief.md†L5-L37】 |
| EU AI Act Annex IV | `README.md`; `docs/standards-alignment-brief.md` | "requirements" / "contextual" | Cite Annex IV sections and article numbers.【F:README.md†L32-L35】【F:docs/standards-alignment-brief.md†L5-L37】 |

## Detailed Findings & Recommendations

### 1. Authorship & Provenance (Critical)
- **Observation:** Numerous assets (HTML, JSON, YAML) lack the canonical authorship statement, breaching provenance requirements and enabling misattribution.【F:dashboard/index.html†L1-L12】【F:schemas/aeip/aeip-frame-schema.json†L1-L10】 
- **Recommendation:** Embed a machine-readable provenance block (e.g., JSON metadata or HTML comment) at build time for non-comment formats; extend linting to fail when assets omit the canonical text.
- **Automated Patch Note:** Introduce a pre-commit hook that injects/validates the authorship snippet during asset generation.

### 2. Legal & Licensing (Major)
- **Observation:** Only CC BY-SA 4.0 text is distributed; Apache-2.0 terms are referenced but absent. Non-commentable files rely on implication rather than SPDX-compliant metadata.【F:meta/license.txt†L1-L14】 
- **Recommendation:** Add `LICENSE-apache-2.0.txt`, update build scripts to embed license metadata for JSON/YAML (e.g., `license` property), and extend documentation clarifying dual-license scope.
- **Automated Patch Note:** Generate license headers during schema export using a templated metadata stanza.

### 3. Standards & Policy Alignment (Major)
- **Observation:** Standards crosswalk lists "implied" linkages without clause references, limiting regulatory traceability.【F:docs/standards-alignment-brief.md†L5-L37】 
- **Recommendation:** Update tables with clause numbers (e.g., ISO/IEC 42001 §8.2) and add footnotes referencing official documents or appendices that detail alignment analysis.

### 4. Reproducibility & Manifest Integrity (Major)
- **Observation:** Manifest and integrity notice lack concrete hashes; instructions remain advisory, preventing deterministic verification.【F:meta/v5-manifest.yaml†L1-L36】【F:meta/INTEGRITY_NOTICE.md†L1-L46】 
- **Recommendation:** Publish SHA-512 for canonical PDF, manifest, and integrity notice, plus capture the release commit ID. Provide reproducible LaTeX build command with pinned TeX Live image.

### 5. Terminology & Normative Consistency (Major)
- **Observation:** Appendix O contains broken macros (`arrative{`, `ormative{`, `egin{quote}`), breaking normative register and ISO-2119 modal clarity.【F:source/appendices/appendix-o-canonical-provenance-and-signature-metadata.tex†L1-L80】 
- **Recommendation:** Repair macros, ensure each normative block references Appendix A definitions, and add linting to detect malformed command prefixes.

### 6. Ethics, Data, and Privacy (Minor)
- **Observation:** Data ethics statement references Appendix E but Layer 2 control table omits explicit safeguard citations, reducing traceability from obligations to privacy controls.【F:DATA-ETHICS.md†L1-L11】【F:meta/layer-control-tables.json†L1-L60】 
- **Recommendation:** Update control tables and AEIP schemas to cite Appendix E clauses directly (e.g., `Appendix E §3`).

### 7. Security & Cryptography (Major)
- **Observation:** Signing guidance reduced to advisory message; no key generation, signing, or verification workflows are documented.【F:tools/verify-aeip-signatures.py†L1-L20】 
- **Recommendation:** Provide stubbed scripts or documentation for key lifecycle, even if advisory, and describe ledger verification processes.

### 8. Accessibility & Interface Compliance (Minor)
- **Observation:** Automated accessibility tests exist, yet mandated accessibility checklist document is missing from `docs/` tree.【F:dashboard/src/__tests__/a11y.spec.tsx†L1-L22】【d29b9e†L1-L1】 
- **Recommendation:** Publish `docs/accessibility-checklist.md` summarizing WCAG 2.1 AA test results and manual review notes.

### 9. Academic & Research Readiness (Minor)
- **Observation:** References bibliography exists but originality claims in README lack linkage to prior versions or update plans, reducing scholarly auditability.【F:source/backmatter/references.bib†L1-L20】【F:README.md†L16-L18】 
- **Recommendation:** Add change-log mapping of claims to appendices/update plans and cite relevant historical releases.

### 10. Governance & Civic Oversight (Major)
- **Observation:** Control tables generated, but Appendix O corruption blocks custodianship → AEIP schema linkage, risking oversight continuity.【F:source/chapters/generated/layer1-control-table.tex†L1-L23】【F:source/appendices/appendix-o-canonical-provenance-and-signature-metadata.tex†L1-L80】 
- **Recommendation:** Repair Appendix O, ensure cross-references to AEIP custodianship schema, and document signature protocols.

### 11. Commercial & Community Readiness (Minor)
- **Observation:** Commercial documents exist, yet README lacks required audit changelog entry linking to offerings while reinforcing non-endorsement language.【F:commercial/OFFERINGS.md†L1-L40】【F:README.md†L200-L238】 
- **Recommendation:** Add "v5.0 Full Repository Audit — All Integrity Checks Passed" entry with explicit independent-author reminder and link to `commercial/`.

### 12. Security of Language / Hallucination Control (Minor)
- **Observation:** No fabricated institutions found, but Appendix O typographical errors degrade clarity of mandatory language and could be misinterpreted legally.【F:source/appendices/appendix-o-canonical-provenance-and-signature-metadata.tex†L1-L80】 
- **Recommendation:** Fix command typos and add editorial review focusing on anthropomorphic or ambiguous phrasing.

---

Authorship & Provenance — The AI OSI Stack was conceived, authored, and maintained by Daniel P. Madden as an independent, self-funded project. There is no institutional, corporate, or governmental backing. Any references to organizations, domains, or future bodies are aspirational placeholders for a community that does not yet exist.

Large-language-model tools were used under author supervision; all final content reviewed and approved by Daniel P. Madden.
