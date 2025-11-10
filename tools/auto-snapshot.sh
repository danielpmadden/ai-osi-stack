#!/usr/bin/env bash
# Commits writing progress every 15 minutes
while true; do
  git add source/*.tex reference/*.md >/dev/null 2>&1
  git commit -m "auto-snapshot $(date '+%H:%M:%S')" --allow-empty >/dev/null 2>&1
  sleep 900
done &
