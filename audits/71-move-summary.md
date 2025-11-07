# Move Summary — Govspine Normalization

## File Relocations
- `governance-spine/` → `govspine/` (complete runtime evidence store and registries)
- `README.md` → `meta/README.md`
- `INTEGRITY_NOTICE.md` → `meta/INTEGRITY_NOTICE.md`
- `integrity_notice_v5.json` → `meta/integrity_notice_v5.json`
- `v5-manifest.yaml` → `meta/v5-manifest.yaml`
- `license.txt` → `meta/license.txt`
- `CHANGELOG.md` → `meta/CHANGELOG.md`
- `SECURITY.md` → `meta/SECURITY.md`
- `.gitignore` → `ops/.gitignore`
- `.pre-commit-config.yaml` → `ops/.pre-commit-config.yaml`
- `makefile` → `ops/makefile`
- `.github/workflows/*` → `ops/.github/workflows/*`

## Duplicates Skipped
- None — all moved files were unique.

## Import Paths Updated
- `govspine/common/{__init__,artifacts,crypto,interface,layer,schema}.py`
- `govspine/layer0[1-8]*/__init__.py`
- `tools/{governance-manifest,notify-red-status,update-metrics,verify-aeip-signatures}.py`
- `tests/manifest-version-check.py`

## Documentation & Manifest Updates
- `meta/README.md` refreshed to cover new directory map, adjusted relative links, and updated verification commands.
- `meta/SECURITY.md`, `meta/INTEGRITY_NOTICE.md`, `meta/integrity_notice_v5.json`, and `press-kit/fact-sheet.md` now reference `meta/` paths and govspine assets.
- `meta/v5-manifest.yaml` records relocation metadata with `moved_from` / `moved_to` annotations.
- `audits/00-inventory-map.md` and related audit summaries align with the new layout.

## Line Change Overview (selected files)
- `README.md`: 252-line replacement (root stub now links to meta documentation)
- `meta/README.md`: 255 new lines (canonical README moved with refreshed links)
- `meta/v5-manifest.yaml`: +54 lines (relocation metadata added)
- `meta/CHANGELOG.md`: 16 line edits (path mapping table and narrative tweaks)
- `meta/INTEGRITY_NOTICE.md`: 6 line edits (path references)
- `meta/SECURITY.md`: 6 line edits (verification commands)
- `press-kit/fact-sheet.md`: 4 line edits (integrity references)
- `audits/00-inventory-map.md`: 152 line edits (path realignment)
- `audits/10-naming-coherence.md`: 106 line edits (file reference updates)
- `versions/historical/update-plan*.md`: bulk replacements totaling 188–554 line edits per file to point to `meta/INTEGRITY_NOTICE.md`

Refer to `git diff --stat` for the complete per-file change list (130 files changed, 1,989 insertions, 1,940 deletions).
