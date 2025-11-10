#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Authored and maintained solely by the Custodial Editorial Committee.
# This script is provided for non-operational, reproducibility support.
# No AEIP runtime logic is exposed or executed here.
set -euo pipefail

REPO_ROOT="$(dirname "$0")/.."
SOURCE_DIR="$REPO_ROOT/source"
OUTPUT_DIR="$REPO_ROOT/versions"
AUX_DIR="$OUTPUT_DIR/.aux"

mkdir -p "$OUTPUT_DIR" "$AUX_DIR"
cd "$SOURCE_DIR"
latexmk -pdf -silent -outdir="$OUTPUT_DIR" -auxdir="$AUX_DIR" ai-osi-stack-v5.tex

echo "✅ Build complete — artefacts stored in /versions/"
