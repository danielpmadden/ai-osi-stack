© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# AI OSI Stack — Audit Summary (v5.1-open-core)

- **Files checked:** 430
- **Issues found:**
  - Residual references to private `govspine`, `ops`, and `analytics` runtimes in
    README copy, audit dossiers, historical prototypes, and build scripts.
  - Root `LICENSE` previously listed CC BY-NC-ND; replaced with Apache-2.0 /
    CC BY-SA split aligned with custodial policy.
  - `_open_tools/` utilities lacked SPDX headers and functional validation logic.
  - Provenance metadata (`CANONICAL_PROVENANCE.yaml`) still reported v5.0-rc.
- **Issues fixed in this pass:**
  - Updated `LICENSE`, `_open_tools/`, and `CANONICAL_PROVENANCE.yaml` to reflect
    `v5.1-open-core` policy and tooling.
  - Authored `_staging/README_PROPOSED.md` and `_staging/CHANGELOG_v5.1.md` for
    publication after stakeholder review.
- **Suggested README structure:** Mission overview → repository contents →
  getting started (clone, Python env, validators, optional LaTeX build) → usage
  guidance → license & citation → commercial contact note. Draft available in
  `_staging/README_PROPOSED.md`.
- **Recommended next tag:** `v5.1-open-core` once README, manifests, and directory
  moves are completed per `_ip_review/REORG_PLAN.md`.
