# AI OSI Stack – Reference Implementation Toolkit

This repository transforms the conceptual **AI OSI Stack v4 (Test Integrated)** into a runnable, modular, and interoperable protocol suite.  Each AI OSI layer (L1–L7 plus optional L8) is implemented as an independently testable Python module with schema-backed validators, AEIP transport support, and governance ledger integration.

## Highlights

* **Layered Modules:** `src/layer*/` packages expose deterministic transforms, `dignity_compliance` toggles, and Interface Definition Documents (IDDs).
* **Protocol Spine:** `/protocol/aeip_handshake.py` implements the AEIP v1 five-step handshake (`Intent → Justify → CounterSign → Commit → Update`).
* **Governance Ledger Node:** `/protocol/ledger_node.py` launches a local daemon that verifies artifacts, validates signatures, and appends Integrated Ledger Entries (ILEs).
* **Artifact Schemas:** `/schemas/` publishes machine-readable JSON/YAML schemas for ITP, DRR, GDS, OAM, and ILE artifacts.
* **Conformance Testing:** `/tests/` delivers pytest suites for handshake integrity, layer contract validation, and artifact schema compliance.
* **Documentation:** `/docs/` contains the living AI OSI Protocol Specification, AEIP v1 spec, and the IDD guide with mermaid diagrams for rapid onboarding.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # optional if extra packages are added
pytest
python protocol/ledger_node.py  # start the governance node daemon
```

The ledger node listens on `http://0.0.0.0:8080/artifacts` and persists append-only entries in `/ledger/` while updating `protocol/registry_gns.yaml`.

## Repository Layout

```
/docs/                     → Living specifications and diagrams
/examples/                 → Jupyter notebooks demonstrating solo & multi-node flows
/protocol/                 → AEIP handshake implementation, ledger daemon, test vectors
/schemas/                  → Versioned artifact schemas (JSON + YAML)
/src/                      → Layer packages, common utilities, validators
/tests/                    → Pytest suites for protocol and schema conformance
/tools/                    → CLI helpers for artifact generation, validation, version checks
```

Historic materials (including `source/AI_OSI_Stack_v4_Test_Integrated.md`) remain for traceability and are referenced by the executable documentation.

## Licensing & Integrity

All materials are provided under **CC BY-NC-ND 4.0**.  Normative language and temporal governance clauses inherit from `INTEGRITY_NOTICE.md`.  Hashing is performed with SHA3-512 and placeholder Ed25519 signatures to enable deterministic testing while supporting production-ready upgrades.

For questions or governance contributions, submit an issue referencing the relevant ledger entry or contact the maintainers listed in `/docs/AI_OSI_Protocol_Spec.md`.
