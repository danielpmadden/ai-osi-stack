"""Generate markdown reports from governance ML analyses."""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
from typing import Iterable, Sequence

if __package__ is None or __package__ == "":  # pragma: no cover
    import sys

    sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

from ml.audit_text_analysis import glob_paths, load_documents
from ml.schema_coherence import analyse_schema_directory, clusters_to_rows


def _format_markdown_table(rows: Iterable[dict[str, object]], columns: Sequence[str]) -> str:
    rows = list(rows)
    if not rows:
        return "_No qualifying records found._"
    header = "| " + " | ".join(columns) + " |"
    divider = "| " + " | ".join(["---"] * len(columns)) + " |"
    lines = [header, divider]
    for row in rows:
        line = "| " + " | ".join(str(row.get(col, "")) for col in columns) + " |"
        lines.append(line)
    return "\n".join(lines)


def build_report(doc_patterns: Sequence[str], schema_patterns: Sequence[str], limit: int = 5) -> str:
    doc_paths = glob_paths(doc_patterns)
    doc_records = load_documents(doc_paths)
    schema_clusters = analyse_schema_directory(schema_patterns)
    cluster_rows = clusters_to_rows(schema_clusters)

    doc_rows = sorted(
        (
            {
                "Document": record["path"],
                "Normative Rate": f"{(record['normative_sentences'] / record['total_sentences']):.3f}",
                "Modal Share": f"{record['modal_sentence_share']:.3f}",
                "Modal Hits": int(record["modal_term_hits"]),
            }
            for record in doc_records
        ),
        key=lambda row: (float(row["Modal Share"]), float(row["Normative Rate"])),
        reverse=True,
    )[:limit]

    cluster_rows = sorted(cluster_rows, key=lambda row: row["field_count"], reverse=True)[:limit]

    timestamp = dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    report_lines = [
        "<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->",
        "",
        "# Schema Coherence & Normative Language Audit",
        "",
        f"_Generated: {timestamp}_",
        "",
        "## Normative Language Pulse",
        "The table surfaces the documents with the highest share of modal (MUST/SHALL/SHOULD) language.",
        _format_markdown_table(doc_rows, ("Document", "Normative Rate", "Modal Share", "Modal Hits")),
        "",
        "## Schema Field Clusters",
        "Field names are vectorised with TF-IDF character n-grams when the scikit-learn stack is available;"
        " otherwise a prefix-based heuristic groups related terms.",
        _format_markdown_table(
            (
                {
                    "Cluster": row["cluster_id"],
                    "Keywords": row["keywords"],
                    "Field Count": row["field_count"],
                    "Sample Fields": row["fields"],
                }
                for row in cluster_rows
            ),
            ("Cluster", "Keywords", "Field Count", "Sample Fields"),
        ),
    ]

    if not doc_records:
        report_lines.insert(6, "_No documents matched the normative tone analysis input set._")
    if not schema_clusters:
        report_lines.append(
            "\n_No schema fields were discovered. Check the provided patterns or confirm schema files are present._"
        )

    return "\n".join(report_lines)


def write_report(output_path: pathlib.Path, content: str) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")


def run_cli() -> None:
    parser = argparse.ArgumentParser(description="Generate schema coherence markdown report")
    parser.add_argument(
        "--docs",
        nargs="+",
        default=("docs/**/*.md", "README.md"),
        help="Glob patterns for documentation to analyse.",
    )
    parser.add_argument(
        "--schemas",
        nargs="+",
        default=("schemas/**/*.json", "schemas/**/*.jsonld"),
        help="Glob patterns for schema files.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=8,
        help="Maximum rows to include per table in the markdown output.",
    )
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        default=pathlib.Path("audits/schema-coherence-report.md"),
        help="Destination markdown file.",
    )
    args = parser.parse_args()
    content = build_report(args.docs, args.schemas, limit=args.limit)
    write_report(args.output, content)
    print(f"Report written to {args.output}")


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    run_cli()
