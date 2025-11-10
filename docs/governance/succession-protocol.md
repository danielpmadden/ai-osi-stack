© 2025 Daniel P. Madden — Custodial Author
AI OSI Stack v5.0-open-core (Civic Standard Edition)

© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Custodianship Succession Protocol

1. **Trigger** — custodianship transfer initiated via CRO directive.
2. **Preparation** — outgoing custodian runs `tools/update-custodian.py` with successor details.
3. **Key Rotation** — successor generates new signing key and submits fingerprint.
4. **Dual Approval** — CRO and governance steward sign change control record in `govspine/control/change-control-records/`.
5. **Continuity Update** — update `docs/public_keys.json` and regenerate CRO dashboard.
6. **Knowledge Transfer** — schedule 2 working sessions covering AEIP automation, incident drill runbooks, and communication templates.
7. **Verification** — pre-commit hook ensures no registry entry remains `vacant`.

Refer to `/continuity/manifest.json` for archival mirror locations and backup cadence.
