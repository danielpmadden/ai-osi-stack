
# AI OSI Stack v5.0 (Open-Core)
## A Governance Blueprint for Scalable and Trusted AI

**AI OSI Stack** is a civic governance and documentation framework authored and maintained by **Daniel P. Madden**. This public repository provides the open-core standards, schemas, exemplar ledgers, and validator-lite tools needed to understand and steward the Stack’s governance model.

- **Current Release:** `v5.0-open-core` *(pre-v5 governance lock)*
- **Next Release:** `v5.0` *(full canonical publication pending integrity review)*

The operational implementations—**Governance Control Tower™**, AEIP runtime services, ledger execution engines, analytics dashboards, and affiliated commercial tooling—remain proprietary. This repository focuses on transparency, civic legitimacy, and reproducible documentation.

### Custodianship & Authorship
This repository constitutes the official and sole open-core release of the **AI OSI Stack™ (v5.0)**.  

All civic documentation, schema definitions, and layer structures are © 2025 Daniel P. Madden.  

Any other repository, fork, or derivative claiming authorship or affiliation is **unauthorized and unofficial**.  

Commercial and runtime implementations (AEIP™, Governance Control Tower™) remain proprietary to the author.

## What’s Open vs. What’s Private

| Scope | Status | Notes |
| --- | --- | --- |
| Civic governance standards, chapters, and briefs | ✅ Open-core | Markdown, LaTeX, and schema references defining the AI OSI Stack’s governance canon. |
| Schemas, ledgers, and exemplar artefacts | ✅ Open-core | Reference AEIP payloads, integrity notices, and provenance manifests for study and validation. |
| Validator-lite utilities | ✅ Open-core | `_open_tools/` scripts for schema linting, documentation synthesis, and integrity spot-checks. |
| Governance Control Tower™ runtime | ⛔ Private | Operational automation, orchestration services, and runtime governance bindings reside in private repositories. |
| AEIP runtime, ledger engines, analytics dashboards | ⛔ Private | Commercial offerings that implement enforcement, telemetry, and dashboards. |

## Repository Layout

```
├── docs/            Civic standards, briefs, and interpretive canon
├── schemas/         JSON/JSON-LD definitions for AEIP artefacts
├── ledger/          Sample receipts and integrity walkthroughs
├── legal/           Historical custody and license mappings
├── LEGAL/           Public IP boundary and trademark notices
├── audits/          Civic integrity and structure assessments
├── meta/            Manifests, integrity notes, and canonical markers
├── press-kit/       Public announcements and media collateral
├── source/          Typeset manuscripts and generated tables
├── versions/        Versioned releases and historical packages
├── _open_tools/     Validator-lite scripts for schema/document hygiene
└── _ip_review/      Audit memoranda for the open-core boundary
```

## Layer-to-AEIP Schema Summary (v5.0-open-core)

