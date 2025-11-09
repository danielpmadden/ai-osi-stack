<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Security Policy

## Reporting Vulnerabilities

Email **security@aiosi.org** with the subject `AI OSI Stack Security Disclosure`. If you require encryption, use the project PGP key:

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
- Use `ops/secrets/run-gitleaks.sh` locally to ensure no accidental secrets are shared.

## Integrity Requirements

- Canonical artifacts and their hashes are tracked in [`INTEGRITY_NOTICE.md`](INTEGRITY_NOTICE.md).
- Signed releases must be verified via `ops/release/verify.sh` before public disclosure.
- Advisory mirrors **must not** be treated as canonical unless explicitly re-signed.

Implementers who fork or deploy the Stack MUST publish their own signing keys once v5 is sealed and renew fingerprints for each derivative release.

## Scope

This policy covers all source code (Apache-2.0), documentation (CC BY-SA 4.0), schemas, governance receipts, and operational scripts. Synthetic datasets do not contain personal information.

## Emergency Contact

For critical vulnerabilities affecting production deployments, use the PGP key above and include `URGENT` in the subject. The on-call release steward will respond within 12 hours.
