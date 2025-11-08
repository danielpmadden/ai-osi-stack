<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

<!--
Title: AEIP Schema Catalogue Overview
Version: 1.0.0
Date: 2025-05-09T00:00:00Z
Author: Repository Architect
License: CC BY-SA 4.0
Signature: Pending governance signature
-->

# AEIP Schema Catalogue — AEIP-Schema-1.0-2025-11

**Integrity Notice:** Version hash: TBD. Generated on 2025-05-09T00:00:00Z.

## Purpose

This catalogue enumerates the AEIP artifact schemas that safeguard interoperability, temporal integrity, and ethical accountability across the AI OSI Stack v4. Each schema is authored in JSON-LD and aligned with AEIP-Schema-1.0-2025-11 to guarantee machine-readable conformance and governance traceability.

## Artifact Purposes and Layer Mappings

| Artifact Type | Governance Purpose | Primary AI OSI Layer Alignment |
| --- | --- | --- |
| Interpretive Trace Package (ITP) | Captures interpretive reasoning chains and evidence supporting model understanding | Layer 3 – Interpretability and Transparency |
| Decision Rationale Record (DRR) | Documents deliberative justification for governance determinations | Layer 4 – Governance Decision Authority |
| Governance Decision Summary (GDS) | Communicates finalized governance outcomes and mandated actions | Layer 5 – Operationalization and Change Management |
| Oversight Audit Memo (OAM) | Records oversight findings, assurance results, and remediation directives | Layer 6 – Oversight and Assurance |
| Integrity Ledger Entry (ILE) | Notarizes governance events with temporal sequencing and cryptographic assurance | Layer 7 – Integrity and Continuity |

## Workflow Overview

1. **Creation:** Layer-specific authorities generate AEIP-compliant artifacts (e.g., interpretive stewards issue ITPs) using the corresponding JSON-LD schemas, embedding UUIDv4 identifiers, UTC timestamps, and provenance metadata.
2. **Verification:** Governance infrastructure validates each artifact against its schema, confirms digital signatures, and checks cross-artifact linkages (e.g., DRRs must reference relevant ITPs or OAMs).
3. **Ledger Entry:** Once verified, an Integrity Ledger Entry notarizes the event by hashing the payload, recording the prior ledger UUID, and cataloguing linked artifacts to uphold temporal integrity.

## Citation and Licensing

All schema materials are © 2025 Daniel P. Madden and licensed under CC BY-SA 4.0. Cite as: Madden, D. (2025). *AEIP Artifact Schemas for the AI OSI Stack v4*. Zenodo (forthcoming). Redistribution requires attribution, prohibits commercial use, and disallows derivative works without explicit authorization.
