© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Operations Runbook

This guide summarizes local commands required to reproduce the CI pipeline and verify canonical releases.

## Environment Setup

1. Install Node.js >= 18.18.0 and enable `corepack`.
2. Install Python 3.12 with `pip`.
3. Install auxiliary tools: `syft`, `trivy`, `gitleaks`, `jq`, and `git`.

## Baseline Commands

```bash
npm ci
npm run lint
npm test
pytest
./ops/inventory/inventory.sh
./ops/sbom/syft-sbom.sh
./ops/sbom/trivy-scan.sh
./ops/secrets/run-gitleaks.sh
./ops/license/scan-licenses.sh
```

Upload the generated artifacts (`ops/inventory/*.json`, `ops/sbom/*.json`, `ops/license/dependency-licenses.csv`) when filing governance reviews or release PRs.

## Release Preparation

1. Run `./ops/release/mk-dist.sh <version>`.
2. Execute `./ops/release/sign.sh dist/ai-osi-stack-v<version>.tar.gz versions/ai-osi-stack-v5.pdf`.
3. Verify signatures via `./ops/release/verify.sh ...`.
4. Update `INTEGRITY_NOTICE.md` with new hashes and commit the changes.
5. Optionally notarize hashes using the steps in `ops/release/open-timestamps.md`.

## Governance Validators

- `npm run validate:aeip` validates AEIP receipts against the JSON schemas.
- `npm run validate:governance` validates civic charter, GDS, and incident schemas and warns if no receipts reference them.
- `pytest tests/aeip-lifecycle-validator.py` ensures lifecycle transitions remain intact.

## Containerized Execution

Use the hardened image for reproducible validation:

```bash
docker compose run --rm validator
```

This runs AEIP validators and pytest inside a non-root, read-only container.
