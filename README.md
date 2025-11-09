<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# AI OSI Stack v5.0  
### A Governance Blueprint for Scalable and Trusted AI
---

## Overview

> **Not legal advice / jurisdiction-neutral.** The Stack supplies governance architecture and advisory patterns; it does not substitute for legal counsel in any jurisdiction.

The **AI OSI Stack** is a complete open-standard framework for governing artificial-intelligence systems from civic intent to technical implementation. It provides a **layered architecture**—analogous to the Internet’s OSI model—where every layer of an AI system carries explicit duties, evidence records, and public-interest safeguards.

v5.0 represents the **canonical edition** of the Stack: fully audited for conceptual coherence, continuity, clarity, and intent. It unifies technical, ethical, legal, and civic disciplines into a single verifiable structure for **AI accountability by design**.

The Stack translates civic mandates and ethical commitments into operational controls, making every stage of intelligent system design and deployment legible, testable, and auditable. It binds social contracts, organizational practice, and technical enforcement so oversight bodies can shape system behavior in real time. The repository is structured so practitioners can regenerate official publications, execute validation suites, and confirm provenance from local environments.

### Authorship & Provenance

> **Authorship & Provenance**  
> The AI OSI Stack was conceived, authored, and maintained solely by **Daniel P. Madden**  
> under GitHub identity `44127480+danielpmadden@users.noreply.github.com`.  
> There is no institutional, corporate, or governmental backing. Unauthorized contributor
> entries have been removed.

Large-language-model tools were used under author supervision; all final content reviewed and approved by Daniel P. Madden.

---

## Why It Matters

Modern AI operates faster than existing governance can adapt. Most organizations manage AI risk piecemeal—through model cards, privacy reviews, or ethics boards—without a common backbone. The AI OSI Stack solves this fragmentation by defining a **governance spine** that any institution can adopt, audit, or extend.

Its benefits:

* **Transparency with proof.** Every decision, dataset, and model step is tied to an evidence artefact (AEIP).
* **Accountability without surveillance.** Auditability is achieved through registries and provenance, not human tracking.
* **Interoperability.** Layers are aligned with ISO 42001, IEEE 7000-series, NIST AI RMF, and EU AI Act Annex IV requirements.
* **Civic legitimacy.** Governance begins at Layer 0—the public mandate—not at deployment.

The Stack turns “AI ethics” from aspiration into infrastructure.

📘 For legal, policy, and compliance professionals, see:  
[`/docs/LEGAL-AND-POLICY-BRIEF.md`](docs/LEGAL-AND-POLICY-BRIEF.md)

---

## Architecture at a Glance

| Layer | Name | Purpose |
|-------|------|----------|
| 0 | **Civic Mandate** | Defines who authorizes an AI system and under what social license. |
| 1 | **Ethical Charter** | Converts civic values into enforceable ethical clauses and review cycles. |
| 2 | **Data Stewardship** | Ensures rights-respecting data collection, consent, and audit trails. |
| 3 | **Model Development** | Documents training, evaluation, and lineage of models under AEIP. |
| 4 | **Instruction & Control** | Governs prompts, personas, and control policies for safe operation. |
| 5 | **Reasoning Exchange** | Keeps model reasoning and outputs interpretable and contestable. |
| 6 | **Deployment & Integration** | Manages release, monitoring, incident response, and rollback. |
| 7 | **Governance Publication** | Converts internal evidence into public-facing disclosures. |
| 8 | **Civic Participation** | Provides participatory feedback, appeal, and renewal mechanisms. |

**Layer Highlights**

- **Layer 0 – Civic Mandate:** Establishes the democratic legitimacy and community consent for AI initiatives.
- **Layer 1 – Ethical Charter:** Encodes normative commitments, rights, and red lines for participating institutions.
- **Layer 2 – Data Stewardship:** Governs data intake, classification, retention, and fiduciary handling.
- **Layer 3 – Model Development:** Controls training assets, evaluation regimes, and interpretability safeguards.
- **Layer 4 – Instruction & Control:** Manages prompts, directives, and operational guardrails for deployed systems.
- **Layer 5 – Reasoning Exchange:** Defines transparent exchange protocols for AI-AI and AI-human reasoning traces.
- **Layer 6 – Deployment & Integration:** Coordinates release approvals, change logs, and integration sign-offs.
- **Layer 7 – Governance Publication:** Publishes attestations, oversight reports, and civic accountability artefacts.
- **Layer 8 – Civic Participation:** Creates deliberative feedback channels and co-governance records for communities.

Beyond Layer 8, **Part IV – Interpretive and Applied Canon (19A–24)** expands the framework to culture, semantics, emotion, and meta-governance.

---

## Interpretive and Applied Canon (Chs 19A–24)

