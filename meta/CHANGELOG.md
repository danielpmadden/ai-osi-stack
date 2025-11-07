
# Canonical Refactor Changelog

| Previous Path | Canonical Path |
| --- | --- |
| `Annex IV Crosswalk.{md,txt}` | `docs/crosswalks/annex-iv-crosswalk.{md,txt}` |
| `Canonical Provenance Statement.txt` | `ledger/integrity/notices/canonical-provenance-statement.txt` |
| `INTEGRITY_NOTICE.{md,txt}` | `ledger/integrity/notices/integrity-notice.{md,txt}` |
| `LICENSE.txt` | `meta/license.txt` |
| `Makefile` | `ops/makefile` |
| `README.md` | `meta/README.md` |
| `src/common` | `govspine/runtime/common` (exposed via `govspine.common`) |
| `src/layer*_*/` | `govspine/runtime/layer*-*/` (exposed via `govspine.layer0X*`) |
| `governance/*` | `govspine/` (aeip, control, data, deployments, incidents, models, postmortems, registries) |
| `continuity/manifest.json` | `ledger/meta-audit/continuity-manifest.json` |
| `custodianship/succession-protocol.md` | `docs/governance/succession-protocol.md` |
| `apps/control-tower/` | `tools/control-tower/` |
| `examples/` | `docs/examples/` |
| `release_package/` | `versions/historical/prototypes/release-package/` |
| `version_4_master.tex` | `versions/historical/prototypes/version-4-master.tex` |
| `Version 5 Draft.tex` | `versions/historical/prototypes/version-5-draft.tex` |
| `docs/public_disclosures/` | `docs/public-disclosures/` |
| `docs/governance-dashboard/CONTROL_TOWER_README.md` | `docs/governance-dashboard/control-tower-readme.md` |
| `source/chapters/<nn>-*.tex` | `source/chapters/chapter-<nn>-*.tex` |
| `source/appendices/<letter>-*.tex` | `source/appendices/appendix-<letter>-*.tex` |

## Additional Updates
- Rewrote LaTeX master file `source/ai-osi-stack-v5.tex` to reference the canonical file names directly.
- Generated the `govspine` bridge package so Python tooling imports map cleanly to the hyphenated runtime directories.
- Updated automation (`ops/makefile`, tools, and protocol loaders) to match the reorganized module paths and directory layout.
- Archived historical release artifacts and drafts under `versions/historical/prototypes/` to declutter the canonical tree.
- Refreshed `meta/README.md` with the canonical abstract, directory guide, build instructions, integrity verification steps, and citation.
