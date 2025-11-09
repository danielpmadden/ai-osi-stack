# OpenTimestamps Notarization Plan

The AI OSI Stack maintainers notarize release hashes using [OpenTimestamps](https://opentimestamps.org). The workflow below should be executed immediately after updating `INTEGRITY_NOTICE.md` and committing the release.

## Prerequisites

- Install the CLI: `pip install opentimestamps-client`
- Ensure `ots` is available on the PATH in CI and release environments.

## Commands

```bash
# 1. Collect hashes for canonical artifacts
sha512sum dist/ai-osi-stack-v5.0.0.tar.gz versions/ai-osi-stack-v5.pdf > dist/canonical-artifacts.sha512

# 2. Create timestamp requests
ots stamp --file dist/canonical-artifacts.sha512

# 3. (Optional) Timestamp integrity notice for audit completeness
ots stamp --file INTEGRITY_NOTICE.md

# 4. Verify proofs locally before uploading
ots verify dist/canonical-artifacts.sha512.ots
```

Store the `.ots` proof files under `dist/` and reference them in `INTEGRITY_NOTICE.md`. Proof uploads should accompany the signed release assets on GitHub Releases.

## CI Integration

The GitHub release workflow will:

1. Generate the deterministic tarball via `ops/release/mk-dist.sh`.
2. Produce the SHA-512 manifest and request timestamps with `ots stamp` (if available).
3. Upload `.ots` files as release assets.

When OpenTimestamps infrastructure is unreachable, rerun the notarization process and append a note to the release changelog.
