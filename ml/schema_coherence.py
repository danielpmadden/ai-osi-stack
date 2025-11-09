"""Cluster JSON schema field names to surface duplication or drift."""
from __future__ import annotations

import argparse
import json
import pathlib
from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence

try:  # Preferred path
    import numpy as np
    from sklearn.cluster import KMeans
    from sklearn.feature_extraction.text import TfidfVectorizer
except Exception:  # pragma: no cover - fallback when ML stack missing
    np = None  # type: ignore[assignment]
    KMeans = None  # type: ignore[assignment]
    TfidfVectorizer = None  # type: ignore[assignment]


@dataclass
class SchemaCluster:
    """Container for clustered schema field names."""

    cluster_id: int
    keywords: List[str]
    fields: List[str]


def _extract_field_names(payload: object, prefix: str = "") -> List[str]:
    names: List[str] = []
    if isinstance(payload, dict):
        for key, value in payload.items():
            if key.startswith("@"):
                continue
            current = f"{prefix}.{key}" if prefix else key
            names.append(current)
            names.extend(_extract_field_names(value, current))
    elif isinstance(payload, list):
        for index, item in enumerate(payload):
            child_prefix = f"{prefix}[{index}]" if prefix else str(index)
            names.extend(_extract_field_names(item, child_prefix))
    return names


def collect_schema_terms(paths: Iterable[pathlib.Path]) -> List[str]:
    terms: List[str] = []
    for path in paths:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
        names = _extract_field_names(payload)
        terms.extend(names)
    return terms


def _cluster_with_sklearn(terms: Sequence[str], n_clusters: int) -> List[SchemaCluster]:
    vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(3, 5))
    matrix = vectorizer.fit_transform(terms)
    cluster_count = min(n_clusters, matrix.shape[0]) or 1
    model = KMeans(n_clusters=cluster_count, random_state=42, n_init="auto")
    labels = model.fit_predict(matrix)
    vocab = np.array(vectorizer.get_feature_names_out())
    clusters: List[SchemaCluster] = []
    for cluster_id in range(cluster_count):
        mask = labels == cluster_id
        cluster_terms = [term for term, flag in zip(terms, mask) if flag]
        if not cluster_terms:
            continue
        centroid = model.cluster_centers_[cluster_id]
        top_indices = np.argsort(centroid)[-5:][::-1]
        keywords = [vocab[idx] for idx in top_indices]
        clusters.append(SchemaCluster(cluster_id=cluster_id, keywords=keywords, fields=cluster_terms))
    return clusters


def _cluster_with_prefix(terms: Sequence[str]) -> List[SchemaCluster]:
    groups: Dict[str, List[str]] = {}
    for term in terms:
        prefix = term.split(".")[0]
        groups.setdefault(prefix, []).append(term)
    clusters: List[SchemaCluster] = []
    for idx, (prefix, items) in enumerate(sorted(groups.items(), key=lambda kv: len(kv[1]), reverse=True)):
        keywords = [prefix[:5], prefix[-5:]] if prefix else ["root"]
        clusters.append(SchemaCluster(cluster_id=idx, keywords=keywords, fields=items))
    return clusters


def cluster_terms(terms: Sequence[str], n_clusters: int = 5) -> List[SchemaCluster]:
    if not terms:
        return []
    if KMeans is not None and np is not None and TfidfVectorizer is not None:
        return _cluster_with_sklearn(terms, n_clusters)
    return _cluster_with_prefix(terms)


def analyse_schema_directory(patterns: Sequence[str], n_clusters: int = 5) -> List[SchemaCluster]:
    paths = []
    for pattern in patterns:
        paths.extend(pathlib.Path().glob(pattern))
    unique_paths = sorted({p for p in paths if p.is_file()})
    terms = collect_schema_terms(unique_paths)
    return cluster_terms(terms, n_clusters=n_clusters)


def clusters_to_rows(clusters: Sequence[SchemaCluster]) -> List[dict[str, object]]:
    rows: List[dict[str, object]] = []
    for cluster in clusters:
        rows.append(
            {
                "cluster_id": cluster.cluster_id,
                "keywords": ", ".join(cluster.keywords),
                "field_count": len(cluster.fields),
                "fields": "; ".join(cluster.fields[:10]) + (" …" if len(cluster.fields) > 10 else ""),
            }
        )
    return rows


def run_cli() -> None:
    parser = argparse.ArgumentParser(description="Cluster schema field names")
    parser.add_argument(
        "--schemas",
        nargs="+",
        default=("schemas/**/*.json", "schemas/**/*.jsonld"),
        help="Glob patterns of schema files to analyse.",
    )
    parser.add_argument("--clusters", type=int, default=6, help="Maximum number of clusters to generate.")
    args = parser.parse_args()
    clusters = analyse_schema_directory(args.schemas, n_clusters=args.clusters)
    if not clusters:
        print("No schema terms discovered.")
        return
    for row in clusters_to_rows(clusters):
        print(f"cluster={row['cluster_id']} fields={row['field_count']} keywords={row['keywords']}")


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    run_cli()
