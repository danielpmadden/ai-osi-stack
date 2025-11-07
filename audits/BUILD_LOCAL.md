# Local Build Instructions

1. Install TeX Live (full distribution recommended).
2. Run `latexmk -pdf source/ai-osi-stack-v5.tex`.
3. Compute `sha512sum source/ai-osi-stack-v5.pdf > versions/ai-osi-stack-v5.sha512`.
4. Prepare Zenodo upload with PDF, manifest, and integrity notice.
5. Ensure canonical version remains v5.0.0.
