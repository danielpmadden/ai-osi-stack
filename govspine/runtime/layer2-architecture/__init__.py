# SPDX-License-Identifier: Apache-2.0

"""Layer 2 — Architecture design and persona topology."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Any

from ..common.crypto import sha3_512_hex, temporal_seal
from ..common.layer import BaseLayer, LayerContext
from ..common.schema import load_schema, json_dumps


class Layer2Architecture(BaseLayer):
    """Translates physical telemetry into architecture blueprints for higher layers."""

    def __init__(self) -> None:
        super().__init__(
            layer_id="L2",
            description="Architecture design & persona topology",
            context=LayerContext(name="Architecture"),
        )
        self.schema = load_schema(Path(__file__).with_name("schema.json"))

    def _transform(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        plan = {
            "personaGraph": payload.get("personaGraph", []),
            "interfaces": payload.get("interfaces", ["aeip:v1"]),
            "temporalSeal": temporal_seal(),
        }
        envelope = {
            "layerId": self.layer_id,
            "dignityCompliance": self.context.dignity_compliance,
            "architecturePlan": plan,
        }
        envelope["hash"] = sha3_512_hex(json_dumps(envelope))
        return envelope


__all__ = ["Layer2Architecture"]
