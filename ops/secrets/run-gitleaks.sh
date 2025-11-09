#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Purpose: Execute gitleaks secret scanning with repo-specific configuration.
# Usage: ./ops/secrets/run-gitleaks.sh

set -euo pipefail

if ! command -v gitleaks >/dev/null 2>&1; then
  echo "gitleaks not found. Install from https://github.com/gitleaks/gitleaks/releases and retry." >&2
  exit 1
fi

gitleaks detect --config ops/secrets/gitleaks.toml --verbose --redact
