© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
# AI OSI Stack v5 — Full Repository Audit & Context Report

## 1. Context: Who, What, When, Why, How

### Who
- **Primary steward:** Daniel P. Madden maintains authorship, provenance, and release duties; canonical provenance files, manifest metadata, and README reiterate sole authorship and absence of institutional backing.【F:CANONICAL_PROVENANCE.yaml†L1-L10】【F:README.md†L1-L24】【F:meta/README.md†L1-L40】
- **Intended users:** Policy teams, compliance officers, civic technologists, and AI governance engineers seeking an auditable governance spine for AI systems, with documentation oriented to professionals comfortable with legal, civic, and technical terminology.【F:docs/LEGAL-AND-POLICY-BRIEF.md†L1-L57】【F:README.md†L25-L87】
- **Contributors & maintainers:** Contributions are tightly controlled, requiring DCO sign-off, SBOM regeneration, and integrity updates; the project anticipates highly disciplined maintainers familiar with both Python and TypeScript tooling.【F:CONTRIBUTING.md†L5-L44】

### What
- **Repository purpose:** Implements the AI OSI governance stack as both documentation and executable reference, covering layered governance models, AEIP schemas, runtime validators, dashboards, and audits.【F:README.md†L25-L125】【F:govspine/readme.md†L1-L18】
- **Problem solved:** Provides a reproducible, verifiable governance blueprint that links civic mandates to operational controls and evidence artefacts for AI deployments.【F:README.md†L25-L70】【F:docs/LEGAL-AND-POLICY-BRIEF.md†L12-L47】
- **Architectural intent:** Mirror the OSI model with nine layers (0–8) plus interpretive canon, binding normative duties to machine-verifiable artefacts and runtime enforcement points.【F:meta/README.md†L24-L71】【F:govspine/runtime/common/layer.py†L1-L44】

### When
- **Creation & cadence:** Canonical manifest dated 9 Nov 2025 for v5.0; release assets and metadata share that timestamp, indicating active maintenance into late 2025.【F:meta/v5-manifest.yaml†L1-L36】
- **Recent activity:** Audit bundle and manifest highlight repository-wide integrity checks aligned with v5 release cycle, implying maintenance around the same window.【F:audits/200-repo-wide-integrity-report.md†L1-L116】
- **Operational timing:** Runtime layers process payloads sequentially in a pipeline; AEIP receipts follow defined lifecycle transitions for compliance events.【F:tests/test_layer_contracts.py†L1-L52】【F:tests/aeip-lifecycle-validator.py†L1-L88】

### Why
- **Motivation:** Address regulatory lag by providing a structured, evidence-backed governance architecture that regulators, civic bodies, and technologists can adopt.【F:README.md†L25-L70】【F:docs/LEGAL-AND-POLICY-BRIEF.md†L12-L57】
- **Technology choices:** Python for canonical runtime and schema validation (aligns with governance and automation workflows), TypeScript/React for dashboard accessibility, JSON-LD/YAML for provenance-friendly artefacts; choices emphasise auditability and portability.【F:requirements.txt†L1-L4】【F:package.json†L1-L29】【F:dashboard/package.json†L1-L45】
- **Structure:** Maintains clear separation between normative texts (`source/`), schemas (`schemas/`), runtime library (`govspine/`), and public interface (`dashboard/`), enabling independent verification and publication.【F:govspine/readme.md†L1-L18】【F:docs/LEGAL-AND-POLICY-BRIEF.md†L58-L71】

