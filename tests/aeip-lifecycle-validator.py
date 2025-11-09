# SPDX-License-Identifier: Apache-2.0
"""Lifecycle validation helpers for AEIP receipts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List, Sequence

REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_DIR = REPO_ROOT / "examples" / "aeip"
EXPECTED_SEQUENCE: Sequence[str] = ("Intent", "Justify", "CounterSign", "Commit", "Update")


class LifecycleError(RuntimeError):
    """Raised when AEIP lifecycle transitions are invalid."""


def load_receipts() -> List[dict]:
    receipts: List[dict] = []
    for path in sorted(EXAMPLE_DIR.glob("*.jsonld")):
        with path.open("r", encoding="utf-8") as handle:
            receipts.append(json.load(handle))
    return receipts


def validate_privacy_block(receipt: dict) -> None:
    privacy = receipt.get("privacy", {})
    scope = privacy.get("scope")
    if scope not in {"public", "restricted", "deidentified", "internal"}:
        raise LifecycleError(f"{receipt['id']} invalid privacy scope: {scope}")
    if not privacy.get("notes"):
        raise LifecycleError(f"{receipt['id']} missing privacy notes")


def validate_provenance_block(receipt: dict) -> None:
    provenance = receipt.get("provenance", {})
    if not provenance.get("source"):
        raise LifecycleError(f"{receipt['id']} missing provenance.source")
    if not provenance.get("method"):
        raise LifecycleError(f"{receipt['id']} missing provenance.method")


def validate_uncertainty(receipt: dict) -> None:
    uncertainty = receipt.get("uncertainty", {})
    score = uncertainty.get("score")
    if not isinstance(score, (int, float)) or not 0 <= score <= 1:
        raise LifecycleError(f"{receipt['id']} uncertainty.score must be between 0 and 1")


def validate_signatures(receipt: dict) -> None:
    signatures = receipt.get("signatures", [])
    if not signatures:
        raise LifecycleError(f"{receipt['id']} missing signatures")
    for signature in signatures:
        value = signature.get("value", "")
        if "[redacted" not in value:
            raise LifecycleError(f"{receipt['id']} signature value must be redacted placeholder")


def validate_lifecycle_chain(receipts: Iterable[dict]) -> None:
    ordering = {receipt["lifecycle"]["current"]: receipt for receipt in receipts}
    missing = [stage for stage in EXPECTED_SEQUENCE if stage not in ordering]
    if missing:
        raise LifecycleError(f"Missing lifecycle stages: {', '.join(missing)}")
    for index, stage in enumerate(EXPECTED_SEQUENCE):
        current = ordering[stage]
        lifecycle = current["lifecycle"]
        if lifecycle["current"] != stage:
            raise LifecycleError(f"Receipt {current['id']} mislabels stage {stage}")
        if index < len(EXPECTED_SEQUENCE) - 1:
            expected_next = EXPECTED_SEQUENCE[index + 1]
            if lifecycle.get("next") != expected_next:
                raise LifecycleError(
                    f"{current['id']} should advance to {expected_next} not {lifecycle.get('next')}"
                )
        if index > 0:
            expected_prev = EXPECTED_SEQUENCE[index - 1]
            if lifecycle.get("previous") not in {expected_prev, EXPECTED_SEQUENCE[index - 1]}:
                raise LifecycleError(
                    f"{current['id']} previous stage should be {expected_prev}"
                )


def validate_receipt(receipt: dict) -> None:
    validate_privacy_block(receipt)
    validate_provenance_block(receipt)
    validate_uncertainty(receipt)
    validate_signatures(receipt)


# -------------------
# Pytest integration
# -------------------


def test_examples_pass_validators() -> None:
    receipts = load_receipts()
    for receipt in receipts:
        validate_receipt(receipt)
    validate_lifecycle_chain(receipts)


def test_invalid_uncertainty() -> None:
    receipt = load_receipts()[0].copy()
    receipt["uncertainty"] = {"score": 1.5}
    try:
        validate_uncertainty(receipt)
    except LifecycleError:
        return
    raise AssertionError("Expected LifecycleError when uncertainty score exceeds range")


def test_missing_signatures() -> None:
    receipt = load_receipts()[0].copy()
    receipt["signatures"] = []
    try:
        validate_signatures(receipt)
    except LifecycleError:
        return
    raise AssertionError("Expected LifecycleError when signatures missing")


def test_lifecycle_sequence_enforced() -> None:
    receipts = load_receipts()
    receipts[0]["lifecycle"]["next"] = "Commit"
    try:
        validate_lifecycle_chain(receipts)
    except LifecycleError:
        return
    raise AssertionError("Expected LifecycleError when lifecycle chain is broken")
