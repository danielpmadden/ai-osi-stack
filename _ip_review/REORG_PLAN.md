<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# AI OSI Stack — Reorganization Plan (v5.1-open-core)

## Normalized Top-Level Order

1. `/docs`
2. `/schemas`
3. `/ledger`
4. `/legal`
5. `/audits`
6. `/meta`
7. `/source`
8. `/examples`
9. `/_open_tools`
10. `/archive`
11. `/versions`
12. `/press-kit`
13. `/_ip_review`
14. `/_staging`

Update directory listings (README navigation, repo documentation) to follow this
sequence so newcomers encounter mission-critical documentation, schemas, and
ledger samples before archival material.

## Recommended Moves & Renames

| Current Location | Proposed Location | Rationale |
|------------------|-------------------|-----------|
| `press-kit/` | `docs/press-kit/` | Keep public communications adjacent to canonical documentation; leave a stub README in `press-kit/` pointing to the new location. |
| `archive/v4/` | `versions/historical/v4/` | Consolidate historical releases under the `versions/` tree to reduce duplicate archival routes. |
| Legacy runtime-heavy audit files in `audits/` | `archive/audits/` | Separate live audit posture from historical reports referencing private runtimes. |
| Dashboard planning notes inside `docs/` mentioning `analytics/` | `archive/dashboard-planning/` | Prevent confusion now that analytics tooling lives in the private Governance Control Tower repo. |
| Build artefacts referencing `ops/` (e.g., `Dockerfile`, `package.json`) | `archive/build/` or updated open-only equivalents | Avoid broken workflows in the open-core tree while preserving historical scripts for context. |

## Cleanup Actions

1. **Publish the refreshed README.** Replace the production `README.md` with
   `_staging/README_PROPOSED.md` once moves are complete and references updated.
2. **Revise cross-references.** Search for `govspine`, `analytics`, `ops`, and
   `control-tower`; update or annotate links to clarify their private status.
3. **Refresh manifests.** Regenerate integrity manifests under `meta/` and update
   ledger hashes after restructuring.
4. **Tag alignment.** Ensure `versions/` contains regenerated PDFs and the new
   changelog before creating the `v5.1-open-core` tag.
5. **Automation clarity.** Provide minimal open-core scripts to replace removed
   `ops/` tooling or remove broken scripts entirely after documenting manual
   workflows.

## Sequencing Guidance

1. Execute directory moves/renames and update internal links.
2. Adopt the new README and changelog.
3. Regenerate manifests and ledger checksums.
4. Conduct a final validation pass (JSON validator, provenance check).
5. Tag and publish `v5.1-open-core` once documentation and manifests are synced.
