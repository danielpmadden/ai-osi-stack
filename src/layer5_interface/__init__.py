"""Layer 5 — Interface orchestration bridging AEIP transport."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Any

from ..common.crypto import sha3_512_hex, temporal_seal
from ..common.layer import BaseLayer, LayerContext
from ..common.schema import json_dumps, load_schema


class Layer5Interface(BaseLayer):
    """Wraps instruction packets with AEIP headers ready for transport."""

    def __init__(self) -> None:
        super().__init__(
            layer_id="L5",
            description="Interface normalisation & AEIP header management",
            context=LayerContext(name="Interface"),
        )
        self.schema = load_schema(Path(__file__).with_name("schema.json"))

    def _transform(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        headers = {
            "aeipVersion": payload.get("aeipVersion", "1.0"),
            "temporalSeal": temporal_seal(),
            "personaSignature": payload.get("personaSignature", {}),
            "governanceScope": payload.get("governanceScope", "default"),
        }
        envelope = {
            "layerId": self.layer_id,
            "headers": headers,
            "dignityCompliance": self.context.dignity_compliance,
            "payload": payload,
        }
        envelope["hash"] = sha3_512_hex(json_dumps({k: v for k, v in envelope.items() if k != "hash"}))
        return envelope


__all__ = ["Layer5Interface"]
