# Custodianship Succession Protocol

1. **Trigger** — custodianship transfer initiated via CRO directive.
2. **Preparation** — outgoing custodian runs `tools/update-custodian.py` with successor details.
3. **Key Rotation** — successor generates new signing key and submits fingerprint.
4. **Dual Approval** — CRO and governance steward sign change control record in `governance/change_control_records/`.
5. **Continuity Update** — update `docs/public_keys.json` and regenerate CRO dashboard.
6. **Knowledge Transfer** — schedule 2 working sessions covering AEIP automation, incident drill runbooks, and communication templates.
7. **Verification** — pre-commit hook ensures no registry entry remains `vacant`.

Refer to `/continuity/manifest.json` for archival mirror locations and backup cadence.
