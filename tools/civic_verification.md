Layer/Theme: tool_civic_verification
Version: v5.0-open-core
Purpose: Describe the civic verification routine for AI OSI v5.

# Civic Verification Checklist

This procedure SHALL be executed manually or with simple scripts. Record findings in Transparency Records.

1. **Scan for Banned Terms**
   - Search the repository for prohibited terms (AEIP, Control Tower, API, payload, signatures, ledger, dashboard).
   - Document findings and remediation steps.

2. **Validate Markdown Links**
   - Check that all internal and external links resolve.
   - Note any broken links with file paths and line references.

3. **Confirm Metadata Blocks**
   - Ensure every markdown file begins with Layer/Theme, Version, and Purpose lines using v5.0-open-core.
   - Flag files missing or misformatted metadata.

4. **Count Layer Files**
   - Verify there are nine layer files under `/layers/` and that names remain lowercase with underscores.

5. **List Transparency Records**
   - Compile every Transparency Record reference encountered during the review.
   - Summarize which layers or guides each record supports.

6. **Output Compliance Summary**
   - Produce a final note covering pass/fail status for each step, outstanding issues, and responsible stewards for follow-up.

Traceability

Keys: Tool=CivicVerification-v5, Review_Cycle=per_run
Open Civic Artefacts

- Transparency Record: Verification Run Log
- Transparency Record: Remediation Tracker

```sql
-- Copy code
SELECT artefact_id, run_date
FROM transparency_registry
WHERE tool = 'civic_verification';
```
