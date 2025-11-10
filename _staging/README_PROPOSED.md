© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# AI OSI Stack: Civic Infrastructure for Accountable AI

The AI OSI Stack provides a civic-first governance framework that turns public
mandates into verifiable technical controls. This open-core distribution keeps
authoritative documentation, schemas, integrity ledgers, and lightweight audit
tools so regulators, researchers, and civic technologists can examine how
accountable AI systems are assembled.

## Repository Contents

- **`docs/`** – Plain-language briefs, policy explainers, and governance
overviews mapped to the OSI-inspired layers.
- **`schemas/`** – JSON and JSON-LD definitions for AEIP evidence records,
  governance decisions, and integrity manifests.
- **`ledger/`** – Sample civic ledger entries, integrity notices, and
  hermeneutic annotations illustrating accountable publication workflows.
- **`source/`** – LaTeX manuscripts for the canonical stack volumes and
  appendices used to produce release PDFs.
- **`legal/`** – Custodianship statements, license mapping, and provenance
  attestations supporting long-term stewardship.
- **`audits/`** – Historical audit trails and structure reviews showing how the
  stack has been assessed across releases.
- **`archive/` & `versions/`** – Prior tagged artifacts, including versioned
  PDFs and historical prototypes retained for context.
- **`_open_tools/`** – Minimal validation utilities (JSON parsing, provenance
  reporting, integrity guards) that rely only on open dependencies.
- **`meta/` & `press-kit/`** – Integrity manifests, communication packs, and
  reference materials for civic briefings.

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/danielpmadden/ai-osi-stack.git
   cd ai-osi-stack
   ```
2. **Create a Python environment for validators**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run the open validation helpers**
   ```bash
   python _open_tools/validate_json.py
   python _open_tools/version-check.py
   ```
4. **Build the canonical documents (optional)**
   - Install a LaTeX toolchain (e.g., TeX Live) or run a container with
     `latexmk` available.
   - From the repository root execute:
     ```bash
     cd source
     latexmk -pdf ai-osi-stack-v5.tex
     ```
   - Generated PDFs publish under `versions/` alongside integrity hashes.

## How to Use These Materials

- Map civic mandates to AEIP schemas to trace obligations through each layer.
- Reference the ledger samples to design your own accountable disclosure
  pipeline.
- Leverage `_open_tools/` to spot JSON or provenance drift before releasing
  updates.
- Consult `legal/` for authorship, custodianship, and licensing provenance when
  citing or adapting material.

## License and Citation

- **Code, configuration, and automation**: Apache License 2.0.
- **Documentation and narrative content**: Creative Commons BY-SA 4.0.
- Cite as: *Madden, Daniel P. — AI OSI Stack (v5.1-open-core), 2025. GitHub:
  danielpmadden/ai-osi-stack.*

## Looking for the commercial suite?

Governance Control Tower and related operational runtimes are maintained
privately to protect closed IP and deployment partners. Contact the custodian
via the repository issue tracker or provenance records for commercial
engagements.
