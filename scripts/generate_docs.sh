#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCS_DIR="$ROOT_DIR/docs/AI_OSI_Stack"

python "$ROOT_DIR/scripts/validate_json.py" "$DOCS_DIR/00_Project_Definition.json"

echo "Docs validated at $DOCS_DIR"
