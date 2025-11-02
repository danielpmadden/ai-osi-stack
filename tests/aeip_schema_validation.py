#!/usr/bin/env python3
"""
Title: AEIP Schema Validation Examples
Version: 1.0.1
Date: 2025-05-09T00:00:00Z
Author: Repository Architect
License: CC BY-NC-ND 4.0
Signature: Pending governance signature
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List
from urllib.parse import urlparse

SCHEMA_DIRECTORY = Path(__file__).resolve().parents[1] / "schemas"
SCHEMA_FILES = {
    "InterpretiveTracePackage": "interpretive-trace-package.jsonld",
    "DecisionRationaleRecord": "decision-rationale-record.jsonld",
    "GovernanceDecisionSummary": "governance-decision-summary.jsonld",
    "OversightAuditMemo": "oversight-audit-memo.jsonld",
    "IntegrityLedgerEntry": "integrity-ledger-entry.jsonld",
}
UUID_PATTERN = re.compile(r"^(?:urn:uuid:)?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$")
HASH_PATTERN = re.compile(r"^[A-Fa-f0-9]{64}$")


def load_schema(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def is_uri(value: str) -> bool:
    parsed = urlparse(value)
    return bool(parsed.scheme and parsed.netloc)


def validate_required_fields(payload: Dict[str, Any], schema: Dict[str, Any]) -> None:
    for field in schema.get("required", []):
        assert field in payload, f"Missing required field: {field}"


def validate_timestamp(value: str) -> datetime:
    assert isinstance(value, str) and value, "Timestamp must be a non-empty string"
    iso_value = value.replace("Z", "+00:00") if value.endswith("Z") else value
    dt = datetime.fromisoformat(iso_value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def validate_uuid(value: str) -> None:
    assert isinstance(value, str) and UUID_PATTERN.match(value), "UUID must follow UUIDv4 or URN UUIDv4 format"


def validate_signature(signature: Dict[str, Any]) -> None:
    assert isinstance(signature, dict), "Signature block must be an object"
    for key in ("method", "key_id", "value"):
        assert key in signature and isinstance(signature[key], str) and signature[key], f"Signature missing {key}"


def validate_provenance(provenance: Dict[str, Any]) -> None:
    assert isinstance(provenance, dict), "Provenance block must be an object"
    for key in ("source_system", "collection_method", "jurisdiction"):
        assert key in provenance and isinstance(provenance[key], str) and provenance[key], f"Provenance missing {key}"


def validate_linked_artifacts(items: Iterable[Any]) -> List[str]:
    links: List[str] = []
    for ref in items:
        assert isinstance(ref, str), "Linked artifact references must be strings"
        if not (UUID_PATTERN.match(ref) or is_uri(ref)):
            raise AssertionError("Linked artifact must be UUIDv4 or URI")
        links.append(ref)
    assert links, "At least one linked artifact is required"
    return links


def validate_examples() -> None:
    for artifact_type, file_name in SCHEMA_FILES.items():
        schema_path = SCHEMA_DIRECTORY / file_name
        schema = load_schema(schema_path)
        examples: Iterable[Dict[str, Any]] = schema.get("examples", [])
        for index, payload in enumerate(examples):
            validate_required_fields(payload, schema)
            assert payload.get("artifact_type") == artifact_type, (
                f"Example {index} in {file_name} does not advertise {artifact_type}."
            )
            validate_uuid(payload["uuid"])
            validate_timestamp(payload["timestamp"])
            validate_signature(payload["signature"])
            validate_provenance(payload["provenance"])
            validate_linked_artifacts(payload["linked_artifacts"])
            layer = payload["layer"]
            assert isinstance(layer, int) and 1 <= layer <= 7, "Layer must be between 1 and 7"
            if artifact_type == "IntegrityLedgerEntry":
                assert HASH_PATTERN.match(payload["hash"]), "Integrity hash must be 64 hex characters"
                prev = payload["previous_entry"]
                assert isinstance(prev, str) and (prev == "GENESIS" or UUID_PATTERN.match(prev)), "Invalid previous_entry reference"


def build_integrity_entry(linked: Iterable[str]) -> Dict[str, Any]:
    now = datetime(2025, 5, 9, 13, 15, 0, tzinfo=timezone.utc)
    entry_links = validate_linked_artifacts(linked)
    return {
        "artifact_type": "IntegrityLedgerEntry",
        "version": "1.0.0",
        "uuid": "urn:uuid:663e4567-e89b-42d3-a456-426614174050",
        "timestamp": now.isoformat().replace("+00:00", "Z"),
        "layer": 7,
        "issuer": {
            "name": "Integrity Ledger Custodian",
            "role": "Layer 7 Custodian",
            "organization": "AI Governance Council",
            "contact": "https://governance.example.org/custodian/ledger"
        },
        "summary": "Ledger entry chaining oversight artifacts for release 2025.05 post-audit closure.",
        "hash": "B4E6D7C8F90123456789ABCDEF0123456789ABCDEF0123456789ABCDEF012345",
        "previous_entry": "urn:uuid:553e4567-e89b-42d3-a456-426614174040",
        "linked_artifacts": entry_links,
        "signature": {
            "method": "Ed25519",
            "key_id": "did:example:governance-keys#ledger-custodian",
            "value": "MEQCIG..."
        },
        "provenance": {
            "source_system": "Integrity Ledger Service",
            "collection_method": "Automated notarization with human oversight",
            "jurisdiction": "Global",
            "confidence": "Authoritative"
        }
    }


def demonstrate_integrity_linkage() -> None:
    linked = [
        "urn:uuid:333e4567-e89b-42d3-a456-426614174020",
        "urn:uuid:443e4567-e89b-42d3-a456-426614174030",
    ]
    entry = build_integrity_entry(linked)
    validate_uuid(entry["uuid"])
    validate_timestamp(entry["timestamp"])
    validate_signature(entry["signature"])
    validate_provenance(entry["provenance"])
    validate_linked_artifacts(entry["linked_artifacts"])
    assert entry["previous_entry"] == "urn:uuid:553e4567-e89b-42d3-a456-426614174040"


if __name__ == "__main__":
    validate_examples()
    demonstrate_integrity_linkage()
    print("AEIP schema examples validated and integrity ledger demonstration completed.")