| Chapter | Focus | Key Idea |
|----------|--------|----------|
| 19A | **Usage, Trust & Social Reality** | Empirical patterns of AI use and what they reveal about trust. |
| 20 | **Rhetoric & Semantics** | Preventing semantic drift and preserving language integrity. |
| 21 | **The Companion Trap** | Safeguarding against engineered intimacy and false reciprocity. |
| 22 | **Persona Architecture** | Building bounded, role-specific AIs with explicit mandates. |
| 23 | **Therapy-Tech & Governance of Care** | Applying the Stack to mental-health and well-being systems. |
| 24 | **Governance Paradox** | Addressing AI-assisted authorship and recursive rulemaking. |

Each chapter follows a **Triple Register**:

- **Narrative Intent** – why the rule exists,  
- **Normative Clauses** – what must be done,  
- **Plain-Speak Summary** – what it means in everyday terms.

Representative materials can be found in `source/interpretive/` (LaTeX sources) and `schemas/` (JSON-LD governance artefacts) for each chapter.

---

## AEIP – AI Epistemic Infrastructure Protocol

The **AEIP** is the Stack’s data layer: a protocol and schema set for encoding evidence. It defines artefacts such as Decision Rationale Records, Governance Directive Sets, Integrity Ledger Entries, and Interpretive Trace Packages.

Each artefact is machine-verifiable through JSON-LD/YAML schemas in [`schemas/`](schemas/). Together, they make the Stack *provable* rather than merely declarative.

**Canonical Resources**