| Layer | Documentation | AEIP Schema References |
| --- | --- | --- |
| Layer 0 – Civic Mandate | [04_Layer_0_Civic_Mandate.md](docs/AI_OSI_Stack/04_Layer_0_Civic_Mandate.md) | [`schemas/aeip/aeip-intent.schema.json`](schemas/aeip/aeip-intent.schema.json), [`schemas/aeip/civic-charter-schema.json`](schemas/aeip/civic-charter-schema.json) |
| Layer 1 – Ethical Charter | [05_Layer_1_Ethical_Charter.md](docs/AI_OSI_Stack/05_Layer_1_Ethical_Charter.md) | [`schemas/aeip/aeip-justify.schema.json`](schemas/aeip/aeip-justify.schema.json), [`schemas/aeip/tecl-schema.json`](schemas/aeip/tecl-schema.json) |
| Layer 2 – Data Stewardship | [06_Layer_2_Data_Stewardship.md](docs/AI_OSI_Stack/06_Layer_2_Data_Stewardship.md) | [`schemas/aeip/ccm-schema.json`](schemas/aeip/ccm-schema.json) |
| Layer 3 – Model Development | [07_Layer_3_Model_Development.md](docs/AI_OSI_Stack/07_Layer_3_Model_Development.md) | [`schemas/aeip/modelcard-schema.json`](schemas/aeip/modelcard-schema.json) |
| Layer 4 – Instruction & Control | [08_Layer_4_Instruction_Control.md](docs/AI_OSI_Stack/08_Layer_4_Instruction_Control.md) | [`schemas/aeip/instruction-log-schema.json`](schemas/aeip/instruction-log-schema.json), [`schemas/aeip/aeip-frame-schema.json`](schemas/aeip/aeip-frame-schema.json) |
| Layer 5 – Reasoning Exchange | [09_Layer_5_Reasoning_Exchange.md](docs/AI_OSI_Stack/09_Layer_5_Reasoning_Exchange.md) | [`schemas/aeip/aeip-countersign.schema.json`](schemas/aeip/aeip-countersign.schema.json), [`schemas/aeip/aeip-frame-schema.json`](schemas/aeip/aeip-frame-schema.json) |
| Layer 6 – Deployment & Integration | [10_Layer_6_Deployment_Integration.md](docs/AI_OSI_Stack/10_Layer_6_Deployment_Integration.md) | [`schemas/aeip/aeip-commit.schema.json`](schemas/aeip/aeip-commit.schema.json), [`schemas/aeip/gds-schema.json`](schemas/aeip/gds-schema.json), [`schemas/aeip/incident-report-schema.json`](schemas/aeip/incident-report-schema.json), [`schemas/aeip/aeip-frame-schema.json`](schemas/aeip/aeip-frame-schema.json) |
| Layer 7 – Governance Publication | [11_Layer_7_Governance_Publication.md](docs/AI_OSI_Stack/11_Layer_7_Governance_Publication.md) | [`schemas/aeip/aeip-update.schema.json`](schemas/aeip/aeip-update.schema.json), [`schemas/aeip/gds-schema.json`](schemas/aeip/gds-schema.json), [`schemas/aeip/aeip-frame-schema.json`](schemas/aeip/aeip-frame-schema.json) |
| Layer 8 – Civic Participation | [12_Layer_8_Civic_Participation.md](docs/AI_OSI_Stack/12_Layer_8_Civic_Participation.md) | [`schemas/aeip/aeip-update.schema.json`](schemas/aeip/aeip-update.schema.json), [`schemas/integrity-ledger-entry.jsonld`](schemas/integrity-ledger-entry.jsonld) |

## Stewardship Principles

- **Single authorship.** All materials are authored and curated by Daniel P. Madden; contributions occur only through explicit custodial channels.
- **Civic-first orientation.** The open-core set preserves civic legitimacy, contextual documentation, and verification pathways.
- **Clear IP boundary.** Proprietary runtimes and commercial services are out of scope; this repository documents standards, not implementations.

### Authorship & Contact

The maintainer can be reached via GitHub identity `44127480+danielpmadden@users.noreply.github.com`. See `CANONICAL_PROVENANCE.yaml` for provenance metadata and `INTEGRITY_NOTICE.md` for checksum workflow guidance.

---

> **IP Boundary Excerpt**  
> AEIP runtime, Governance Control Tower, ledger engines, and analytics dashboards are proprietary and excluded from this repository.  
> © 2025 Daniel P. Madden. All rights reserved. See `LICENSE` and `LEGAL/TRADEMARK-NOTE.md` for usage guidance.

## Custodianship & Provenance Summary

- Custodial Author: Daniel P. Madden (sole Independent Custodian).
- Canonical Version: `AI OSI Stack v5.0-open-core (Civic Standard Edition)` as recorded in `CANONICAL_PROVENANCE.yaml`.
- Licensing: Documentation under CC BY-SA 4.0; code artifacts under Apache-2.0.
- Verification: See `_ip_review/REPO_FINAL_AUDIT_v5.0-open-core.md` and `meta/v5-open-core-sha512-manifest.txt` for integrity confirmations.
- Trademarks: Refer to `LEGAL/TRADEMARK-NOTE.md` and `LEGAL/VALIDATION-NOTICE.md` for custodial use guidance.

