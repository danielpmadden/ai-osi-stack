© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Repository Coherence Audit — v5-RC

> **Historical Reference Notice:** This audit describes the pre-open-core repository layout. Mentions of directories such as `analytics/`, `ops/`, `ml/`, and `protocol/` refer to private Governance Control Tower™ workspaces and are retained for archival context only.

## A) Executive Summary
The v5 release-candidate tree now mirrors the civic governance workflow: analytics assets live under `analytics/`, operational tooling under `ops/`, and canonical documentation under `docs/`. We added lightweight READMEs to every top-level directory so maintainers can quickly confirm stewardship scope. Misplaced assets—including dashboard schemas, signing keys, and Zenodo metadata—now reside with their canonical peers, reducing duplicate linkage across handbooks. References throughout the documentation set were refreshed to acknowledge the new layout and the centralization of automation scripts inside `ops/scripts`. Remaining convergence work focuses on collapsing legacy dashboard planning notes and ensuring upcoming ML audit utilities slot cleanly into the new `/ml` namespace.

## B) Misplacements & Inconsistencies
| Item | Issue | Recommended Action | Status |
| --- | --- | --- | --- |
| Dashboard application | Front-end lived at repository root (`dashboard/`) causing path drift in docs and tooling. | Relocate to `analytics/dashboard/` and update references. | Completed |
| Automation scripts | Maintenance scripts in root `scripts/` duplicated operational scope. | Move scripts to `ops/scripts/` and align documentation. | Completed |
| Dashboard schema JSON | Schema stored in `docs/dashboard/` alongside prose. | Move to `schemas/dashboard/data-model-schema.json`. | Completed |
| AEIP public key manifest | `public-keys.json` lived in `docs/` despite being part of protocol tooling. | Relocate to `protocol/public-keys.json` and adjust inventory references. | Completed |
| Zenodo metadata | Release metadata lived in `docs/`. | Move to `meta/zenodo-metadata.yaml` and note canonical location. | Completed |
| Governance dashboard notes | `docs/governance-dashboard/` duplicates portions of analytics README and build scripts. | Consolidate into `analytics/dashboard/docs/` and cross-link from docs once ML audit finalizes new flow. | Pending |

## C) Suggested Restructuring Plan
- Maintain the normalized top-level map: `/analytics`, `/ml`, `/docs`, `/schemas`, `/examples`, `/ops`, `/tests`, `/archive`, `/versions`, and stewardship-specific collections.
- Keep operational automation within `ops/scripts/` and expose entrypoints via `ops/README.md` and `CONTRIBUTING.md`.
- Merge duplicated dashboard planning notes after verifying no normative clauses are embedded; retain canonical instructions under `docs/dashboard/`.
- Continue inventory regeneration (`ops/inventory/inventory.sh`) after structural changes to ensure hashes and file tables reference new paths.

## D) Checklist of Renamed or Merged Files
- [x] `dashboard/` → `analytics/dashboard/`
- [x] `scripts/*` → `ops/scripts/*`
- [x] `docs/dashboard/data-model-schema.json` → `schemas/dashboard/data-model-schema.json`
- [x] `docs/public-keys.json` → `protocol/public-keys.json`
- [x] `docs/zenodo-metadata.yaml` → `meta/zenodo-metadata.yaml`
