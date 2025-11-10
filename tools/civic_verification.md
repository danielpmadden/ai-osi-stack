# Civic Verification Routine (Public Execution)

## Objective
Provide a reproducible procedure for the public to validate claims of conformity with the AI OSI Stack v5 canonical specification.

## Steps
1. Retrieve the latest canonical release from the main branch of the AI-OSI-v5-canonical repository.
2. Confirm the presence and hash of `foundation/ai_osi_v4_source/ai-osi-stack-v4-master.pdf` to verify provenance.
3. Execute `python tools/validate_crosswalk.py` to ensure crosswalk mappings reference existing layer files.
4. Review publication logs in `CHANGELOG.md` for the ratification date and summary of modifications.
5. Submit verification attestations, including hash outputs and test logs, to the civic oversight portal.

---
*License: Creative Commons Attribution–NonCommercial–NoDerivatives 4.0 International.*
