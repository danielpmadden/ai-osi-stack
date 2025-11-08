# SPDX-License-Identifier: Apache-2.0

"""Layer 7 — Governance oversight and ledger integration."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Any

from ..common.crypto import sha3_512_hex, temporal_seal
from ..common.layer import BaseLayer, LayerContext
from ..common.schema import json_dumps, load_schema


class Layer7Governance(BaseLayer):
    """Creates governance directives, DRR, and ledger-ready payloads."""

    def __init__(self) -> None:
        super().__init__(
            layer_id="L7",
            description="Governance synthesis & ledger serialisation",
            context=LayerContext(name="Governance"),
        )
        self.schema = load_schema(Path(__file__).with_name("schema.json"))

    def _transform(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        decision = {
            "summary": payload.get("summary", "Approved"),
            "temporalSeal": temporal_seal(),
            "aeipDigest": payload.get("aeipDigest", {}),
            "governanceClauses": payload.get("governanceClauses", ["v4-clause-1"]),
        }
        envelope = {
            "layerId": self.layer_id,
            "dignityCompliance": self.context.dignity_compliance,
            "governanceDecision": decision,
        }
        envelope["hash"] = sha3_512_hex(json_dumps({k: v for k, v in envelope.items() if k != "hash"}))
        return envelope


__all__ = ["Layer7Governance"]
