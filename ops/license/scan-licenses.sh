#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Purpose: Aggregate dependency license metadata for compliance review.
# Usage: ./ops/license/scan-licenses.sh

set -euo pipefail

OUTPUT_DIR="ops/license"
OUTPUT_FILE="$OUTPUT_DIR/dependency-licenses.csv"
mkdir -p "$OUTPUT_DIR"

echo 'ecosystem,package,version,license' >"$OUTPUT_FILE"

if command -v npx >/dev/null 2>&1; then
  echo "Collecting Node.js dependency licenses" >&2
  npx --yes license-checker --production --json >"$OUTPUT_DIR/node-licenses.json"
  python3 - <<'PY'
import csv
import json
from pathlib import Path

node_data = json.loads(Path('ops/license/node-licenses.json').read_text())
with Path('ops/license/dependency-licenses.csv').open('a', encoding='utf-8', newline='') as handle:
    writer = csv.writer(handle)
    for pkg, meta in sorted(node_data.items()):
        writer.writerow([
            'node',
            pkg,
            meta.get('version', ''),
            meta.get('licenses', ''),
        ])
PY
else
  echo "npx not available; skipping Node license scan" >&2
fi

if python3 -m pip show pip-licenses >/dev/null 2>&1; then
  echo "Collecting Python dependency licenses" >&2
else
  echo "Installing pip-licenses" >&2
  python3 -m pip install --upgrade pip-licenses >/dev/null
fi

python3 -m piplicenses --format=csv --output-file="$OUTPUT_DIR/python-licenses.csv" --with-system --no-header
python3 - <<'PY'
import csv
from pathlib import Path

source = Path('ops/license/python-licenses.csv')
dest = Path('ops/license/dependency-licenses.csv')
with source.open('r', encoding='utf-8') as handle, dest.open('a', encoding='utf-8', newline='') as out:
    reader = csv.reader(handle)
    writer = csv.writer(out)
    for row in reader:
        if not row:
            continue
        name, version, license = row[0], row[1], row[2]
        writer.writerow(['python', name, version, license])
PY

echo "License report saved to $OUTPUT_FILE"
