# AI OSI Stack v5 — Canonical Edition

The AI OSI Stack is a layered governance architecture for verifiable AI accountability. It translates civic mandates and ethical commitments into operational controls, making every stage of intelligent system design and deployment legible, testable, and auditable. The stack binds social contracts, organizational practice, and technical enforcement so oversight bodies can see and shape system behavior in real time.

This repository exists to make ethics auditable and civic oversight practical. Each layer specifies the evidence, process, and assurances required to keep advanced AI systems aligned with democratic values. The accompanying AEIP (AI Epistemic Infrastructure Protocol) schemas standardize how evidence is generated, verified, and preserved so communities can contest or validate AI decisions with confidence.

AI OSI Stack v5 serves governments, enterprises, auditors, and citizens. Policymakers gain a canonical reference, operators inherit executable tools, auditors receive traceable records, and the public can inspect integrity guarantees without reverse engineering private systems. The repository is structured so practitioners can regenerate official publications, execute validation suites, and confirm provenance from local environments.

## Layer Overview
- **Layer 0 – Civic Mandate:** Establishes the democratic legitimacy and community consent for AI initiatives.
- **Layer 1 – Ethical Charter:** Encodes normative commitments, rights, and red lines for participating institutions.
- **Layer 2 – Data Stewardship:** Governs data intake, classification, retention, and fiduciary handling.
- **Layer 3 – Model Development:** Controls training assets, evaluation regimes, and interpretability safeguards.
- **Layer 4 – Instruction & Control:** Manages prompts, directives, and operational guardrails for deployed systems.
- **Layer 5 – Reasoning Exchange:** Defines transparent exchange protocols for AI-AI and AI-human reasoning traces.
- **Layer 6 – Deployment & Integration:** Coordinates release approvals, change logs, and integration sign-offs.
- **Layer 7 – Governance Publication:** Publishes attestations, oversight reports, and civic accountability artifacts.
- **Layer 8 – Civic Participation:** Creates deliberative feedback channels and co-governance records for communities.

**Part IV – Interpretive and Applied Canon (Chs 19A–24)**
- **19A – Usage, Trust & Social Reality:** Empirical usage narratives justify semantic governance and reinforce civic evidence loops for trust calibration. [`chapter-19a-usage-and-trust.tex`](source/interpretive/chapter-19a-usage-and-trust.tex)
- **20 – Rhetoric & Semantics:** Establishes linguistic integrity, semantic version control, and verifiable language governance through registry-based accountability. [`chapter-20-rhetoric-and-semantics.tex`](source/interpretive/chapter-20-rhetoric-and-semantics.tex) · [`semantic-registry.jsonld`](schemas/svc/semantic-registry.jsonld)
- **21 – The Companion Trap:** Governs affective AI, engineered warmth, and consent safeguards to prevent exploitative intimacy loops. [`chapter-21-companion-trap.tex`](source/interpretive/chapter-21-companion-trap.tex)
- **22 – Persona Architecture:** Codifies bounded personas as ethical design units with manifest-based accountability and lifecycle governance. [`chapter-22-persona-architecture.tex`](source/interpretive/chapter-22-persona-architecture.tex) · [`persona/registry.jsonld`](schemas/persona/registry.jsonld)
- **23 – Therapy-Tech & Governance of Care:** Applies Stack principles to mental-health ecosystems, harmonising duty-of-care, credential verification, and crisis response. [`chapter-23-therapy-tech-and-governance-of-care.tex`](source/interpretive/chapter-23-therapy-tech-and-governance-of-care.tex) · [`therapy/credential-verification.jsonld`](schemas/therapy/credential-verification.jsonld)
- **24 – Governance Paradox:** Formalises AI-assisted authorship, recursive drafting, and transparent ratification of governance artifacts. [`chapter-24-governance-paradox.tex`](source/interpretive/chapter-24-governance-paradox.tex) · [`governance/ai-assisted-drafting.jsonld`](schemas/governance/ai-assisted-drafting.jsonld)

