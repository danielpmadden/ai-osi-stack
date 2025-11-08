# SPDX-License-Identifier: Apache-2.0

"""Validation helpers for Layer 4 payloads."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Any

from ..common.crypto import sha3_512_hex
from ..common.schema import SchemaValidationError, json_dumps, load_schema

SCHEMA = load_schema(Path(__file__).with_name("schema.json"))


def validate(payload: Dict[str, Any]) -> Dict[str, Any]:
    SCHEMA.validate(payload)
    without_hash = {k: v for k, v in payload.items() if k != "hash"}
    expected_hash = sha3_512_hex(json_dumps(without_hash))
    if payload.get("hash") != expected_hash:
        raise SchemaValidationError(
            f"Layer4 hash mismatch: {payload.get('hash')} != {expected_hash}"
        )
    return payload


__all__ = ["validate", "SCHEMA"]
