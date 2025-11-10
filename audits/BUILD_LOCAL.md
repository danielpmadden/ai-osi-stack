© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Local Build Instructions

1. Install TeX Live (full distribution recommended).
2. Run `latexmk -pdf source/ai-osi-stack-v5.tex`.
3. Record `sha512sum source/ai-osi-stack-v5.pdf` (or equivalent) in your personal checksum log; do not commit outputs to the repository.
4. Prepare Zenodo upload with PDF, manifest, and integrity notice.
5. Ensure canonical version remains v5.0.0.
