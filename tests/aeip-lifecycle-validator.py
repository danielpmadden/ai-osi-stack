"""AEIP lifecycle validator utilities and accompanying tests.

The module defines helper functions that validate receipts, signatures, and
layer paths for AEIP governed artifacts. These utilities support future
integration with governance pipelines and ensure Update Plan 12 requirements
remain testable.
"""
from __future__ import annotations

from typing import Iterable

VALID_LAYERS = {
    "L0",
    "L1",
    "L2",
    "L3",
    "L4",
    "L5",
    "L6",
    "L7",
    "L8",
}


def validate_receipts(receipts: Iterable[dict]) -> bool:
    """Ensure at least one receipt exists and every receipt has an identifier."""
    receipts = list(receipts)
    if not receipts:
        return False
    return all("receiptId" in receipt and receipt["receiptId"] for receipt in receipts)


def validate_signatures(receipts: Iterable[dict]) -> bool:
    """Check that every receipt carries a canonical signature block."""
    for receipt in receipts:
        signature = receipt.get("signature", {})
        if not isinstance(signature, dict):
            return False
        if not signature.get("signer") or not signature.get("hash"):
            return False
    return True


def validate_layer_path(layer_path: str) -> bool:
    """Validate an AEIP layer path of the form L{n}[.subdomain]."""
    if not layer_path:
        return False
    segments = layer_path.split(".")
    if segments[0] not in VALID_LAYERS:
        return False
    return all(segment.isalnum() for segment in segments[1:])


# -------------------
# Pytest integration
# -------------------

def test_validate_receipts_success():
    receipts = [
        {"receiptId": "R-001", "signature": {"signer": "custodian", "hash": "abc"}},
        {"receiptId": "R-002", "signature": {"signer": "auditor", "hash": "def"}},
    ]
    assert validate_receipts(receipts) is True


def test_validate_receipts_failure():
    receipts = [
        {"receiptId": "", "signature": {"signer": "custodian", "hash": "abc"}},
    ]
    assert validate_receipts(receipts) is False


def test_validate_signatures_success():
    receipts = [
        {"receiptId": "R-001", "signature": {"signer": "custodian", "hash": "abc"}}
    ]
    assert validate_signatures(receipts) is True


def test_validate_signatures_failure_missing_block():
    receipts = [{"receiptId": "R-001"}]
    assert validate_signatures(receipts) is False


def test_validate_signatures_failure_empty_fields():
    receipts = [
        {"receiptId": "R-001", "signature": {"signer": "", "hash": ""}}
    ]
    assert validate_signatures(receipts) is False


def test_validate_layer_path_success():
    assert validate_layer_path("L5.Reasoning.Exchange") is True


def test_validate_layer_path_failure_unknown_layer():
    assert validate_layer_path("L9.Unknown") is False


def test_validate_layer_path_failure_invalid_segment():
    assert validate_layer_path("L5.Reasoning-Exchange") is False
