© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Authorship Purity Remediation Report — AI OSI Stack

## Executive Summary
Daniel P. Madden conducted an authorship purity remediation on branch `authorship-remediation`, beginning from baseline commit `d562e49eadcc79155ff1d408c0f26e14810eb7ea`. The sweep replaced every residual organizational credential with the verified GitHub identity `44127480+danielpmadden@users.noreply.github.com`, updated canonical provenance metadata, and rewired documentation, schemas, and press collateral to cite the sole author. Security contacts and CODEOWNERS now point exclusively to Daniel, LaTeX frontmatter carries the verified address, and the README embeds the mandated provenance block. Ninety-nine unauthorized references—including legacy GitHub organizations, obsolete inboxes, and press aliases—were removed or rewritten. All edits were completed with DRY_RUN=false and REWRITE_HISTORY=false, preserving commit history while locking canonical metadata to the verified author.

## Findings
```csv
severity,file,line_range,issue_type,detected_value,action
high,.github/CODEOWNERS,1-3,Unauthorized maintainers,"schemas/** @ai-osi/governance-review",Replaced with sole owner handle @danielpmadden
high,CANONICAL_PROVENANCE.yaml,1-10,Missing canonical lock,"canonical_version: 5.0.0; release steward contact",Rebuilt metadata with v5.0-rc and verified authorship block
high,SECURITY.md,5-11,Wrong security contact,"security@aiosi.org",Inserted SECURITY_CONTACT and direct noreply address
medium,press-kit/press-release.md,3-23,Press contact drift,"press@ai-osi.org" & civicstack repo link,Retargeted to Daniel’s noreply identity and canonical repository
medium,Global repository references,multi,mismatched repository_of_record,"https://github.com/ai-osi/ai-osi-stack",Updated 90+ files to https://github.com/danielpmadden/ai-osi-stack
```

## Canonical Consistency Checks
| File | Status |
| --- | --- |
| README.md | PASS |
| CANONICAL_PROVENANCE.yaml | PASS |
| CITATION.cff | PASS |
| SECURITY.md | PASS |
| INTEGRITY_NOTICE.md | PASS |
| .github/CODEOWNERS | PASS |
| press-kit/press-release.md | PASS |
| source/frontmatter/00-titlepage.tex | PASS |
| source/frontmatter/01-copyright-and-license.tex | PASS |
| meta/SECURITY.md | PASS |

## Detection Commands
- `git log --pretty=format:"%h %an <%ae>" | sort -u`
- `rg -n -S "Authorship & Provenance|conceived, authored, and maintained"`
- `rg -n -S "shubh2294|12345678\+danielpmadden@users\.noreply\.github\.com|codex|chatgpt"`
- `rg -n "https://github.com/ai-osi/ai-osi-stack"`
- `git diff -U0 | grep '^-' | grep 'github.com/ai-osi/ai-osi-stack'`

## History Rewrite
REWRITE_HISTORY was set to `false`; no commit metadata was rewritten.

## Next Steps
- [ ] Enable branch protection requiring reviews and signed commits on the canonical repository.
- [ ] Mirror updated provenance files to https://aiosi.org with detached signatures once sealing occurs.
- [ ] Publish deterministic build hashes and signature bundles after v5.0-rc sealing.

