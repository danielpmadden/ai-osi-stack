# Async Workflow Helpers

To keep documentation builds, integrity manifests, and style audits running in the background while you author content, start the helper processes in separate shells (or append `&` to run them in the background):

```bash
bash tools/watch-build.sh &
python3 tools/gen-checksums.py &
bash tools/lint-style.sh &
bash tools/auto-snapshot.sh &
```

Each helper runs independently, can be terminated at any time, and does not perform any destructive operations. Use them together or individually to match your local workflow.
