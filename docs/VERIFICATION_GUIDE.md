© 2025 Daniel P. Madden — Custodial Author
AI OSI Stack v5.0-open-core (Civic Standard Edition)

© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Verification Guide

This guide explains how to independently verify canonical releases, signatures, and governance receipts for the AI OSI Stack.

## 1. Clone the Repository

```bash
git clone https://github.com/danielpmadden/ai-osi-stack.git
cd ai-osi-stack
```

## 2. Verify Inventory

```bash
./ops/inventory/inventory.sh
jq '.files | length' ops/inventory/file-inventory.json
```

Compare with the published inventory from the release notes. Differences should be reviewed.

## 3. Validate Signatures (Deferred Until v5 Sealing)

1. Import the release PGP key (fingerprint in `CANONICAL_PROVENANCE.yaml`) once published.
2. Download the tarball and signatures from the GitHub Release after the sealing ceremony.
3. `# Real signing deferred until v5 final release`
   Run `./ops/release/verify.sh dist/ai-osi-stack-v5.0.0.tar.gz versions/ai-osi-stack-v5.pdf` when signatures are available.
4. Ensure hashes in `INTEGRITY_NOTICE.md` match the computed output after publication.

## 4. Validate AEIP Receipts

```bash
npm ci
npm run validate:aeip
npm run validate:governance
```

All receipts should pass without error; governance validator may emit warnings if no civic charter receipts are present.

## 5. Review SBOM and Vulnerability Scans

```bash
./ops/sbom/syft-sbom.sh
./ops/sbom/trivy-scan.sh
```

Inspect `ops/sbom/trivy-fs.txt` and `ops/sbom/trivy-sbom.txt` for high or critical vulnerabilities.

## 6. Optional: OpenTimestamps Proof

Follow `ops/release/open-timestamps.md` to verify that timestamp proofs match the recorded hashes.

By completing these steps you can confirm the provenance of the AI OSI Stack and rely on the canonical release for civic governance operations.
