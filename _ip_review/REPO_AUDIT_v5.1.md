© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# AI OSI Stack — Repository Audit (v5.1-open-core)

**Audit date:** 2025-11-15  \
**Auditor:** Repository steward (senior documentation architect)  \
**Scope:** Full tree at commit under review (430 files)

## 1. Methodology

- Enumerated repository contents with `find` to confirm total file count (430
  artefacts) for this open-core snapshot.
- Searched for residual references to private runtimes or operational systems
  using targeted keyword scans (`govspine`, `backend`, `analytics`, `ops`).
- Reviewed licensing notices against the updated dual-license `LICENSE` record
  and verified SPDX headers on executable assets.
- Executed `_open_tools/validate_json.py` to parse all JSON/JSON-LD files and
  confirm syntax integrity (no errors reported).
- Sampled each top-level directory to document custodial purpose and expected
  contents.

## 2. Private Runtime & Sensitive Reference Check

- **No private runtimes detected:** Directories for `govspine`, `ops`,
  `analytics`, or backend runtimes are absent from the tree.
- **Residual references remain:**
  - Historical prototype code under
    `versions/historical/prototypes/release-package/protocol/ledger-node.py`
    still imports `govspine` modules that are no longer distributed. The file
    should be annotated or relocated to avoid implying the runtime ships with the
    open-core release.
  - `README.md` continues to describe the `govspine/` runtime, sample imports,
    and testing instructions that no longer function without private modules.
  - Documentation in `docs/idd-layer-interface-guide.md` and other briefs
    references schema paths inside `govspine/runtime/...` that should now point
    to the public `schemas/` equivalents.
  - Multiple legacy audit records (`audits/*`) catalog assets inside
    `govspine/` and `ops/`; these need historical disclaimers or relocation to
    the archive so current readers do not assume the assets are present.

## 3. Keyword Scan Results

| Keyword | Paths Requiring Follow-up | Notes |
|---------|---------------------------|-------|
| `govspine` | `README.md`, `docs/idd-layer-interface-guide.md`, numerous audit dossiers, and historical prototypes under `versions/historical/` | Update references to clarify the runtime is private or replace with public equivalents. |
| `backend` | Legacy audit inventory mentions `tools/control-tower/backend/...` paths | Ensure cross-references move to archive context or add “historical only” labels. |
| `analytics` | Audit notes and historical dashboard plans cite `analytics/analytics/...` directories | Confirm these references are marked as historical and that current README no longer points to them. |
| `ops` | `Dockerfile` and `package.json` scripts reference `ops/` tooling that no longer exists | Adjust or deprecate build scripts to avoid confusion for new users. |

## 4. Licensing Review

- Root `LICENSE` now documents the Apache-2.0 (code) and CC BY-SA 4.0
  (documentation) split consistent with `legal/COPYRIGHT-AND-LICENSE-MAP.md` and
  the SPDX headers across the repo.
- All `_open_tools/*.py` utilities now include SPDX identifiers and minimal logic
  appropriate for open redistribution.
- Documentation assets continue to carry CC BY-SA 4.0 headers; no conflicting
  notices observed after this update.

## 5. Schema & JSON Integrity

- `_open_tools/validate_json.py` executed successfully; no JSON or JSON-LD syntax
  errors were detected across the repository.
- Schema inventory remains consistent with ledger samples; however, ensure future
  schema additions maintain SPDX headers and provenance metadata.

## 6. Directory Role Summary

| Directory | Purpose |
|-----------|---------|
| `_open_tools/` | Public validation helpers (JSON syntax, provenance, integrity checks) free of private dependencies. |
| `archive/` | Frozen historical materials, including pre-open-core artefacts (v4, prototypes). |
| `audits/` | Legacy and current audit reports describing governance posture and repository structure. |
| `docs/` | Civic briefs, policy guides, and operational documentation mapped to stack layers. |
| `examples/` | Sample AEIP payloads and walkthroughs for civic demonstrations. |
| `ledger/` | Illustrative ledger entries, integrity notices, and hermeneutic annotations. |
| `legal/` | Custodianship, licensing, and provenance declarations. |
| `meta/` | Integrity manifests, release manifests, and supporting metadata. |
| `press-kit/` | Media-facing fact sheets and communication assets. |
| `schemas/` | JSON/JSON-LD schemas defining AEIP artefacts and governance receipts. |
| `source/` | LaTeX manuscripts for canonical stack publications. |
| `versions/` | Published PDFs, historical releases, and prototype packages. |

## 7. Outstanding Issues & Recommendations

1. **Update onboarding materials.** Refresh the production `README.md` and other
   introductory docs to align with the new open-core scope (draft prepared in
   `_staging/README_PROPOSED.md`).
2. **Annotate historical references.** Add notices to residual audit files and
   prototype code clarifying that `govspine` and `ops` modules live in the
   private Governance Control Tower repository.
3. **Rationalize build scripts.** The root `Dockerfile` and `package.json`
   reference missing `ops/` and `tests/` directories; either restore minimal
   open-core tooling or replace scripts with open-only equivalents.
4. **Archive deprecated instructions.** Move outdated runtime walkthroughs and
   dashboard plans into `archive/` with clear version labeling to prevent
   confusion.
5. **Continue SPDX enforcement.** Ensure any new file additions include SPDX
   headers matching the dual-license policy and cite provenance per
   `CANONICAL_PROVENANCE.yaml`.

## 8. Completed Remediation in This Audit

- Created `_open_tools` SPDX-compliant helper scripts suitable for public use.
- Updated the root `LICENSE` and `CANONICAL_PROVENANCE.yaml` to reflect
  `v5.1-open-core`.
- Authored `_staging/README_PROPOSED.md` and `_staging/CHANGELOG_v5.1.md` for
  steward review prior to publishing the new release tag.
