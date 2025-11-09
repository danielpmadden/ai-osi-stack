#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Purpose: Verify release artifact hashes and detached signatures.
# Usage: ./ops/release/verify.sh dist/ai-osi-stack-v5.0.0.tar.gz versions/ai-osi-stack-v5.pdf

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <artifact> [<artifact> ...]" >&2
  exit 1
fi

REPO_ROOT="$(git rev-parse --show-toplevel)"
NOTICE_FILE="$REPO_ROOT/INTEGRITY_NOTICE.md"

if [[ ! -f "$NOTICE_FILE" ]]; then
  echo "INTEGRITY_NOTICE.md not found." >&2
  exit 2
fi

python3 - "$NOTICE_FILE" "$REPO_ROOT" "$@" <<'PY'
import re
import sys
from pathlib import Path

notice_path = Path(sys.argv[1])
repo_root = Path(sys.argv[2])
artifacts = [Path(p) for p in sys.argv[3:]]

content = notice_path.read_text(encoding="utf-8")
rows = {
    match.group("artifact"): match.group("hash")
    for match in re.finditer(r"\| `(.*?)` \| `(?P<hash>[A-Fa-f0-9]{64}|TBD_AFTER_RELEASE)` \|", content)
}

missing = []
for artifact in artifacts:
    if not artifact.exists():
        missing.append(str(artifact))

if missing:
    raise SystemExit(f"Missing artifacts: {', '.join(missing)}")

for artifact in artifacts:
    rel = str(artifact.relative_to(repo_root))
    expected = rows.get(rel)
    if expected is None:
        print(f"Warning: {rel} not recorded in INTEGRITY_NOTICE.md")
        continue
    import hashlib

    digest = hashlib.sha512(artifact.read_bytes()).hexdigest()
    if expected == "TBD_AFTER_RELEASE":
        print(f"INFO: {rel} hash recorded as TBD. Computed {digest}.")
    elif digest != expected:
        raise SystemExit(f"Hash mismatch for {rel}: expected {expected}, got {digest}")
    else:
        print(f"Hash OK for {rel}")

PY

for ARTIFACT in "$@"; do
  ASC="$ARTIFACT.asc"
  if [[ -f "$ASC" ]]; then
    gpg --verify "$ASC" "$ARTIFACT"
  else
    echo "Signature missing for $ARTIFACT (skipped)"
  fi
done
