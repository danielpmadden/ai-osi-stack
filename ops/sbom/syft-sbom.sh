#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Purpose: Generate SPDX and CycloneDX SBOMs using Syft.
# Usage: ./ops/sbom/syft-sbom.sh

set -euo pipefail

OUTPUT_DIR="ops/sbom"
SPDX_FILE="$OUTPUT_DIR/spdx.json"
CYCLONE_FILE="$OUTPUT_DIR/cyclonedx.json"

mkdir -p "$OUTPUT_DIR"

if ! command -v syft >/dev/null 2>&1; then
  echo "Syft is required. Install via https://github.com/anchore/syft/releases" >&2
  exit 1
fi

syft packages dir:. -o spdx-json >"$SPDX_FILE"
syft packages dir:. -o cyclonedx-json >"$CYCLONE_FILE"

echo "SPDX SBOM written to $SPDX_FILE"
echo "CycloneDX SBOM written to $CYCLONE_FILE"
