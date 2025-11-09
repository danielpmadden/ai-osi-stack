#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Purpose: Scan the container image for vulnerabilities using Trivy.
# Usage: ./ops/container/trivy-image-scan.sh ai-osi-stack/validator:latest

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <image>" >&2
  exit 1
fi

IMAGE="$1"

if ! command -v trivy >/dev/null 2>&1; then
  echo "Trivy is required. Install via https://aquasecurity.github.io/trivy/ and re-run." >&2
  exit 2
fi

trivy image --exit-code 1 --severity HIGH,CRITICAL --format table "$IMAGE"
