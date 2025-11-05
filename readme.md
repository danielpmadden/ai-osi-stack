
# AI OSI Stack v5 — Canonical Edition

## Abstract
The AI OSI Stack v5 Canonical Edition preserves the institutional specification for accountable AI operations. This repository codifies governance controls, evidentiary ledgers, and executable reference models across the full sociotechnical stack. Content is organized so custodians, auditors, and engineers can verify provenance, regenerate canonical publications, and exercise lifecycle checks without relying on informal drafts.

## Directory Overview
| Path | Purpose |
| --- | --- |
| `docs/` | Canonical publications, dashboards, crosswalks, and public-facing guidance. |
| `source/` | LaTeX source for the v5 canonical manuscript (front matter, chapters, appendices, back matter). |
| `governance-spine/` | Runtime layer implementations, AEIP payloads, governance data, and operational records. |
| `govspine/` | Python bridge package that exposes runtime layers and shared utilities for tools and tests. |
| `schemas/` | Machine-readable governance and AEIP schemas used across the stack. |
| `protocol/` | AEIP handshake and ledger node reference implementations with test vectors. |
| `tools/` | Command-line tools, dashboards, and automation (including the control-tower prototype). |
| `ledger/` | Signed evidentiary manifests, integrity notices, and continuity records. |
| `tests/` | Validation suites covering AEIP lifecycle, layer contracts, and governance simulations. |
| `versions/` | Historical releases, update plans, and archived prototypes (including legacy release packages). |

## Build & Validation
1. **Install dependencies**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt  # curate per deployment needs
   ```
2. **Run test suites**
   ```bash
   make test
   ```
3. **Compile the canonical manuscript**
   ```bash
   cd source
   latexmk -pdf ai-osi-stack-v5.tex
   ```
4. **Validate AEIP artifacts**
   ```bash
   python tools/validate-artifact.py governance-spine/aeip/frame-payload.json
   python tools/verify-aeip-signatures.py
   ```

## Integrity Verification
1. Compare repository state with the published digest:
   ```bash
   sha512sum -c ledger/integrity/notices/integrity-notice.md
   ```
2. Review canonical provenance statements under `ledger/integrity/notices/` for custody, signature, and supersession context.
3. Cross-check ledger manifests (e.g., `ledger/meta-audit/continuity-manifest.json`) against governance deployment records in `governance-spine/deployments/`.

## License & Citation
- **License:** Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0). See [`license.txt`](license.txt).
- **Preferred citation:**
  > Madden, Daniel P. (2025). *The AI OSI Stack: A Governance Blueprint for Scalable and Trusted AI* (Version 5, Canonical Edition). https://github.com/danielpmadden/ai-osi-stack
