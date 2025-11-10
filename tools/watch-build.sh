#!/usr/bin/env bash
# Watches source/ for changes and rebuilds PDF asynchronously.
sudo apt-get install -y inotify-tools latexmk >/dev/null 2>&1
while inotifywait -r -e modify,close_write source; do
  bash tools/build-docs.sh > /dev/null 2>&1 &
done
tools/gen-checksums.py
