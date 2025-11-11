---
Title: Semantic Version Control Guide
Version: 5.0.0
Status: Canonical Draft
License: CC BY-NC-ND 4.0
---

# Semantic Version Control (SVC) Guide

## Version Semantics
- **MAJOR** increments signify constitutional rewrites that alter civic mandates or AEIP fundamentals. All dependent layers MUST synchronize before release.
- **MINOR** increments capture additive capabilities, new clauses, or governance tooling that remain backward compatible. Downstream references SHOULD update within one publication cycle.
- **PATCH** increments codify errata, clarifications, and integrity corrections without altering obligations. Implementers MAY adopt immediately.

## Propagation Rules by Layer
- **Layers L0–L3**: MAJOR or MINOR updates SHALL trigger review of provenance statements and Governance Manifest alignment.
- **Layers L4–L6**: Changes MUST propagate to Persona Architecture, AEIP routing registries, and deployment checklists.
- **Layers L7–L8**: Publication cadence and civic participation frameworks SHOULD mirror version changes within thirty days.

## Cross-Document Traceability
- Each document SHALL reference its governing SVC identifier.
- Integrity Ledger entries MUST cite the semantic version and commit hash.
- Codex automation SHALL enforce schema validation against the declared SVC baseline.
