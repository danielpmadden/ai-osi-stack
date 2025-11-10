#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."/source
latexmk -pdf -silent ai-osi-stack-v5.tex
cp ai-osi-stack-v5.pdf ../versions/
