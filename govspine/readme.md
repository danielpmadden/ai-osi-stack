<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Governance Spine Evidence Store

This directory tree captures signed evidence manifests that correspond to each
layer of the AI OSI Governance Spine. Automation workflows populate the
subdirectories and ensure that each manifest conforms to the schemas in
`schemas/aeip/`.

| Directory | Layer | Contents |
|-----------|-------|----------|
| `charter/` | L0 | Civic charter manifest and rendered PDF |
| `compute/` | L1 | Trusted Execution & Compute Logs (TECL) |
| `data/` | L2 | Curated data stewardship manifests |
| `models/` | L3 | Model cards and reproducibility metadata |
| `control/` | L4 | Instruction and override logs |
| `aeip/` | L4–L7 | Aggregated AEIP frames |
| `deployment/` | L6–L7 | Governance Decision Summaries and incident reports |

Refer to `.github/workflows/*.yml` for the automation hooks that maintain these
manifests as by-products of normal development activity.
