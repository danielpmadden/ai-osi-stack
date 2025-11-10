© 2025 Daniel P. Madden — Custodial Author
AI OSI Stack v5.0-open-core (Civic Standard Edition)

© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Security Policy

## Reporting Vulnerabilities

SECURITY_CONTACT: 44127480+danielpmadden@users.noreply.github.com

Email **44127480+danielpmadden@users.noreply.github.com** with the subject `AI OSI Stack Security Disclosure`. If you require encryption, use the project PGP key:

```
Fingerprint: [pending release fingerprint]
Key URL: https://aiosi.org/pgp/ai-osi-stack-security.asc
```

Acknowledge receipt within **3 business days** and coordinate remediation timelines with the release steward. Please include:

- Impacted components and AEIP layers.
- Reproduction steps or proof-of-concept.
- Suggested mitigations or compensating controls.
- Whether the issue affects published signed artifacts.

## Coordinated Disclosure Expectations

- Do not publicly disclose details until a mutually agreed remediation window has elapsed.
- Avoid submitting third-party personal data in reports.
- Use local secret-scanning tools (e.g., gitleaks) before submitting reports to avoid leaking credentials.

## Integrity Requirements

- Canonical artifacts, verification notes, and advisory hashes are tracked in [`INTEGRITY_NOTICE.md`](INTEGRITY_NOTICE.md). Follow its instructions to confirm provenance and validate signed releases.
- Signed releases must be verified using custodial release scripts before public disclosure.
- Advisory mirrors **must not** be treated as canonical unless explicitly re-signed.

Implementers who fork or deploy the Stack MUST publish their own signing keys once v5 is sealed and renew fingerprints for each derivative release.

## Scope

This policy covers all source materials, documentation, schemas, governance receipts, and validator-lite utilities distributed with the repository under Apache-2.0 (code) and CC BY-SA 4.0 (documentation). Proprietary runtimes—including Governance Control Tower™, AEIP runtime services, ledger engines, analytics dashboards, and related operational tooling—are out of scope and remain private.

## Non-Liability and Good-Faith Cooperation

The maintainer is not responsible for any damages, misuse, or derivative actions by third parties. Security researchers and implementers engaging with the Stack agree to act in good faith, respect the custodial mission, and coordinate remediation transparently.

## Emergency Contact

For critical vulnerabilities affecting production deployments, use the PGP key above and include `URGENT` in the subject. The on-call release steward will respond within 12 hours.
