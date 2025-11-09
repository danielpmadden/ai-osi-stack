#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
# Purpose: Produce a deterministic source distribution archive.
# Usage: ./ops/release/mk-dist.sh 5.0.0
# Requirements: bash, git, tar, find, xargs. SOURCE_DATE_EPOCH will be honored if set.

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <version>" >&2
  exit 1
fi

VERSION="$1"
REPO_ROOT="$(git rev-parse --show-toplevel)"
DIST_DIR="$REPO_ROOT/dist"
TARBALL="$DIST_DIR/ai-osi-stack-v${VERSION}.tar.gz"

mkdir -p "$DIST_DIR"

SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-$(date -u +%s)}"
export SOURCE_DATE_EPOCH
export GZIP=-n

cd "$REPO_ROOT"

TMP_LIST="$(mktemp)"
trap 'rm -f "$TMP_LIST"' EXIT

git ls-files >"$TMP_LIST"

tar \
  --create \
  --gzip \
  --file "$TARBALL" \
  --sort=name \
  --mtime="@${SOURCE_DATE_EPOCH}" \
  --owner=0 --group=0 --numeric-owner \
  --pax-option=exthdr.name=%d/PaxHeaders/%f \
  --pax-option=delete=atime --pax-option=delete=ctime \
  --exclude='.git' \
  --exclude='dist' \
  --exclude='node_modules' \
  --exclude='**/__pycache__' \
  --exclude='**/*.pyc' \
  --files-from "$TMP_LIST"

sha512sum "$TARBALL"
