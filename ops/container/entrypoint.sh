#!/usr/bin/env sh
# SPDX-License-Identifier: Apache-2.0
# Purpose: Run baseline governance validations inside the hardened container image.

set -eu

npm run validate:aeip
npm run validate:governance || true
pytest -q
