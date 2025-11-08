# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from pathlib import Path
import re

SCHEMA_PURPOSE = {
    "schemas/aeip-1-3.jsonld": "Defines AEIP lifecycle stages and minimum evidence for phases 1–3",
    "schemas/aeip-template.yaml": "Blueprint for composing AEIP assurance packages",
    "schemas/aeip/aeip-frame-schema.json": "Maps AEIP records to Stack layers and oversight checkpoints",
    "schemas/aeip/ccm-schema.json": "Structures ethical charter commitments and change tracking",
    "schemas/aeip/civic-charter-schema.json": "Captures civic mandate terms and accountability triggers",
    "schemas/aeip/gds-schema.json": "Summarises governance design decisions for publication",
    "schemas/aeip/incident-report-schema.json": "Standard incident reporting payload for remediation workflows",
    "schemas/aeip/instruction-log-schema.json": "Logs instruction sequences and control evidence",
    "schemas/aeip/modelcard-schema.json": "Collects model development metadata for regulated releases",
    "schemas/aeip/tecl-schema.json": "Records trust and engagement covenant ledgers",
    "schemas/ccm-template.yaml": "Template for civic charter maintenance and consultations",
    "schemas/decision-rationale-record.jsonld": "Documents deployment and integration justifications",
    "schemas/drr-schema.yaml": "Defines data request and retention stewardship evidence",
    "schemas/governance-decision-summary.jsonld": "Publishes formal governance decisions for civic review",
    "schemas/governance/ai-assisted-drafting.jsonld": "Discloses AI-assisted policy drafting contributions",
    "schemas/integrity-ledger-entry.jsonld": "Registers integrity ledger attestations across layers",
    "schemas/interpretive-trace-package.jsonld": "Packages contextual evidence for interpretive analysis",
    "schemas/modelcard-template.yaml": "Template for extended model cards and evaluation details",
    "schemas/oam-schema.yaml": "Oversight assessment memorandum structure",
    "schemas/oversight-audit-memo.jsonld": "Captures oversight audit findings and remediation directives",
    "schemas/persona/persona-manifest.jsonld": "Defines persona capabilities, safeguards, and limits",
    "schemas/persona/registry.jsonld": "Indexes approved personas and stewardship assignments",
    "schemas/svc/semantic-registry.jsonld": "Tracks semantic definitions and mitigates vocabulary drift",
    "schemas/therapy/credential-verification.jsonld": "Verifies clinician credentials for therapy technology",
}

pattern = re.compile(r"schemas/[A-Za-z0-9_\-/\.]+")
files = list(Path('source/chapters').glob('*.tex')) + list(Path('source/interpretive').glob('*.tex'))
reference_map: dict[str, set[str]] = {}

for path in files:
    text = path.read_text()
    matches = set(pattern.findall(text))
    if not matches:
        continue
    stem = path.stem
    match = re.match(r"chapter-([0-9a-zA-Z]+)", stem)
    if not match:
        continue
    chapter_id = match.group(1).upper()
    label = f"Ch.{chapter_id}"
    for schema in matches:
        reference_map.setdefault(schema, set()).add(label)

rows = []
for schema in sorted(reference_map):
    purpose = SCHEMA_PURPOSE.get(schema, "Purpose pending documentation")
    chapters = sorted(reference_map[schema], key=lambda value: [int(chunk) if chunk.isdigit() else chunk for chunk in re.findall(r"\d+|\D+", value.replace('Ch.', ''))])
    rows.append((schema, purpose, ", ".join(chapters)))

header = "| Schema | Purpose | Referenced In |\n|---------|----------|---------------|"
lines = ["# Schema Cross-Reference", "", header]
for schema, purpose, refs in rows:
    lines.append(f"| {schema} | {purpose} | {refs} |")

Path("schemas/readme.md").write_text("\n".join(lines) + "\n")
