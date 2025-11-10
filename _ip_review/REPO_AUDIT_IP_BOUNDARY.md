# Repository Audit: Open-Core IP Boundary Alignment

**Date:** 2025-11-09  
**Auditor:** Daniel P. Madden (custodial review)

## Objectives

1. Confirm repository contents reflect the open-core governance layer only.  
2. Document exclusion of proprietary runtimes (Governance Control Tower™, AEIP runtime, ledger engines, analytics dashboards).  
3. Refresh licensing, provenance, and README posture to prevent boundary drift.

## Actions Completed

- Normalised repository messaging to "AI OSI Stack — Open-Core Civic Layer" and enumerated the civic scope versus proprietary runtimes.  
- Added `LEGAL/IP-BOUNDARIES.md` and `LEGAL/TRADEMARK-NOTE.md` to publish the IP matrix and trademark notice.  
- Updated README, provenance metadata, changelog, and NOTICE to reference Apache-2.0 / CC BY-SA licensing and clarify the governance lock status.  
- Expanded `.gitignore` to exclude private workspaces (`analytics`, `backend`, `govspine`, `protocol`, `ml`, `ops`, `tools`, `tests`, `commercial`, `briefing`).  
- Generated `_staging/README_IP_BOUNDARY.md` for release packaging and `CHANGELOG_v5.1-open-core.md` capturing the alignment work.

## Outstanding Considerations

- Proprietary runtimes remain unpublished pending Governance Control Tower™ release; audit artifacts should continue to flag any regression toward runtime inclusion.  
- Historical documents referencing private workspaces should note their archival context when revised in future passes.  
- Integrity review for the canonical v5 publication remains underway; lock release contingent on governance verification.

