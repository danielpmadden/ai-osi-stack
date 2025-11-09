#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Purpose: Create detached signatures for release artifacts and refresh integrity hashes.
# Usage: ./ops/release/sign.sh dist/ai-osi-stack-v5.0.0.tar.gz versions/ai-osi-stack-v5.pdf
# Requirements: gpg, python3, sha512sum.

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <artifact> [<artifact> ...]" >&2
  exit 1
fi

if ! command -v gpg >/dev/null 2>&1; then
  echo "gpg is required but not installed. Install GnuPG and retry." >&2
  exit 2
fi

REPO_ROOT="$(git rev-parse --show-toplevel)"
NOTICE_FILE="$REPO_ROOT/INTEGRITY_NOTICE.md"

if [[ ! -f "$NOTICE_FILE" ]]; then
  echo "INTEGRITY_NOTICE.md not found at repository root." >&2
  exit 3
fi

declare -A HASHES

for ARTIFACT in "$@"; do
  if [[ ! -f "$ARTIFACT" ]]; then
    echo "Missing artifact: $ARTIFACT" >&2
    exit 4
  fi
  RELATIVE_PATH="$(python3 -c 'import os,sys;print(os.path.relpath(sys.argv[1], sys.argv[2]))' "$ARTIFACT" "$REPO_ROOT")"
  SIGNATURE="$ARTIFACT.asc"
  GPG_ARGS=(--armor --detach-sign --output "$SIGNATURE")
  if [[ -n "${GPG_KEY:-}" ]]; then
    GPG_ARGS+=(--local-user "$GPG_KEY")
  fi
  gpg "${GPG_ARGS[@]}" "$ARTIFACT"
  HASH=$(sha512sum "$ARTIFACT" | awk '{print $1}')
  HASHES["$RELATIVE_PATH"]="$HASH"
  echo "Signed $RELATIVE_PATH -> ${RELATIVE_PATH}.asc"
  echo "SHA-512: $HASH"

done

(
  for key in "${!HASHES[@]}"; do
    printf '%s=%s\n' "$key" "${HASHES[$key]}"
  done
) | python3 - "$NOTICE_FILE" <<'PY'
import re
import sys
from pathlib import Path

notice_path = Path(sys.argv[1])
content = notice_path.read_text(encoding="utf-8")
updates = {
    key: value
    for key, value in (line.split("=", 1) for line in sys.stdin.read().strip().splitlines() if line)
}

for artifact, digest in updates.items():
    pattern = re.compile(rf"(\| `{re.escape(artifact)}` \| `)([^`]+)(` \|)")
    if not pattern.search(content):
        print(f"Warning: {artifact} not found in INTEGRITY_NOTICE.md", file=sys.stderr)
        continue
    content = pattern.sub(rf"\1{digest}\3", content)

notice_path.write_text(content, encoding="utf-8")
PY
