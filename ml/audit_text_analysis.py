"""Utility for assessing tone and modality in governance documentation.

The module prefers scikit-learn for sentence classification but gracefully
falls back to a rules-based approach when the dependency is unavailable.
This keeps the audit runnable in network-constrained environments while
still encouraging full installations via ``ml/requirements.txt``.
"""
from __future__ import annotations

import argparse
import pathlib
import re
from dataclasses import dataclass
from typing import Iterable, List, Sequence

try:  # Optional, preferred path
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import Pipeline
except Exception:  # pragma: no cover - used only when sklearn missing
    CountVectorizer = None  # type: ignore[assignment]
    LogisticRegression = None  # type: ignore[assignment]
    Pipeline = None  # type: ignore[assignment]

_MODAL_TERMS = {"must", "shall", "should", "required", "obligated"}
_TRAINING_DATA: Sequence[tuple[str, str]] = (
    ("Custodians SHALL publish ledger updates within the statutory window.", "normative"),
    ("Stewards MUST document refusal logic before deployment.", "normative"),
    ("Board liaisons SHOULD brief civic partners weekly when incidents occur.", "normative"),
    ("Update Plan 8 emphasises transparency without surveillance pressure.", "descriptive"),
    ("The analytics portal aggregates persona manifests and ledger excerpts.", "descriptive"),
    ("This chapter documents historical stewardship discussions for context.", "descriptive"),
    ("The civic glossary highlights definitions that tend to drift in public debate.", "descriptive"),
    ("AEIP handshakes SHALL include temporal integrity seals and witness countersigns.", "normative"),
    ("Governance offices MUST track publication cadence across all layers.", "normative"),
    ("Persona architects SHOULD cross-check refusal scripts against Update Plan guidance.", "normative"),
)


@dataclass
class SentenceAssessment:
    """Result of classifying a sentence for tonal analysis."""

    sentence: str
    predicted_label: str
    confidence: float
    modal_terms: List[str]


class NormativeToneAnalyzer:
    """Detects normative vs descriptive tone in sentences."""

    def __init__(self) -> None:
        self._has_sklearn = CountVectorizer is not None and LogisticRegression is not None
        if self._has_sklearn:
            texts, labels = zip(*_TRAINING_DATA)
            self._pipeline = Pipeline(
                steps=[
                    (
                        "vectorizer",
                        CountVectorizer(lowercase=True, ngram_range=(1, 2), stop_words="english"),
                    ),
                    ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced")),
                ]
            )
            self._pipeline.fit(texts, labels)
        else:
            self._pipeline = None

    @staticmethod
    def _split_sentences(text: str) -> List[str]:
        cleaned = re.sub(r"\s+", " ", text)
        parts = re.split(r"(?<=[.!?])\s+", cleaned)
        return [p.strip() for p in parts if p.strip()]

    def classify(self, text: str) -> List[SentenceAssessment]:
        sentences = self._split_sentences(text)
        results: List[SentenceAssessment] = []
        if not sentences:
            return results
        if self._has_sklearn:
            probabilities = self._pipeline.predict_proba(sentences)  # type: ignore[union-attr]
            labels = self._pipeline.classes_  # type: ignore[union-attr]
            label_index = {label: idx for idx, label in enumerate(labels)}
            for sentence, dist in zip(sentences, probabilities):
                normative_score = dist[label_index["normative"]]
                predicted = "normative" if normative_score >= 0.5 else "descriptive"
                modal_terms = sorted(
                    {
                        token.lower()
                        for token in re.findall(r"[A-Za-z']+", sentence)
                        if token.lower() in _MODAL_TERMS
                    }
                )
                results.append(
                    SentenceAssessment(
                        sentence=sentence,
                        predicted_label=predicted,
                        confidence=normative_score if predicted == "normative" else 1 - normative_score,
                        modal_terms=modal_terms,
                    )
                )
            return results

        # Fallback heuristics: rely on modal terms to approximate normative tone.
        for sentence in sentences:
            modal_terms = sorted(
                {
                    token.lower()
                    for token in re.findall(r"[A-Za-z']+", sentence)
                    if token.lower() in _MODAL_TERMS
                }
            )
            predicted = "normative" if modal_terms else "descriptive"
            confidence = 0.8 if modal_terms else 0.2
            results.append(
                SentenceAssessment(
                    sentence=sentence,
                    predicted_label=predicted,
                    confidence=confidence,
                    modal_terms=modal_terms,
                )
            )
        return results


def load_documents(paths: Iterable[pathlib.Path]) -> List[dict[str, float | str]]:
    """Load documents and compute tonal statistics."""

    analyzer = NormativeToneAnalyzer()
    records: List[dict[str, float | str]] = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        assessments = analyzer.classify(text)
        if not assessments:
            continue
        normative = sum(1 for row in assessments if row.predicted_label == "normative")
        descriptive = len(assessments) - normative
        modal_hits = sum(len(row.modal_terms) for row in assessments)
        records.append(
            {
                "path": str(path),
                "total_sentences": len(assessments),
                "normative_sentences": normative,
                "descriptive_sentences": descriptive,
                "modal_term_hits": modal_hits,
                "modal_sentence_share": modal_hits / len(assessments),
                "avg_confidence": sum(row.confidence for row in assessments) / len(assessments),
            }
        )
    return records


def glob_paths(patterns: Sequence[str]) -> List[pathlib.Path]:
    files: List[pathlib.Path] = []
    for pattern in patterns:
        files.extend(pathlib.Path().glob(pattern))
    return sorted({path for path in files if path.is_file()})


def run_cli() -> None:
    parser = argparse.ArgumentParser(description="Analyse governance docs for normative tone")
    parser.add_argument(
        "--paths",
        nargs="+",
        default=("docs/**/*.md", "README.md"),
        help="Glob patterns of files to inspect (default: docs and README).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Limit output rows when printing to stdout (default: 20).",
    )
    args = parser.parse_args()
    paths = glob_paths(args.paths)
    records = load_documents(paths)
    if not records:
        print("No readable documents found for the provided patterns.")
        return
    for row in sorted(records, key=lambda r: r["modal_term_hits"], reverse=True)[: args.limit]:
        print(
            f"{row['path']}: normative={row['normative_sentences']} modal_share={row['modal_sentence_share']:.3f}"
        )


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    run_cli()
