# SPDX-License-Identifier: Apache-2.0

"""Validation helpers for Layer 1 payloads."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from ..common.crypto import sha3_512_hex
from ..common.schema import SchemaValidationError, load_schema, json_dumps

SCHEMA = load_schema(Path(__file__).with_name("schema.json"))


def validate(payload: Dict[str, Any]) -> Dict[str, Any]:
    SCHEMA.validate(payload)
    expected_hash = sha3_512_hex(_material_without_hash(payload))
    if payload.get("hash") != expected_hash:
        raise SchemaValidationError(
            f"Layer1 hash mismatch: {payload.get('hash')} != {expected_hash}"
        )
    return payload


def _material_without_hash(payload: Dict[str, Any]) -> str:
    shadow = dict(payload)
    shadow.pop("hash", None)
    return json_dumps(shadow)


__all__ = ["validate", "SCHEMA"]
