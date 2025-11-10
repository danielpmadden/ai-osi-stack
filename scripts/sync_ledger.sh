#!/usr/bin/env bash
set -euo pipefail

API_URL="${API_URL:-http://localhost:8000}"

echo "Requesting ledger sync from $API_URL"
curl -s "$API_URL/ledger/entries" | jq '.'

