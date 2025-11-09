<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Product One-Pager — AI OSI Stack v5

**Canonical reference:** AI OSI Stack v5 (version v5.0-rc, 2025-11-09). Source materials: [README](../README.md), [docs/architecture-overview.md](../docs/architecture-overview.md), [docs/governance-dashboard/control-tower-readme.md](../docs/governance-dashboard/control-tower-readme.md), [docs/aeip-spec-v1-3.md](../docs/aeip-spec-v1-3.md).

## Component Overview

| Component | Purpose | Customer Value |
|-----------|---------|----------------|
| **AEIP Schemas & Protocol** | Encode Decision Rationale Records, Governance Disclosure Statements, Integrity Ledger Entries with signed provenance. | Provides machine-verifiable compliance evidence tied to regulatory clauses and audits. |
| **Governance Spine Runtime (`govspine/`)** | Implements stack layer contracts, validation utilities, and registry hooks. | Accelerates integration with existing AI pipelines while preserving canonical governance logic. |
| **Control Tower Dashboard** | FastAPI + React scaffold for asset registry, manifest crosswalks, and audit telemetry. | Gives risk, legal, and oversight teams a unified cockpit for AEIP manifests and ledger health. |
| **Interpretive Canon & Documentation** | Layered chapters, standards briefs, and legal outreach materials. | Equips executives and regulators with plain-language guidance tied to canonical artefacts. |
| **Integrity Notice & Verification Guide** | Deferred-signing policy, checksum workflow, and validation playbook. | Ensures trust in releases and aligns customers with advisory signing procedures. |

## Stack & AEIP Flow (Diagram Placeholder)

```
[Layer 0 Civic Mandate] → [Layer 1 Ethical Charter] → … → [Layer 7 Governance Publication]
        ↓                            ↓                              ↓
   AEIP Intent ↔ Justification ↔ Counter-Signature ↔ Ledger Commit ↔ Dashboard Disclosure
```

> Replace placeholder with a 7-layer plus AEIP lifecycle graphic during design polish.

## Pillars in One Sentence Each

- **AEIP:** A privacy-aware protocol that binds every AI decision to temporal, provenance, and governance metadata so evidence survives scrutiny ([docs/aeip-spec-v1-3.md](../docs/aeip-spec-v1-3.md)).
- **Persona Architecture:** Structured roles and refusal logic that keep AI personas bounded by civic mandates and ethical charters ([docs/architecture-overview.md](../docs/architecture-overview.md), [docs/persona-architecture-v1.pdf](../docs/persona-architecture-v1.pdf)).
- **Dashboard:** The Control Tower surfaces asset registries, manifest crosswalks, and audit telemetry for continuous oversight ([docs/governance-dashboard/control-tower-readme.md](../docs/governance-dashboard/control-tower-readme.md)).
- **Ledger:** Integrity notices and AEIP ledger receipts document deferred signing, custodial rights, and verification workflows ([INTEGRITY_NOTICE.md](../INTEGRITY_NOTICE.md), [docs/VERIFICATION_GUIDE.md](../docs/VERIFICATION_GUIDE.md)).
