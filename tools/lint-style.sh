#!/usr/bin/env bash
pip install -q codespell proselint
mkdir -p audits
find source -type f \( -name "*.tex" -o -name "*.md" \) | \
  xargs -r -n1 -P4 proselint > audits/style.log 2>&1 &
