---
canonical_version: "AI OSI Stack v5"
canonical_date: "2025-11-07"
aeip_version: "1.3"
repository_of_record: "https://github.com/danielpmadden/ai-osi-stack"
domain_of_record: "https://aiosi.org"
supersedes_all_prior_metadata: true
---

# AEIP Schema Catalogue — Canonical Reference

**Integrity Notice:** Version hash: TBD. Generated on 2025-11-07T00:00:00Z.

## Purpose

This catalogue enumerates the AEIP artifact schemas that safeguard interoperability, temporal integrity, and ethical accountability across the AI OSI Stack v5. Each schema is authored in JSON-LD or JSON Schema and aligned with AEIP 1.3 to guarantee machine-readable conformance and governance traceability.

## Artifact Purposes and Layer Mappings

| Artifact Type | Governance Purpose | Primary AI OSI Layer Alignment |
| --- | --- | --- |
| Interpretive Trace Package (ITP) | Captures interpretive reasoning chains and evidence supporting model understanding | Layer 3 – Model Development |
| Decision Rationale Record (DRR) | Documents deliberative justification for governance determinations | Layer 4 – Instruction & Control |
| Governance Decision Summary (GDS) | Communicates finalized governance outcomes and mandated actions | Layer 6 – Deployment & Integration |
| Oversight Audit Memo (OAM) | Records oversight findings, assurance results, and remediation directives | Layer 7 – Governance Publication |
| Integrity Ledger Entry (ILE) | Notarizes governance events with temporal sequencing and cryptographic assurance | Layer 7 – Governance Publication |
| Civic Charter | Establishes civic mandate, consent, and rights alignment | Layer 0 – Civic Mandate |
| Custodial Controls Matrix (CCM) | Maps fiduciary obligations and custodial controls | Layer 2 – Data Stewardship |
| Temporal Exchange Chain Log (TECL) | Traces AI reasoning exchanges for interpretability | Layer 5 – Reasoning Exchange |
| AEIP Frame | Packages deployment-ready payloads with manifest bindings | Layer 6 – Deployment & Integration |

## Workflow Overview

1. **Creation:** Layer-specific authorities generate AEIP-compliant artifacts (e.g., interpretive stewards issue ITPs) using the corresponding schemas, embedding UUID identifiers, UTC timestamps, and provenance metadata.
2. **Verification:** Governance infrastructure validates each artifact against its schema, confirms digital signatures, and checks cross-artifact linkages (e.g., DRRs must reference relevant ITPs or OAMs).
3. **Ledger Entry:** Once verified, an Integrity Ledger Entry notarizes the event by hashing the payload, recording the prior ledger UUID, and cataloguing linked artifacts to uphold temporal integrity.

## Citation and Licensing

All schema materials are © 2025 Daniel P. Madden and licensed under CC BY-NC-ND 4.0. Cite as: Madden, D. (2025). *AEIP Artifact Schemas for the AI OSI Stack v5*. Zenodo (forthcoming). Redistribution requires attribution, prohibits commercial use, and disallows derivative works without explicit authorization.