These chapters expand governance guidance into semantics, intimacy, care, and meta-authorship while remaining anchored to Layers 0–8 and existing AEIP schemas.

## Canonical Resources
- **Canonical PDF:** [`versions/ai-osi-stack-v5.pdf`](versions/ai-osi-stack-v5.pdf)
- **AEIP Schemas:** [`schemas/`](schemas/)
- **Provenance Record:** [Zenodo DOI record](https://zenodo.org/records/17517241)

## Repository Layout
- `source/` — LaTeX sources for the canonical manuscript (`chapters/`, `appendices/`, `frontmatter/`, and `backmatter/`).
- `schemas/` — Machine-readable AEIP definitions, governance ledgers, and supporting schema templates.
- `tools/` — Verification utilities, automation scripts, and governance runtime helpers (Python/CLI).
- `docs/` — Supplemental guides, dashboards, and explanatory materials that elaborate the stack.
- `tests/` — Automated validation suites for AEIP compliance, layer contracts, and runtime interfaces.
- `versions/` — Canonical release artifacts, historical packages, and update plans (see `versions/historical/`).

## Major Tooling & Build Instructions
- **Governance Spine Runtime:** Use `pip install -e .` to expose the `govspine` bridge for runtime tests.
- **Artifact Generation:** Run `python tools/generate-artifact.py --help` to create AEIP-compliant payloads.
- **Signature Verification:** `python tools/verify-aeip-signatures.py --manifest v5-manifest.yaml` verifies AEIP signatures and manifest integrity.
- **Manuscript Build:** From `source/`, run `latexmk -pdf ai-osi-stack-v5.tex` to regenerate the canonical PDF.
- **Test Suite:** Execute `pytest` from the repository root to validate AEIP schemas and layer contracts.

## Cross-Reference Map
| Layer | Primary Schema Reference | Supporting Tools |
| --- | --- | --- |
| Layer 0 – Civic Mandate | `schemas/aeip/civic-charter-schema.json` | `tools/governance/manifest-builder.py`
| Layer 1 – Ethical Charter | `schemas/aeip/ccm-schema.json` | `tools/generate-artifact.py`
| Layer 2 – Data Stewardship | `schemas/aeip/gds-schema.json` | `tools/update-custodian.py`
| Layer 3 – Model Development | `schemas/aeip/modelcard-schema.json` | `tools/update-metrics.py`
| Layer 4 – Instruction & Control | `schemas/aeip/instruction-log-schema.json` | `tools/simulate-incident.py`
| Layer 5 – Reasoning Exchange | `schemas/aeip/tecl-schema.json` | `tools/crosswalk-generator.py`
| Layer 6 – Deployment & Integration | `schemas/aeip/aeip-frame-schema.json` | `tools/tag-release.py`
| Layer 7 – Governance Publication | `schemas/aeip/gds-schema.json` | `tools/governance/aeip-frame-builder.py`
| Layer 8 – Civic Participation | `schemas/aeip/incident-report-schema.json` | `tools/notify-red-status.py`

## Citation & License
- **Preferred Citation:** Madden, Daniel P. (2025). *AI OSI Stack v5 — Canonical Edition*. https://github.com/danielpmadden/ai-osi-stack.
- **License:** Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0). See [`license.txt`](license.txt).
- **Canonical Metadata:** `canonical_version="AI OSI Stack v5"`, `canonical_date="2025-11-07"`, `aeip_version="1.3"`, `repository_of_record="https://github.com/danielpmadden/ai-osi-stack"`, `domain_of_record="https://aiosi.org"`, `supersedes_all_prior_metadata=true`.

## How to Verify This Repository
1. Review [`INTEGRITY_NOTICE.md`](INTEGRITY_NOTICE.md) for SHA-512 checksums and verification workflow.
2. Confirm `v5-manifest.yaml` matches the checksums and includes the active commit hash.
3. Run `python tools/verify-aeip-signatures.py --manifest v5-manifest.yaml` to validate signatures and ledger continuity.

Verification artifacts are non-negotiable: if an archive lacks the manifest, integrity notice, or matching checksums, treat it as non-canonical.