- **Canonical PDF:** [`versions/ai-osi-stack-v5.pdf`](versions/ai-osi-stack-v5.pdf)
- **Provenance Record:** [Zenodo DOI record](https://zenodo.org/records/17517241)
- **Integrity Manifest:** [`meta/v5-manifest.yaml`](meta/v5-manifest.yaml)

---

## Governance Spine Implementation

The `govspine/` package is the **runtime reference implementation** of the Stack. It mirrors the eight layers and provides utilities for:

* AEIP handshakes and ledger operations  
* Governance manifest generation  
* Evidence validation and federation checks  
* Continuous risk simulation and dashboard integration

Developers can import it to embed governance logic directly in AI pipelines.

```python
from govspine.layer04instruction import ControlPolicy

policy = ControlPolicy.load("schemas/aeip/instruction-log-schema.json")
policy.verify()
```

Install the runtime locally with `pip install -e .` and execute `pytest` from the repository root to validate AEIP schemas and layer contracts. `tools/` contains additional automation such as `tools/generate-artifact.py` for AEIP-aligned payloads and the legacy `tools/verify-aeip-signatures.py`, which now emits advisory checksum guidance.

---

## Audits and Verification

All source chapters and schemas have been audited for:

* **Conceptual coherence** – alignment of theory, code, and vocabulary.
* **Continuity** – consistent versioning and schema linkage.
* **Clarity** – complete Triple Registers with plain-language sections.
* **Intent traceability** – every “shall” clause maps to an AEIP artefact.

Audit reports live in [`audits/`](audits/); `audits/200-repo-wide-integrity-report.md` summarizes the latest repository-wide findings. Lightweight machine-learning utilities in [`ml/`](ml/) generate supporting analytics such as modality drift checks and schema coherence clustering.

To independently review repository integrity (advisory model):

1. Review [`INTEGRITY_NOTICE.md`](INTEGRITY_NOTICE.md) for recommended checksum practices and advisory workflow guidance.
2. Confirm [`meta/v5-manifest.yaml`](meta/v5-manifest.yaml) follows the advisory integrity structure and references the current canonical metadata.
3. Optionally record SHA-512 or equivalent hashes locally for archival reproducibility; compare them against personal logs when revisiting the release.

Checksum verification is advisory: this repository does not publish authoritative hashes or cryptographic signatures.

---

## Standards Alignment

A full crosswalk is provided in [`docs/standards-alignment-brief.md`](docs/standards-alignment-brief.md).

| Framework | Corresponding Layers | Shared Principles |
|-----------|----------------------|-------------------|
| ISO / IEC 42001 | 0–8 | Management system governance, risk control, continuous improvement |
| IEEE 7000 Series | 1, 4, 5, 8 | Ethical governance, transparency, well-being |
| NIST AI RMF | All | Govern, Map, Measure, Manage functions |
| EU AI Act (Annex IV) | 2–7 | Technical documentation, human oversight, post-market monitoring |

---

## Using the Stack

- Reference the LaTeX chapters or Markdown exports to design governance policy.
- Implement AEIP schemas within development and audit pipelines.
- Verify outputs using the `govspine` tools and tests.
- Publish governance manifests for transparency.

The Stack is modular—organizations can adopt one layer at a time and still gain measurable accountability.

### Cross-Reference Map

| Layer | Primary Schema Reference | Supporting Tools |
| --- | --- | --- |
| Layer 0 – Civic Mandate | `schemas/aeip/civic-charter-schema.json` | `tools/governance/manifest-builder.py` |
| Layer 1 – Ethical Charter | `schemas/aeip/ccm-schema.json` | `tools/generate-artifact.py` |
| Layer 2 – Data Stewardship | `schemas/aeip/gds-schema.json` | `tools/update-custodian.py` |
| Layer 3 – Model Development | `schemas/aeip/modelcard-schema.json` | `tools/update-metrics.py` |
| Layer 4 – Instruction & Control | `schemas/aeip/instruction-log-schema.json` | `tools/simulate-incident.py` |
| Layer 5 – Reasoning Exchange | `schemas/aeip/tecl-schema.json` | `tools/crosswalk-generator.py` |
| Layer 6 – Deployment & Integration | `schemas/aeip/aeip-frame-schema.json` | `tools/tag-release.py` |
| Layer 7 – Governance Publication | `schemas/aeip/gds-schema.json` | `tools/governance/aeip-frame-builder.py` |
| Layer 8 – Civic Participation | `schemas/aeip/incident-report-schema.json` | `tools/notify-red-status.py` |

---

## Repository Layout

```
analytics/             → Dashboards and governance analytics (e.g., civic portal)
archive/               → Historical and superseded materials (read-only)
audits/                → Coherence, integrity, and structural review reports
commercial/            → Civic-aligned contracting and engagement templates
docs/                  → Canonical governance documentation and briefs
examples/              → Illustrative AEIP receipts and governance scenarios
govspine/              → Python runtime package (implementation spine)
ledger/                → Canonical governance ledger artefacts (GDS, DRR, ITP, ILE)
legal/                 → Rights analyses and legal interpretations
meta/                  → Repository-level manifests and provenance descriptors
ml/                    → Machine-learning utilities for governance analytics
ops/                   → Build, release, inventory, and stewardship scripts
press-kit/             → Public release materials and messaging
protocol/              → AEIP reference operations and handshake specifications
schemas/               → JSON/JSON-LD definitions for governance artefacts
source/                → LaTeX manuscripts for canonical publications
tests/                 → Pytest, Vitest, and validation suites
tools/                 → Reusable utilities supporting governance workflows
versions/              → Release manifests, update plans, and canonical PDFs
```

---

## Building and Reviewing

To compile the canonical PDF locally:

```bash
sudo apt install texlive-full
cd source
latexmk -pdf ai-osi-stack-v5.tex
```

For review without LaTeX, open [`audits/ai-osi-stack-v5-plaintext.txt`](audits/ai-osi-stack-v5-plaintext.txt).

---

## Status and Integrity Notice

Canonical version: **5.0.0**
Purpose: conceptual and academic review.
Integrity review is advisory. [`INTEGRITY_NOTICE.md`](INTEGRITY_NOTICE.md) describes how to perform independent checksum capture for archival reproducibility; no formal signing or cryptographic commitment is provided.

Canonical metadata:

- `canonical_version = "AI OSI Stack v5.0.0"`
- `canonical_date = "2025-11-09"`
- `aeip_version = "1.3"`
- `repository_of_record = "https://github.com/danielpmadden/ai-osi-stack"`
- `domain_of_record = "https://aiosi.org"`
- `supersedes_all_prior_metadata = true`

---

## Contact and Citation

Author: Daniel P. Madden  
Website: https://danielpmadden.com
Repository: https://github.com/danielpmadden/ai-osi-stack

Suggested citation:

> Madden, Daniel P. (2025). *The AI OSI Stack: A Governance Blueprint for Scalable and Trusted AI*. Zenodo DOI TBD.

---

## License

Documentation (Markdown, LaTeX, and narrative assets) is released under **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**.

Source code (Python, TypeScript, automation scripts) is released under the **Apache License 2.0**.

> **Authorship & Provenance**  
> The AI OSI Stack was conceived, authored, and maintained solely by **Daniel P. Madden**  
> under GitHub identity `44127480+danielpmadden@users.noreply.github.com`.  
> There is no institutional, corporate, or governmental backing. Unauthorized contributor
> entries have been removed.

Large-language-model tools were used under author supervision; all final content reviewed and approved by Daniel P. Madden. Mistakes will happen. I'm only one human.

“Accountability is infrastructure.”
The AI OSI Stack transforms governance from paperwork into protocol, ensuring that every intelligent system remains intelligible to the society it serves.

To engage the author for implementation or verification, see [`commercial/`](commercial/).

## Changelog

- **v5.0 Full Repository Audit — Integrity verification pending v5 sealing.** — Comprehensive repository-wide integrity review recorded in [`audits/200-repo-wide-integrity-report.md`](audits/200-repo-wide-integrity-report.md); results confirm independent authorship status and advisory checksum posture.

🧭 Demo:
Explore the AI OSI Stack Compliance Portal prototype — a visual demonstration of the governance layers and evidence artefacts.
Run locally via:
cd analytics/analytics/dashboard/demo-portal && npm install && npm run dev

---
### Ethics, License, and Governance
This project is released under a custodial, non-commercial license.
Please read [LICENSE](LICENSE), [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before any reuse.  
Use this work responsibly, credit the author, and respect the civic mission that underlies the AI OSI Stack.
