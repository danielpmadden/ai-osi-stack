<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# AI OSI Stack — Integrity & Canonical Provenance Notice

**Canonical version:** v5.0.0 (established 2025-11-09)

This repository (`https://github.com/danielpmadden/ai-osi-stack`) and domain of record (`https://aiosi.org`) are the sole canonical sources for the AI OSI Stack and affiliated AEIP specifications. Only artifacts signed by Daniel P. Madden and recorded in this notice are normative.

## Signed Artifacts (SHA-512)

| Artifact | SHA-512 | Notes |
| --- | --- | --- |
| `versions/ai-osi-stack-v5.pdf` | `87d0414872ab29393ee46e585c7dd49bf30c7c13bcf2637ff2bd52078c558b4b6a4598c0b3ffbebfe87588c391f9a002cac4f636efa392df04275266fee08156` | Canonical PDF reference edition |
| `dist/ai-osi-stack-v5.0.0.tar.gz` | `[pending canonical publication – hashes will be issued in v5 release]` | Deterministic source bundle produced via `ops/release/mk-dist.sh` |
| Additional notarized PDF annexes | `[pending canonical publication – hashes will be issued in v5 release]` | Record hash and OpenTimestamps proof when available |

Signing and hash publication will occur once the v5 release is sealed; until then, placeholders remain for visibility only.

Hashes must be updated immediately after a new canonical release. Every update should be signed using Daniel P. Madden's detached signatures stored alongside the artifacts once the signing ceremony is complete.

## Repository-of-Record & Domain-of-Record

- **Repository:** https://github.com/danielpmadden/ai-osi-stack
- **Domain:** https://aiosi.org
- **Supersedes:** v4.x advisory publications (archived in `/versions/legacy/`)

## Update Workflow

1. `# Real signing deferred until v5 final release`
   Run `./ops/release/mk-dist.sh <version>` to create the deterministic archive under `dist/` once sealing begins.
2. `# Real signing deferred until v5 final release`
   Execute `./ops/release/sign.sh dist/ai-osi-stack-<version>.tar.gz versions/ai-osi-stack-<version>.pdf` to create detached signatures and refresh this notice.
3. Commit the updated hashes and `.asc` signature files.
4. Notarize resulting hashes using the OpenTimestamps guidance in `ops/release/open-timestamps.md` and append the proof references below when available.

## Timestamp Proofs

| Artifact | OpenTimestamps Proof | Notes |
| --- | --- | --- |
| Pending | — | Run `ots stamp` as described in the release documentation. |

## Verification Checklist

- Validate signature files with `./ops/release/verify.sh`.
- Compare SHA-512 hashes recorded above with locally generated values.
- Confirm release tags are signed and protected via branch protection rules.

Daniel P. Madden reserves the right to revoke non-canonical mirrors. Forks are informational only and cannot claim canonical status without signed delegation.
