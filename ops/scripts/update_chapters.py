# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from pathlib import Path

from .triple_register_data import CHAPTER_DATA


def format_enforcement_list(items: list[str]) -> str:
    if not items:
        return "[]"
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return ", ".join(items[:-1]) + f", and {items[-1]}"


def insert_triple_register(text: str, info: dict[str, object]) -> str:
    marker = "\\subsection*{Triple Register}"
    if marker in text:
        return text
    first_idx = text.find("\\narrative{")
    if first_idx == -1:
        first_idx = text.find("\\section")
        if first_idx == -1:
            raise ValueError("Unable to locate insertion point")
    brace_start = text.find("{", first_idx)
    if brace_start == -1:
        raise ValueError("Unable to locate opening brace")
    depth = 1
    i = brace_start + 1
    while i < len(text) and depth:
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
        i += 1
    insert_pos = i
    narrative = info["narrative_intent"]
    clauses = info["normative_clauses"]
    summary = info["plain_summary"]
    triple_lines = [
        "\\subsection*{Triple Register}",
        f"\\textbf{{Narrative Intent:}} {narrative}",
        "\\textbf{Normative Clauses:}",
        "\\begin{itemize}",
    ]
    for clause in clauses:
        triple_lines.append(f"\\item {clause}")
    triple_lines.extend([
        "\\end{itemize}",
        f"\\textbf{{Plain-Speak Summary:}} {summary}",
        "",
    ])
    triple_block = "\n".join(triple_lines)
    return text[:insert_pos] + "\n\n" + triple_block + text[insert_pos:]


def insert_enforcement(text: str, info: dict[str, object]) -> str:
    marker = "\\subsection*{Verification and Enforcement}"
    if marker in text:
        return text
    schemas = info.get("enforcement_schemas", [])
    schema_text = format_enforcement_list(schemas)
    enforcement_block = (
        "\\n\\subsection*{Verification and Enforcement}\n"
        f"Conformance is evidenced through artefacts {schema_text} and corresponding AEIP audit records.\n"
    )
    clear_idx = text.rfind("\\clearpage")
    if clear_idx != -1:
        return text[:clear_idx] + enforcement_block + text[clear_idx:]
    return text + enforcement_block


def process_file(path: str, info: dict[str, object]) -> None:
    file_path = Path(path)
    text = file_path.read_text()
    text = insert_triple_register(text, info)
    text = insert_enforcement(text, info)
    file_path.write_text(text)


for chapter, data in CHAPTER_DATA.items():
    process_file(chapter, data)

