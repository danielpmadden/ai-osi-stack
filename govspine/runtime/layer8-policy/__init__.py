# SPDX-License-Identifier: Apache-2.0

"""Layer 8 — Civic and policy extension."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Any

from ..common.crypto import sha3_512_hex, temporal_seal
from ..common.layer import BaseLayer, LayerContext
from ..common.schema import json_dumps, load_schema


class Layer8Policy(BaseLayer):
    """Synthesises public policy overlays for federated civic participation."""

    def __init__(self) -> None:
        super().__init__(
            layer_id="L8",
            description="Policy harmonisation and civic extension",
            context=LayerContext(name="Policy"),
        )
        self.schema = load_schema(Path(__file__).with_name("schema.json"))

    def _transform(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        directive = {
            "policyIntent": payload.get("policyIntent", "civic-transparency"),
            "temporalSeal": temporal_seal(),
            "stakeholderInputs": payload.get("stakeholderInputs", []),
        }
        envelope = {
            "layerId": self.layer_id,
            "policyDirective": directive,
            "dignityCompliance": self.context.dignity_compliance,
        }
        envelope["hash"] = sha3_512_hex(json_dumps({k: v for k, v in envelope.items() if k != "hash"}))
        return envelope


__all__ = ["Layer8Policy"]
