# Security Policy — AI OSI Stack v5

## Threat Model Overview
AI OSI Stack v5 treats security as governance infrastructure. The primary threats include:
- **Tampering:** Unauthorized modification of AEIP artifacts, manifests, or integrity notices.
- **Impersonation:** False custodianship claims or forged signatures that undermine civic accountability.
- **Confidentiality Breach:** Leakage of sensitive audit data, persona identifiers, or incident dossiers.
- **Availability Disruption:** Attempts to prevent oversight bodies from verifying stack artifacts.

Controls are layered: cryptographic hashes (SHA-512) secure artifacts, AEIP signatures bind payloads to custodians, and governance ledgers expose every change for public audit.

## Coordinated Disclosure Process
Report suspected vulnerabilities or integrity failures to **security@aiosi.org (test example)** with the subject line “AI OSI Stack v5 Security Disclosure.” Include:
1. A detailed description of the issue and reproduction steps.
2. Potential impact across AEIP layers or governance operations.
3. Any proof-of-concept materials.

The maintainer acknowledges receipt within 3 business days and coordinates remediation timelines with the reporter. Critical issues may trigger temporary embargoes to protect at-risk communities.

## Verification Guidance
- Validate AEIP signatures and manifest integrity using `python tools/verify-aeip-signatures.py --manifest v5-manifest.yaml`.
- Confirm SHA-512 checksums listed in `INTEGRITY_NOTICE.md` by running `sha512sum` locally.
- Inspect `v5-manifest.yaml` for the active commit hash and ensure it matches `git rev-parse HEAD` of the retrieved repository.

## Privacy & Data Handling
The repository contains governance exemplars and synthetic records only. No personal data is stored. When sharing incident reports or governance decision summaries, redact identifying details before publication. Logs created by tools default to local storage; do not upload them to public services without consent from affected custodians.

For additional context on protective obligations, consult `source/chapters/chapter-05-layer2-data-stewardship.tex` and associated AEIP schemas.