### How
- **End-to-end flow:** Civic mandates and normative clauses live in LaTeX chapters (`source/`). AEIP schemas define evidence structures (`schemas/`). Runtime layers load schemas/contracts, process payloads, and compute hashes (`govspine/runtime`). Tests exercise AEIP lifecycle and layer chaining (`tests/`). Dashboards present governance receipts (`dashboard/`). Integrity metadata and audits ensure provenance (`meta/`, `audits/`).【F:govspine/runtime/common/schema.py†L1-L78】【F:govspine/runtime/layer5-interface/__init__.py†L1-L40】【F:tests/test_layer_contracts.py†L1-L52】【F:dashboard/README.md†L1-L64】【F:meta/v5-manifest.yaml†L1-L40】
- **Developer interaction:** Install Python deps for runtime validators, run pytest/ops scripts, use npm/Vite for dashboard, regenerate documents via LaTeX and ops tooling, follow integrity updates per CONTRIBUTING.【F:CONTRIBUTING.md†L9-L38】【F:dashboard/README.md†L5-L64】

## 2. Directory Tree & Purpose Map

```
.
├── README.md – Canonical overview, architecture, motivation.
├── CANONICAL_PROVENANCE.yaml – Authoritative authorship metadata.
├── CONTRIBUTING.md – Contribution, integrity, and workflow rules.
├── SECURITY.md – Vulnerability reporting and integrity policy.
├── requirements.txt – Python runtime dependencies.
├── package.json – Root TypeScript/Node tooling for AEIP ops.
├── Dockerfile / docker-compose.yml – Containerized runtime/test scaffolds.
├── audits/
│   └── 200-repo-wide-integrity-report.md – Comprehensive integrity audit.
├── dashboard/
│   ├── README.md – Dashboard workspace quickstart.
│   ├── package.json – React/Vite tooling.
│   ├── src/ – Civic dashboard components, data, tests, stories.
│   ├── scripts/ – Data validation tooling for dashboard payloads.
│   └── docs/ – Dashboard-specific documentation.
├── docs/
│   ├── LEGAL-AND-POLICY-BRIEF.md – Outreach summary for policymakers.
│   ├── standards-alignment-brief.md – Standards crosswalk.
│   └── (new) REPOSITORY-AUDIT.md – This audit report.
├── examples/
│   └── aeip/ – Sample AEIP receipts consumed by validators/tests.
├── govspine/
│   ├── runtime/ – Canonical Python implementation of governance layers.
│   ├── common/ – Import bridges delegating to runtime modules.
│   ├── layer01physical … layer08policy – Layer entry points.
│   ├── aeip/, charters/, control/, etc. – Evidence stores per layer.
│   └── readme.md – Structure of evidence store.
├── legal/, commercial/, press-kit/ – Public-facing collateral and disclosures.
├── meta/
│   ├── README.md – Canonical narrative/architecture summary.
│   ├── v5-manifest.yaml – Release manifest and hashes.
│   └── INTEGRITY_NOTICE.md, CHANGELOG.md, etc. – Integrity collateral.
├── protocol/ – Governance protocol references and registries.
├── schemas/
│   ├── aeip/ – JSON/JSON-LD schemas for AEIP artefacts.
│   ├── persona/, therapy/, svc/ – Specialized schema domains.
│   └── readme.md – Schema usage guidance.
├── source/
│   ├── chapters/, appendices/, backmatter/ – LaTeX canonical text.
│   └── interpretive/ – Interpretive canon sources.
├── tests/
│   ├── test_layer_contracts.py – Layer pipeline tests.
│   ├── aeip-lifecycle-validator.py – AEIP lifecycle validation suite.
│   └── ops/ – Operational validation scripts.
├── tools/
│   └── verify-aeip-signatures.py – Deprecated signing helper (advisory notice).
├── ops/
│   ├── aeip/, inventory/, sbom/, secrets/ – Operational scripts and workflows.
│   └── .github/ – CI workflows relocated for organization.
└── versions/
    └── ai-osi-stack-v5.pdf – Canonical compiled publication.
```

