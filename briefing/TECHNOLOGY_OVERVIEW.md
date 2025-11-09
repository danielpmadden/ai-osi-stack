<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Technology Overview — AI OSI Stack v5

**Canonical anchors:** [README](../README.md), [docs/architecture-overview.md](../docs/architecture-overview.md), [docs/aeip-spec-v1-3.md](../docs/aeip-spec-v1-3.md), [docs/governance-dashboard/control-tower-readme.md](../docs/governance-dashboard/control-tower-readme.md), [docs/VERIFICATION_GUIDE.md](../docs/VERIFICATION_GUIDE.md), [audits/200-repo-wide-integrity-report.md](../audits/200-repo-wide-integrity-report.md).

## Layered Architecture

AI OSI Stack v5 organizes accountability into nine governance layers—Civic Mandate (Layer 0) through Civic Participation (Layer 8)—each with explicit duties, evidence artefacts, and oversight checkpoints ([README](../README.md)). The runtime reference (`govspine/`) mirrors these layers, supplying controls for data stewardship, persona instruction, reasoning exchange, and deployment governance ([docs/architecture-overview.md](../docs/architecture-overview.md)). Layer contracts connect directly to AEIP artefacts so every obligation can be traced to a signed manifest or ledger entry.

## AEIP Lifecycle

The AI Epistemic Infrastructure Protocol (AEIP) v1.3 governs how intents, justifications, counter-signatures, and ledger commits flow between personas and oversight bodies ([docs/aeip-spec-v1-3.md](../docs/aeip-spec-v1-3.md)). Its layered structure (Temporal, Provenance, Justification, Exchange, Governance, Audit, optional Reflection) ensures that:

1. Intents declare objectives, privacy posture, and governance scope.
2. Participants attach justifications and counter-factual evidence.
3. Counter-signatures bind agreements and update consent states.
4. Ledger commits record immutable hashes and drift signals.
5. Reflection entries capture lessons without altering prior obligations.

Lifecycle tooling includes schema validators, manifest generators, and dashboard flows that operationalize the handshake steps across distributed teams.

## Dashboard & Registry

The Governance Control Tower pairs a FastAPI API with a React dashboard to register assets, ingest AEIP manifests, and visualize audit telemetry ([docs/governance-dashboard/control-tower-readme.md](../docs/governance-dashboard/control-tower-readme.md)). Core views (asset registry, manifest crosswalk, resilience metrics) expose persona roles, custody status, and outstanding remediation tasks. Background jobs publish integrity summaries to `govspine/` manifests so registry records remain synchronized with canonical artefacts.

## Canonical Schemas & Tests

- **Schemas:** JSON-LD/YAML definitions for Decision Rationale Records, Governance Disclosure Statements, Integrity Ledger Entries, and Interpretive Trace Packages live under [`schemas/`](../schemas) with SPDX headers and canonical authorship statements.
- **Validation:** `npm run validate:aeip` and `npm run validate:governance` confirm schema conformance; `pytest` validates Python utilities; integrity inventories and SBOM scripts provide reproducibility checks ([docs/VERIFICATION_GUIDE.md](../docs/VERIFICATION_GUIDE.md)).
- **Audits:** Repository-wide integrity audits document findings across authorship, licensing, standards alignment, and security posture, informing remediation roadmaps ([audits/200-repo-wide-integrity-report.md](../audits/200-repo-wide-integrity-report.md)).

## Provenance & Deferred Signing

Provenance is enforced through canonical metadata (`CANONICAL_PROVENANCE.yaml`), advisory signing instructions (`INTEGRITY_NOTICE.md`), and custodial policies that bind releases to Daniel P. Madden’s authorship. Deferred signing acknowledges that cryptographic signatures publish once the v5 sealing ceremony completes; until then, integrity relies on reproducible manifests, checksum guidance, and advisory verification via `ops/release/verify.sh`. This approach balances transparency with custodial control, ensuring organizations can audit artefacts today while preparing for full signature-backed validation tomorrow.
