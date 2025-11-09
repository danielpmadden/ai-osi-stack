SPDX-License-Identifier: CC-BY-SA-4.0
Author: Daniel P. Madden
Title: Repository Structure & Continuity Audit (AI OSI Stack v5.0)
Date: 2025-11-08

## Section 1 — Canonical Tree Overview
```
ai-osi-stack/
├── .github/ (canonical) – CI/CD workflows and templates
│   └── workflows/ (canonical) – automated lint, audit, and release pipelines
├── .storybook/ (review) – legacy Storybook configuration awaiting dashboard alignment
├── audit/ (redundant) – legacy integrity report duplicate of /audits/
├── audits/ (canonical) – primary repository audits and integrity reports
├── commercial/ (canonical) – contracting templates and commercial policy artefacts
├── dashboard/ (canonical) – React governance dashboard implementation
│   ├── .husky/ (generated) – local git hooks for dashboard contributors
│   ├── docs/ (review) – dashboard-local notes overlapping with /docs/dashboard/
│   ├── ops/scripts/ (canonical) – dashboard validation and tooling utilities
│   └── src/ (canonical) – frontend source (components, data, stories, styles, utils)
├── docs/ (canonical) – standards crosswalks, guidance, and narrative documentation
│   ├── charter/ (canonical) – charter history and adoption materials
│   ├── crosswalks/ (canonical) – regulatory and policy alignment matrices
│   ├── dashboard/ (review) – dashboard planning artefacts duplicating /analytics/dashboard/docs/
│   ├── diagrams/ (canonical) – architecture and process diagrams
│   ├── examples/ (canonical) – reference walkthroughs and exemplars
│   ├── governance/ (canonical) – governance frameworks and board materials
│   ├── governance-dashboard/ (review) – transitional notes overlapping dashboard folders
│   ├── public-disclosures/ (canonical) – transparency and disclosure packages
│   └── verify/ (canonical) – verification procedures and checklists
├── govspine/ (canonical) – Python AEIP runtime, reference layers, and operational playbooks
│   ├── aeip/ (canonical) – AEIP interface definitions
│   ├── charters/ (canonical) – governance charter source files
│   ├── common/ (canonical) – shared utilities across runtime layers
│   ├── compute/ (canonical) – computational workflows and pipelines
│   ├── control/ (canonical) – control mechanisms and escalation scripts
│   ├── data/ (canonical) – data management and lineage tooling
│   ├── deployments/ (canonical) – deployment runbooks and timelines
│   ├── incidents/ (canonical) – incident response narratives
│   ├── layer01physical/ (canonical) – physical infrastructure specifications
│   ├── layer02architecture/ (canonical) – architecture-level governance guides
│   ├── layer03training/ (canonical) – training governance and audit plans
│   ├── layer04instruction/ (canonical) – instruction and oversight procedures
│   ├── layer05interface/ (canonical) – interface, access, and exchange controls
│   ├── layer06application/ (canonical) – application integration standards
│   ├── layer07governance/ (canonical) – governance board operations
│   ├── layer08policy/ (canonical) – policy harmonization guidance
│   ├── models/ (canonical) – model cards and configuration manifests
│   ├── postmortems/ (canonical) – retrospectives and post-incident analyses
│   └── runtime/ (canonical) – runtime orchestration and support scripts
├── ledger/ (canonical) – canonical ledgers and interpretive manifests
│   ├── hermeneutic/ (canonical) – interpretive record exemplars
│   ├── integrity/ (canonical) – integrity manifests and attestations
│   └── meta-audit/ (canonical) – meta-audit continuity manifests
├── legal/ (canonical) – legal notices, agreements, and compliance summaries
├── meta/ (review) – release manifests and maturity data overlapping versions/
├── ops/ (review) – build/devops stubs duplicating top-level automation
│   └── .github/workflows/ (redundant) – workflows duplicating root CI definitions
├── press-kit/ (canonical) – outreach collateral and media assets
│   └── media-assets/ (canonical) – press imagery placeholders and metadata
├── protocol/ (canonical) – AEIP transport specification and interoperability guides
│   └── test-vectors/ (canonical) – protocol test vectors and validation assets
├── schemas/ (canonical) – JSON/YAML schemas and linked data artefacts
│   ├── aeip/ (canonical) – AEIP-specific schema bundles
│   ├── governance/ (canonical) – governance process schemas
│   ├── persona/ (canonical) – persona definition schemas
│   ├── svc/ (canonical) – service catalogue schemas
│   └── therapy/ (canonical) – therapeutic governance schemas
├── ops/scripts/ (canonical) – automation scripts for audits and document generation
├── source/ (canonical) – LaTeX master specification
│   ├── appendices/ (canonical) – appendices including generated tables
│   │   └── generated/ (generated) – auto-built tables and schema registries
│   ├── backmatter/ (canonical) – indexes, references, and closing matter
│   ├── chapters/ (canonical) – layer chapters and narratives
│   ├── frontmatter/ (canonical) – title, preface, and verification preamble
│   ├── interpretive/ (canonical) – interpretive companion chapters
│   └── templates/ (canonical) – reusable LaTeX templates
├── tests/ (canonical) – validation and simulation suites
│   └── governance-simulation/ (canonical) – governance scenario tests
├── tools/ (canonical) – automation utilities and support apps
│   ├── control-tower/ (canonical) – oversight orchestration tool (backend/frontend)
│   └── governance/ (canonical) – governance-specific CLI utilities
├── versions/ (canonical) – compiled releases and historical plans
│   ├── historical/ (review) – legacy update plans pending consolidation
│   └── release/ (generated) – compiled TEX outputs for distribution
└── .git/ (generated) – git object store and repository metadata
```

