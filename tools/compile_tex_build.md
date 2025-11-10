# Build Instructions — ai-osi-stack-v5-master.tex

## Prerequisites
- Pandoc 3.0 or newer
- TeX Live or another LaTeX distribution with `xelatex`
- GNU Make (optional but recommended)

## Compilation Steps
1. Ensure all markdown sources under `layers/` and `layers/appendices/` are updated.
2. Run the following command to concatenate and convert to LaTeX:
   ```bash
   pandoc \
     README.md \
     layers/00_civic_mandate.md \
     layers/01_physical_compute_substrate.md \
     layers/02_data_stewardship.md \
     layers/03_model_development.md \
     layers/04_instruction_control.md \
     layers/05_reasoning_exchange.md \
     layers/06_deployment_integration.md \
     layers/07_governance_publication.md \
     layers/08_civic_participation.md \
     layers/09_epistemic_infrastructure_protocol.md \
     layers/10_governance_transport_maturity_model.md \
     layers/11_implementation_verification.md \
     layers/12_strategic_resilience_risk_mitigation.md \
     layers/appendices/appendix_a_normative_vocabulary.md \
     layers/appendices/appendix_b_escalation_remediation.md \
     layers/appendices/appendix_c_changelog.md \
     layers/appendices/appendix_d_glossary.md \
     layers/appendices/appendix_e_sources_provenance.md \
     layers/appendices/appendix_f_acknowledgments.md \
     layers/appendices/appendix_g_about_author.md \
     layers/appendices/appendix_h_authorship_statement.md \
     layers/appendices/appendix_i_custodial_metadata.md \
     -s -o ai-osi-stack-v5-master.tex
   ```
3. Compile the LaTeX source into PDF:
   ```bash
   xelatex ai-osi-stack-v5-master.tex
   ```
4. Repeat the `xelatex` command until references are resolved (typically twice).
5. Store the generated PDF under `dist/` or publish alongside the canonical repository release.

---
*License: Creative Commons Attribution–NonCommercial–NoDerivatives 4.0 International.*
