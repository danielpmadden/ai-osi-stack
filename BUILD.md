<!-- SPDX-License-Identifier: CC-BY-NC-ND-4.0 -->
# Build and Reproducibility Guide

This guide documents the LaTeX toolchain, deterministic build process, and Codex automation for the AI OSI Stack custodial specification.

## Toolchain Requirements
- TeX Live 2023 or newer with `latexmk`
- GNU Make compatible shell (bash)
- Python 3.10+ for checksum generation

## Build Commands
1. `bash tools/build-docs.sh` — Compiles `source/ai-osi-stack-v5.tex` using `latexmk` with reproducible flags and places PDFs in `versions/`.
2. `python tools/gen-checksums.py` — Updates `meta/v5-manifest.yaml` and appends SHA-512 hashes for each PDF to `versions/checksums.txt`.

## Codex Automation
Execute the following commands before tagging a release:
```
codex run validate-aeip
codex run integrity-ledger
codex run clarity-compile
```

## Output Targets
- `versions/ai-osi-stack-v5.pdf` — Canonical custodial specification
- `versions/checksums.txt` — SHA-512 manifest for published artefacts

## Deterministic Build Notes
- The repository ships a `latexmkrc` configured for non-interactive, reproducible builds.
- Builds must be executed from the repository root to ensure consistent relative paths.
- Regenerate artefacts after substantive documentation updates and verify hashes before release.

> Authored and maintained solely by the Custodial Editorial Committee.
> This is a non-operational, publication-grade governance artifact.
> No AEIP runtime specs or machine-readable schemas are included.