## Section 2 — Redundant / Conflicting Directories
- `audit/`: redundant; migrate the integrity report pair into `/audits/` and remove the folder.
- `docs/dashboard/` vs `analytics/dashboard/docs/`: duplicated dashboard planning notes; converge into a single documentation path under `/docs/dashboard/`.
- `ops/.github/workflows/`: redundant with root `.github/workflows/`; de-duplicate CI workflows at the repository root.
- `versions/historical/`: overlaps with planning notes in `/docs/governance/`; determine authoritative home and merge accordingly.
- `meta/` vs `versions/`: both store release manifests; consolidate structured release data into one canonical location.

## Section 3 — Misplaced or Orphan Files
- `docs/dashboard/data-model-schema.json`: schema asset should live under `/schemas/dashboard/` (new folder) with docs referencing it.
- `protocol/public-keys.json`: relocate alongside protocol artefacts under `/protocol/` to align with transport/key distribution guidance.
- `meta/zenodo-metadata.yaml`: move to `/meta/` or `/versions/` with other release metadata manifests.
- `ops/makefile`: relocate into `/tools/` or `/ops/scripts/` to centralize automation entrypoints.
- `meta/layer-control-tables.json`: generated table aligns with `/source/appendices/generated/`; move there with accompanying build note.
- `analytics/dashboard/docs/`: fold into `/docs/dashboard/` to avoid split ownership of product documentation.

## Section 4 — Generated / Build Artefacts
- `source/appendices/generated/*.tex`: automatically produced tables; ensure build tooling writes to `/source/appendices/generated/` (current path is correct).
- `audits/82-tex-build-summary.md`, `audits/ai-osi-stack-v5-plaintext.txt`: generated audit/build outputs; consider relocating recurring build artefacts into a dedicated `/build/` tree.
- `meta/layer-control-tables.json`, `meta/v5-maturity.json`: generated release metrics; document provenance and/or relocate to `/build/metrics/`.
- `versions/ai-osi-stack-v5.pdf`, `versions/release/*.tex`: compiled specification outputs; stage future builds under a `/build/releases/` namespace with published copies mirrored in `/versions/`.
- `analytics/dashboard/.husky/` hooks: generated by frontend tooling; guard against committing tool-generated binaries and document regeneration steps.

## Section 5 — Recommendations Summary
- [ ] Delete `/audit/` folder after migrating contents into `/audits/`.
- [ ] Merge dashboard documentation into `/docs/dashboard/` and remove `/analytics/dashboard/docs/`.
- [ ] Relocate schema JSON assets (`docs/dashboard/data-model-schema.json`) into a new `/schemas/dashboard/` directory.
- [ ] Move release metadata files (`meta/zenodo-metadata.yaml`, `protocol/public-keys.json`) into `/meta/` or `/protocol/` as appropriate.
- [ ] Create a `/build/` namespace for generated artefacts (PDFs, plaintext exports, generated tables, CI summaries).
- [ ] Consolidate release manifests by merging `/meta/` planning data with `/versions/` historical records.
- [ ] Relocate `ops/makefile` and supporting automation into `/ops/scripts/` or `/tools/` to centralize entrypoints.

## Section 6 — Status Declaration
The AI OSI Stack v5.0 repository remains under active development and structural refinement.  
Redundant and legacy directories (e.g., /audit/, /meta/) are being consolidated for clarity.  
This audit report documents the current state and provides canonical guidance for repository reorganization before final v5.0 release.
