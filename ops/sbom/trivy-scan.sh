#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Purpose: Run Trivy filesystem and SBOM scans.
# Usage: ./ops/sbom/trivy-scan.sh

set -euo pipefail

if ! command -v trivy >/dev/null 2>&1; then
  echo "Trivy is required. Install via https://aquasecurity.github.io/trivy/" >&2
  exit 1
fi

OUTPUT_DIR="ops/sbom"
mkdir -p "$OUTPUT_DIR"

trivy fs --exit-code 1 --severity HIGH,CRITICAL --format table --output "$OUTPUT_DIR/trivy-fs.txt" .
trivy sbom --exit-code 1 --severity HIGH,CRITICAL --output "$OUTPUT_DIR/trivy-sbom.txt" "$OUTPUT_DIR/cyclonedx.json"

echo "Trivy filesystem scan: $OUTPUT_DIR/trivy-fs.txt"
echo "Trivy SBOM scan: $OUTPUT_DIR/trivy-sbom.txt"
