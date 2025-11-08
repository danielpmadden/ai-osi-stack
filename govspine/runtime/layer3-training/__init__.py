# SPDX-License-Identifier: Apache-2.0

"""Layer 3 — Training and adaptation orchestration."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Any

from ..common.crypto import sha3_512_hex, temporal_seal
from ..common.layer import BaseLayer, LayerContext
from ..common.schema import json_dumps, load_schema


class Layer3Training(BaseLayer):
    """Turns architectural plans into training or fine-tuning instructions."""

    def __init__(self) -> None:
        super().__init__(
            layer_id="L3",
            description="Training governance and corpus alignment",
            context=LayerContext(name="Training"),
        )
        self.schema = load_schema(Path(__file__).with_name("schema.json"))

    def _transform(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        spec = {
            "dataset": payload.get("dataset", {"name": "synthetic-governance"}),
            "objectives": payload.get("objectives", ["align-governance"]),
            "temporalSeal": temporal_seal(),
        }
        envelope = {
            "layerId": self.layer_id,
            "dignityCompliance": self.context.dignity_compliance,
            "trainingSpec": spec,
        }
        envelope["hash"] = sha3_512_hex(json_dumps(envelope))
        return envelope


__all__ = ["Layer3Training"]
