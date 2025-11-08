# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from pathlib import Path

from .audit_data import AUDIT_DATA

OUTPUT_DIR = Path("audits")
OUTPUT_DIR.mkdir(exist_ok=True)

SECTION_LABELS = [
    ("strengths", "Strengths"),
    ("gaps", "Gaps"),
    ("clarifications", "Recommended clarifications or additional clauses"),
    ("missing_refs", "Missing schema cross-references"),
    ("plain_topics", "Suggested plain-language paragraph topics"),
]

for key, data in AUDIT_DATA.items():
    filename = OUTPUT_DIR / f"{key}-audit.md"
    lines = [f"# {data['title']} Audit", ""]
    for field, heading in SECTION_LABELS:
        lines.append(f"## {heading}")
        for item in data.get(field, []):
            lines.append(f"- {item}")
        if not data.get(field):
            lines.append("- None identified.")
        lines.append("")
    filename.write_text("\n".join(lines).strip() + "\n")
