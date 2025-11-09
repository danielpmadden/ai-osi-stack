<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Security Policy — AI OSI Stack v5

## Threat Model Overview
AI OSI Stack v5 treats security as governance infrastructure. The primary threats include:
- **Tampering:** Unauthorized modification of AEIP artifacts, manifests, or integrity notices.
- **Impersonation:** False custodianship claims or forged signatures that undermine civic accountability.
- **Confidentiality Breach:** Leakage of sensitive audit data, persona identifiers, or incident dossiers.
- **Availability Disruption:** Attempts to prevent oversight bodies from verifying stack artifacts.

Controls are layered: advisory checksum guidance supports provenance tracking, AEIP records bind payloads to custodians, and governance ledgers expose every change for public audit.

## Coordinated Disclosure Process
Report suspected vulnerabilities or integrity failures to **44127480+danielpmadden@users.noreply.github.com** with the subject line “AI OSI Stack v5 Security Disclosure.” Include:
1. A detailed description of the issue and reproduction steps.
2. Potential impact across AEIP layers or governance operations.
3. Any proof-of-concept materials.

The maintainer acknowledges receipt within 3 business days and coordinates remediation timelines with the reporter. Critical issues may trigger temporary embargoes to protect at-risk communities.

## Verification Guidance
- Follow the advisory workflow in `meta/INTEGRITY_NOTICE.md` to record personal SHA-512 (or equivalent) checksums.
- Inspect `meta/v5-manifest.yaml` for the advisory integrity metadata and confirm it references the expected canonical version.
- Store your checksum log with the retrieved artifacts so future reviewers can confirm provenance.

## Privacy & Data Handling
The repository contains governance exemplars and synthetic records only. No personal data is stored. When sharing incident reports or governance decision summaries, redact identifying details before publication. Logs created by tools default to local storage; do not upload them to public services without consent from affected custodians.

For additional context on protective obligations, consult `source/chapters/chapter-05-layer2-data-stewardship.tex` and associated AEIP schemas.

## Editorial Expansion (Chs 19A–24)
The interpretive chapters introduced in Part IV add no executable code, cryptographic primitives, or automated tooling. They consist solely of narrative and normative text that extends governance guidance into semantics, intimacy, care, and meta-authorship. No security posture changes are required; advisory verification workflows and manifests remain the recommended path for provenance review.
