# Repository Inventory

This directory stores machine-verifiable metadata generated from the repository contents. The `inventory.sh` script builds two artifacts:

- `file-inventory.json` — every file with size, SHA-512 digest, MIME/type detection, binary/executable flags, and whether it appears to be a Git LFS pointer.
- `source-index.csv` — extension-level statistics (lines of code, maximum line length) with placeholders for future coverage data.

## Regenerating the Inventory

```bash
./ops/inventory/inventory.sh
```

The script requires Bash, Git, and Python 3. It executes entirely locally and is idempotent.

## Verifying Checksums

1. Regenerate the inventory using the command above.
2. Compare `file-inventory.json` with a previously recorded copy using `jq` and `diff`:

   ```bash
   jq -S '.' ops/inventory/file-inventory.json > /tmp/current.json
   jq -S '.' /path/to/reference/file-inventory.json > /tmp/reference.json
   diff -u /tmp/reference.json /tmp/current.json
   ```

3. Spot-check individual files by recomputing their digest:

   ```bash
   FILE="README.md"
   EXPECTED=$(jq -r ".files[] | select(.path == \"$FILE\") | .sha512" ops/inventory/file-inventory.json)
   ACTUAL=$(shasum -a 512 "$FILE" | awk '{print $1}')
   test "$EXPECTED" = "$ACTUAL"
   ```

4. When publishing artifacts, capture a copy of the inventory alongside signed release materials and record the hash in `INTEGRITY_NOTICE.md`.

## Determinism Notes

- Files are traversed in sorted order.
- SHA-512 is used for all digests.
- The script omits the `.git/` directory and GitHub Action caches; everything else is enumerated.

The CI workflow calls this script on every run and uploads both outputs for archival review.
