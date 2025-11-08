# SPDX-License-Identifier: Apache-2.0

"""Layer 4 — Instruction and control plane."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Any

from ..common.crypto import sha3_512_hex, temporal_seal
from ..common.layer import BaseLayer, LayerContext
from ..common.schema import json_dumps, load_schema


class Layer4Instruction(BaseLayer):
    """Packages training specs into AEIP compatible instruction packets."""

    def __init__(self) -> None:
        super().__init__(
            layer_id="L4",
            description="Instruction encoding & AEIP preparation",
            context=LayerContext(name="Instruction"),
        )
        self.schema = load_schema(Path(__file__).with_name("schema.json"))

    def _transform(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        packet = {
            "intent": payload.get("intent", "governance-aligned operation"),
            "temporalSeal": temporal_seal(),
            "aeipVersion": payload.get("aeipVersion", "1.0"),
            "governanceScope": payload.get("governanceScope", "default"),
            "dignityCompliance": self.context.dignity_compliance,
            "payload": payload,
        }
        envelope = {
            "layerId": self.layer_id,
            "instructionPacket": packet,
        }
        envelope["hash"] = sha3_512_hex(json_dumps(envelope))
        return envelope


__all__ = ["Layer4Instruction"]
