"""Search governance manifests using an in-memory SQLite index."""
from __future__ import annotations

import argparse
import json
import pathlib
import sqlite3

import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
from typing import Any, Dict, Iterable, List

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    yaml = None

from tools.governance.schema_utils import SchemaRegistry, ValidationError, validate_manifest

SCHEMA_DIR = pathlib.Path("schemas/aeip")
GOVERNANCE_ROOT = pathlib.Path("governance")


def iter_manifest_paths(root: pathlib.Path) -> Iterable[pathlib.Path]:
    yield from root.rglob("*.json")
    if yaml is not None:
        yield from root.rglob("*.yaml")
        yield from root.rglob("*.yml")


def load_manifest(path: pathlib.Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        if path.suffix == ".json" or yaml is None:
            return json.load(handle)
        return yaml.safe_load(handle)


def create_table(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE manifests (
            uuid TEXT PRIMARY KEY,
            layer TEXT,
            artifact_type TEXT,
            custodian TEXT,
            timestamp TEXT,
            payload_uri TEXT,
            tags TEXT,
            schema_ref TEXT
        )
        """
    )


def insert_manifest(connection: sqlite3.Connection, manifest: Dict[str, Any]) -> None:
    tags = ",".join(manifest.get("tags", []))
    connection.execute(
        """
        INSERT OR REPLACE INTO manifests
            (uuid, layer, artifact_type, custodian, timestamp, payload_uri, tags, schema_ref)
        VALUES
            (:uuid, :layer, :artifact_type, :custodian, :timestamp, :payload_uri, :tags, :schema_ref)
        """,
        {
            "uuid": manifest["uuid"],
            "layer": manifest.get("layer", ""),
            "artifact_type": manifest.get("artifact_type", ""),
            "custodian": manifest.get("custodian", ""),
            "timestamp": manifest.get("timestamp", ""),
            "payload_uri": manifest.get("payload_uri", ""),
            "tags": tags,
            "schema_ref": manifest.get("schema_ref", ""),
        },
    )


def query_manifests(connection: sqlite3.Connection, args: argparse.Namespace) -> List[sqlite3.Row]:
    clauses = []
    params: Dict[str, Any] = {}
    if args.tag:
        clauses.append("tags LIKE :tag")
        params["tag"] = f"%{args.tag}%"
    if args.layer:
        clauses.append("layer = :layer")
        params["layer"] = args.layer
    if args.artifact_type:
        clauses.append("artifact_type = :artifact_type")
        params["artifact_type"] = args.artifact_type
    where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    query = (
        "SELECT uuid, layer, artifact_type, custodian, timestamp, payload_uri, tags "
        "FROM manifests "
        f"{where} "
        "ORDER BY timestamp DESC "
        "LIMIT :limit"
    )
    params["limit"] = args.limit
    cursor = connection.execute(query, params)
    return cursor.fetchall()


def main() -> None:
    parser = argparse.ArgumentParser(description="Search governance manifests")
    parser.add_argument("--tag", help="Filter manifests by tag")
    parser.add_argument("--layer", help="Restrict to a specific governance layer")
    parser.add_argument("--artifact-type", dest="artifact_type", help="Filter by artifact type")
    parser.add_argument("--limit", type=int, default=10, help="Number of results to return")
    args = parser.parse_args()

    registry = SchemaRegistry(SCHEMA_DIR)
    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row
    create_table(connection)

    for path in iter_manifest_paths(GOVERNANCE_ROOT):
        manifest = load_manifest(path)
        try:
            validate_manifest(manifest, registry)
        except ValidationError as exc:  # pragma: no cover - surfaced in CLI use
            raise RuntimeError(f"Validation failed for {path}: {exc}") from exc
        insert_manifest(connection, manifest)

    rows = query_manifests(connection, args)
    if not rows:
        print("No manifests matched the query.")
        return

    for row in rows:
        print(
            f"[{row['layer']}] {row['artifact_type']} {row['uuid']}\n"
            f"  Custodian: {row['custodian']}\n"
            f"  Timestamp: {row['timestamp']}\n"
            f"  Payload: {row['payload_uri']}\n"
            f"  Tags: {row['tags']}\n"
        )


if __name__ == "__main__":
    main()