**Folder responsibilities**
- **audits/** — Stores integrity and compliance findings that inform modernization priorities.【F:audits/200-repo-wide-integrity-report.md†L1-L196】
- **dashboard/** — Public interface for governance evidence, with accessibility tests and data validation routines.【F:dashboard/README.md†L5-L64】【F:dashboard/src/__tests__/a11y.spec.tsx†L1-L20】
- **docs/** — Context briefs bridging legal, policy, and standards audiences.【F:docs/LEGAL-AND-POLICY-BRIEF.md†L1-L71】【F:docs/standards-alignment-brief.md†L1-L37】
- **govspine/** — Python runtime, bridging modules, and evidence stores aligning runtime logic with canonical schemas.【F:govspine/runtime/common/schema.py†L1-L78】【F:govspine/runtime/layer5-interface/__init__.py†L1-L40】
- **meta/** — Maintains canonical manifest, integrity notices, and release metadata for provenance assurance.【F:meta/v5-manifest.yaml†L1-L45】
- **schemas/** — Houses machine-verifiable contracts for AEIP artefacts and layer interactions.【F:docs/standards-alignment-brief.md†L1-L37】
- **tests/** — Validates AEIP lifecycle discipline and layer interoperability to guard against governance regressions.【F:tests/test_layer_contracts.py†L1-L52】【F:tests/aeip-lifecycle-validator.py†L1-L120】
- **tools/** — Operational scripts, including deprecation notices for signing flows, signposting modernization gaps.【F:tools/verify-aeip-signatures.py†L1-L18】

## 3. High-Level Architecture Summary

### Plain-language overview
The stack codifies a civic-to-technical pipeline: public mandates (Layer 0) become ethical charters, data controls, model governance, operational instructions, interface envelopes, deployment policies, publication artefacts, and civic participation feedback. Evidence is captured through AEIP receipts validated by Python runtime and surfaced via a React dashboard.【F:README.md†L25-L125】【F:govspine/runtime/layer5-interface/__init__.py†L1-L40】【F:dashboard/README.md†L5-L64】

### Technical overview
- **Runtime layers:** `govspine/runtime` defines `BaseLayer` classes enforcing schema contracts and dignity compliance, with per-layer validators performing hashing, sealing, and persona checks.【F:govspine/runtime/common/layer.py†L1-L44】【F:govspine/runtime/layer6-application/validator.py†L1-L23】
- **Schemas:** JSON/JSON-LD definitions stored in `schemas/` drive contract loading and payload validation, enabling `InterfaceContract` objects to guard cross-layer exchanges.【F:govspine/runtime/common/interface.py†L1-L32】【F:docs/standards-alignment-brief.md†L1-L37】
- **Artifacts:** `Artifact` dataclass wraps payloads with deterministic hashing and optional persona signatures, providing extendable integrity enforcement.【F:govspine/runtime/common/artifacts.py†L1-L71】
- **Dashboard:** Vite/React app consumes curated JSON data to visualize governance layers and AEIP logs while enforcing accessibility with `vitest-axe`.【F:dashboard/README.md†L5-L64】【F:dashboard/src/__tests__/a11y.spec.tsx†L1-L20】
- **Ops & audits:** `ops/` scripts produce SBOMs, inventory, and integrity notices; `audits/` documents external verification findings guiding release governance.【F:CONTRIBUTING.md†L13-L32】【F:audits/200-repo-wide-integrity-report.md†L1-L196】

### Module interactions & data flow
1. **Input:** AEIP receipts and governance payloads authored per schema (`schemas/aeip/*.json`).
2. **Validation:** Runtime layers load interface contracts, validate payloads, compute seals/hashes, and propagate enriched envelopes downstream (`govspine/runtime/common`).【F:govspine/runtime/common/schema.py†L1-L78】【F:govspine/runtime/layer5-interface/__init__.py†L18-L40】
3. **Lifecycle checks:** Test suites ensure AEIP receipts traverse mandated lifecycle states and layer outputs satisfy contracts (`tests/`).【F:tests/aeip-lifecycle-validator.py†L41-L120】【F:tests/test_layer_contracts.py†L19-L52】
4. **Publication:** Dashboard ingests validated JSON for visualization; `versions/` stores compiled PDF for canonical reference.【F:dashboard/README.md†L21-L52】【F:versions/ai-osi-stack-v5.pdf†L1-L1】
5. **Governance metadata:** `meta/` holds manifest hashes and provenance statements, cross-referenced by audits for integrity narratives.【F:meta/v5-manifest.yaml†L1-L45】【F:audits/200-repo-wide-integrity-report.md†L1-L196】

### External dependencies
- Python: `jsonschema`, `pytest` for testing & validation scaffolding.【F:requirements.txt†L1-L4】
- Node/TypeScript: `ajv` for schema validation, Vite/Vitest for dashboard build & tests.【F:package.json†L15-L29】【F:dashboard/package.json†L9-L45】
- Tooling: SBOM, inventory, secrets scans orchestrated via `ops/` scripts requiring external CLIs (Syft, Trivy, Gitleaks).【F:CONTRIBUTING.md†L13-L32】

### Text-based flow diagram
```
Civic Mandate (Layer 0 text, schemas) → Ethical Charter (Layer 1) →
Data Stewardship (Layer 2) → Model Development (Layer 3) → Instruction & Control (Layer 4) →
Interface Enveloping (Layer 5) → Deployment Governance (Layer 6) →
Governance Publication (Layer 7) → Civic Participation (Layer 8)
            ↓                                        ↑
       AEIP Schemas & Receipts  ← Runtime validation ← Tests & Ops checks
            ↓                                        ↑
      Dashboard visualisation ← curated JSON data ← Ops/Examples/AEIP receipts
```

## 4. Working Components
- **Layer processing pipeline** validated end-to-end via `test_layer_contracts.py`, confirming contracts and dignity seals propagate through eight layers.【F:tests/test_layer_contracts.py†L1-L52】
- **AEIP lifecycle validators** enforce privacy, provenance, uncertainty bounds, signature placeholders, and ordering, providing reliable governance receipt checks.【F:tests/aeip-lifecycle-validator.py†L1-L120】
- **Runtime schema loaders** gracefully handle JSON/YAML, compute hash validations, and support persona signatures, offering a solid backbone for future cryptographic upgrades.【F:govspine/runtime/common/schema.py†L1-L78】【F:govspine/runtime/common/artifacts.py†L1-L71】
- **Dashboard accessibility testing** uses `vitest-axe` to prevent regressions in civic interface components.【F:dashboard/src/__tests__/a11y.spec.tsx†L1-L20】
- **Manifest metadata** enumerates release moves, hash references, and integrity guidance, providing traceable provenance for canonical assets.【F:meta/v5-manifest.yaml†L1-L55】

## 5. Broken / Missing / Risky Components
- **Provenance propagation gaps:** Audit highlights missing authorship metadata in distributed assets such as dashboard HTML and AEIP schemas, risking provenance drift.【F:audits/200-repo-wide-integrity-report.md†L7-L32】
- **Dual-license compliance:** `meta/license.txt` lacks Apache-2.0 text; numerous assets miss SPDX tags, undermining legal clarity.【F:audits/200-repo-wide-integrity-report.md†L9-L40】
- **Standards verifiability:** Standards brief relies on “implied/contextual” references without clause IDs, weakening regulatory mapping.【F:docs/standards-alignment-brief.md†L1-L37】
- **Manifest hashing gaps:** Release manifest still lists `TO_BE_DETERMINED` commit and hashes only subset of assets, limiting deterministic verification.【F:meta/v5-manifest.yaml†L1-L45】
- **Appendix O corruption:** Broken macros degrade normative clarity and may break LaTeX builds, creating compliance ambiguity.【F:audits/200-repo-wide-integrity-report.md†L23-L76】
- **Cryptography placeholders:** Deterministic persona signatures and deprecated signing script provide advisory-only guarantees, insufficient for production security.【F:govspine/runtime/common/crypto.py†L1-L52】【F:tools/verify-aeip-signatures.py†L1-L18】
- **Accessibility documentation gap:** Required accessibility checklist absent despite automated tests.【F:audits/200-repo-wide-integrity-report.md†L60-L70】

## 6. Code Quality Analysis
- **Structure & organization:** Clear separation between runtime, schemas, documentation, dashboard, and ops tooling promotes modular governance flows.【F:govspine/readme.md†L1-L18】【F:docs/LEGAL-AND-POLICY-BRIEF.md†L58-L71】
- **Naming & clarity:** Layer modules and schema files use explicit OSI-aligned naming (`Layer5Interface`, `governance-decision-summary`), aiding readability.【F:govspine/runtime/layer5-interface/__init__.py†L1-L40】
- **Reusability & abstraction:** `BaseLayer`, `InterfaceContract`, and `Artifact` abstractions provide extensible hooks for future governance logic; dynamic module bridges keep runtime code centralized.【F:govspine/runtime/common/layer.py†L1-L44】【F:govspine/common/layer.py†L1-L27】
- **Coupling/cohesion:** Layer modules depend on shared schema/crypto utilities, maintaining cohesion around AEIP contracts while minimizing duplication.【F:govspine/runtime/common/schema.py†L1-L78】
- **Documentation & comments:** Rich README, briefs, and audits supply context; code modules emphasise docstrings over inline comments, adequate for current scope.【F:README.md†L1-L125】【F:audits/200-repo-wide-integrity-report.md†L1-L196】
- **Maintainability:** Tests enforce critical invariants; however, manual manifest updates and placeholder cryptography require disciplined maintenance to avoid drift.【F:meta/v5-manifest.yaml†L1-L45】【F:govspine/runtime/common/crypto.py†L1-L52】

## 7. Technology Stack & Tooling
- **Languages:** Python (runtime, tests, ops), TypeScript/React (dashboard), LaTeX (canonical text), JSON/JSON-LD/YAML (schemas, manifests).【F:govspine/runtime/common/schema.py†L1-L78】【F:dashboard/package.json†L1-L45】【F:source/chapters/generated/layer1-control-table.tex†L1-L23】
- **Frameworks & libraries:** Pytest, custom schema validation, AJV, Vite, Vitest, Storybook, vitest-axe.【F:requirements.txt†L1-L4】【F:package.json†L15-L29】【F:dashboard/package.json†L9-L45】
- **Build & tooling:** npm scripts for lint/test/validate, ops scripts for SBOM/secrets/inventory, Dockerfiles for reproducible builds, LaTeX toolchain for PDF generation.【F:dashboard/README.md†L5-L64】【F:CONTRIBUTING.md†L13-L32】
- **CI/CD:** Workflows relocated under `ops/.github/`; not inspected here but referenced for automation of manifests and dashboards.【F:govspine/readme.md†L15-L18】
- **Deployment:** Dashboard uses Docker + Nginx; runtime packaged as Python library for integration into AI pipelines.【F:dashboard/README.md†L67-L87】【F:README.md†L100-L125】

### Rationale for choices
- **Python** ensures accessibility for governance teams and integrates with compliance tooling; deterministic hashing fosters reproducibility.【F:govspine/runtime/common/schema.py†L1-L78】
- **TypeScript/React** provides rich UI for civic oversight, with strong accessibility tooling aligning with civic accountability goals.【F:dashboard/README.md†L33-L64】
- **JSON-LD/YAML** suits machine-readable provenance and legal crosswalk requirements, enabling AEIP interoperability.【F:docs/standards-alignment-brief.md†L1-L37】

## 8. Security, Reliability & Performance Audit
- **Hardcoded secrets:** None detected; ops scripts reference external secret scanning expectations.【F:CONTRIBUTING.md†L24-L32】
- **Cryptography gaps:** Persona signatures are deterministic, lacking real key management; signing script emits advisory notice only—risk for tampering.【F:govspine/runtime/common/crypto.py†L19-L52】【F:tools/verify-aeip-signatures.py†L1-L18】
- **Input validation:** Schemas enforce required fields and types; payload validation allows extensibility but may accept unknown keys, trading strictness for flexibility.【F:govspine/runtime/common/schema.py†L25-L71】
- **Hash integrity:** Layers compute SHA3-512 digests for envelopes and payloads, ensuring tamper detection, but reliance on deterministic JSON stringification may diverge if payload ordering changes externally.【F:govspine/runtime/layer5-interface/__init__.py†L28-L37】【F:govspine/runtime/common/artifacts.py†L20-L40】
- **Performance considerations:** Schema validation loops are linear over payload size; AEIP lifecycle validators iterate over small sample sets—no immediate bottlenecks detected.【F:tests/aeip-lifecycle-validator.py†L1-L88】
- **Reliability risks:** Manual manifest updates and placeholder TODOs (dashboard API integration) present operational risk if not synchronised with production pipelines.【F:meta/v5-manifest.yaml†L1-L45】【F:dashboard/README.md†L90-L99】
- **Security posture:** Security policy defines disclosure process but references pending PGP fingerprint; absence of sealed signing keys leaves supply-chain verification incomplete.【F:SECURITY.md†L5-L33】

## 9. Modernization Roadmap

### Short-Term (0–30 days)
- Patch Appendix O macros and regenerate PDFs to restore normative clarity and compile reliability.【F:audits/200-repo-wide-integrity-report.md†L23-L76】
- Embed canonical authorship metadata into non-commentable assets and extend linting/tests to enforce presence.【F:audits/200-repo-wide-integrity-report.md†L7-L32】
- Publish missing Apache-2.0 license text and inject SPDX/license metadata into JSON/YAML artefacts during export.【F:audits/200-repo-wide-integrity-report.md†L9-L40】
- Finalize manifest hashes, including release commit ID and coverage for all canonical artefacts; document reproduction commands.【F:meta/v5-manifest.yaml†L1-L45】
- Draft `docs/accessibility-checklist.md` summarizing automated + manual results to satisfy audit expectations.【F:audits/200-repo-wide-integrity-report.md†L60-L70】

### Mid-Term (1–3 months)
- Replace deterministic persona signatures with proper Ed25519 or similar library, introducing key management guidance and verification tooling.【F:govspine/runtime/common/crypto.py†L19-L52】
- Reintroduce signing workflow or integrate hardware-backed keys; update `tools/verify-aeip-signatures.py` to perform real checks.【F:tools/verify-aeip-signatures.py†L1-L18】
- Expand standards crosswalk with clause-level citations and link to automated compliance checks (e.g., tests verifying required schema fields).【F:docs/standards-alignment-brief.md†L1-L37】
- Automate manifest generation via CI to reduce manual risk; include release commit resolution and hash verification tasks.【F:meta/v5-manifest.yaml†L1-L45】
- Build dashboard integration stubs for live AEIP/governance APIs once ratified, ensuring data ingestion layers apply schema validation server-side as well.【F:dashboard/README.md†L90-L99】

### Long-Term (3–6 months)
- Establish end-to-end supply-chain security: reproducible LaTeX builds (containerized), release signing, verifiable SBOM publication, and ledger-backed AEIP registries.【F:CONTRIBUTING.md†L13-L32】【F:meta/v5-manifest.yaml†L1-L55】
- Introduce governance simulation pipelines bridging `tests/governance-simulation` and runtime to stress-test incident response and policy update flows.【F:tests/governance-simulation†L1-L1】
- Expand dashboard to support participatory feedback (Layer 8) with secure submission workflows, integrating privacy controls and audit logging.
- Create automated provenance injection tooling for schema/doc exports to prevent future drift; integrate with CI gating.
- Formalize continuous compliance metrics (e.g., coverage over AEIP fields, normative clause tracking) and publish as part of governance dashboards.

## 10. Developer Onboarding Guide

### Understand the repo in 10 minutes
1. Read `README.md` for architecture layers and motivation.【F:README.md†L1-L125】
2. Skim `meta/README.md` and `docs/LEGAL-AND-POLICY-BRIEF.md` for governance context and intended audiences.【F:meta/README.md†L1-L71】【F:docs/LEGAL-AND-POLICY-BRIEF.md†L1-L57】
3. Review `govspine/runtime/common` modules (`layer.py`, `schema.py`, `artifacts.py`) to grasp runtime patterns.【F:govspine/runtime/common/layer.py†L1-L44】【F:govspine/runtime/common/schema.py†L1-L78】【F:govspine/runtime/common/artifacts.py†L1-L71】
4. Inspect `tests/test_layer_contracts.py` and `tests/aeip-lifecycle-validator.py` to see expected behaviors.【F:tests/test_layer_contracts.py†L1-L52】【F:tests/aeip-lifecycle-validator.py†L1-L120】
5. Glance at `dashboard/README.md` to understand the UI layer and data expectations.【F:dashboard/README.md†L5-L64】

### Run the project locally
1. **Runtime validators:**
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   pytest
   ```
   (ensures schema validations and lifecycle tests pass).【F:requirements.txt†L1-L4】【F:tests/test_layer_contracts.py†L1-L52】
2. **Dashboard:**
   ```bash
   cd dashboard
   npm install
   npm run validate:data
   npm run dev
   ```
   (validates data, runs Vite dev server).【F:dashboard/README.md†L9-L33】
3. **Ops tooling:** run inventory/SBOM/secrets scripts per CONTRIBUTING to mirror release hygiene.【F:CONTRIBUTING.md†L13-L32】

### How to contribute
- Fork + feature branch, run required checks (npm lint/test, pytest, ops scripts), update integrity notices, sign commits with DCO.【F:CONTRIBUTING.md†L9-L38】
- Coordinate provenance changes by updating manifest and INTEGRITY_NOTICE per release instructions.【F:meta/v5-manifest.yaml†L1-L45】

### Gotchas & hidden complexities
- **Dynamic module bridging:** `govspine/common` modules proxy to runtime files; ensure edits occur under `govspine/runtime` to avoid duplication.【F:govspine/common/layer.py†L1-L27】
- **Deterministic hashing:** Payload canonicalization relies on sorted JSON dumps—mutating serialization strategy can break hash comparisons.【F:govspine/runtime/common/artifacts.py†L20-L40】
- **Placeholder cryptography:** Persona signatures and signing scripts are advisory; deployments must integrate real key management.【F:govspine/runtime/common/crypto.py†L19-L52】【F:tools/verify-aeip-signatures.py†L1-L18】
- **Documentation licensing:** Dual-license expectations require careful SPDX tagging when adding assets outside text-friendly formats.【F:audits/200-repo-wide-integrity-report.md†L7-L40】
- **LaTeX build sensitivity:** Broken macros (Appendix O) can fail builds; ensure TeX updates align with audit fixes.【F:audits/200-repo-wide-integrity-report.md†L23-L76】

### Key files to read first
- `README.md`, `meta/README.md` — conceptual architecture.【F:README.md†L1-L125】【F:meta/README.md†L1-L71】
- `govspine/runtime/common` modules — runtime core.【F:govspine/runtime/common/layer.py†L1-L44】【F:govspine/runtime/common/schema.py†L1-L78】
- `audits/200-repo-wide-integrity-report.md` — outstanding compliance issues.【F:audits/200-repo-wide-integrity-report.md†L1-L196】
- `CONTRIBUTING.md`, `SECURITY.md` — process and disclosure expectations.【F:CONTRIBUTING.md†L5-L44】【F:SECURITY.md†L5-L33】

### Mental model for development
Visualize the repository as a layered civic OSI model: normative texts define duties → schemas encode duties → runtime enforces duties → dashboards publish evidence → ops/audits guarantee provenance. Every change should maintain traceability across this chain.【F:README.md†L25-L125】【F:govspine/runtime/common/artifacts.py†L1-L71】【F:dashboard/README.md†L5-L64】【F:meta/v5-manifest.yaml†L1-L45】
