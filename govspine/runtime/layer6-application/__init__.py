# SPDX-License-Identifier: Apache-2.0

"""Layer 6 — Application semantics and service behaviours."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Any

from ..common.crypto import sha3_512_hex, temporal_seal
from ..common.layer import BaseLayer, LayerContext
from ..common.schema import json_dumps, load_schema


class Layer6Application(BaseLayer):
    """Transforms AEIP payloads into application level responses and artifacts."""

    def __init__(self) -> None:
        super().__init__(
            layer_id="L6",
            description="Application reasoning & artifact generation",
            context=LayerContext(name="Application"),
        )
        self.schema = load_schema(Path(__file__).with_name("schema.json"))

    def _transform(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        response = {
            "serviceOutput": payload.get("serviceOutput", {"status": "ack"}),
            "temporalSeal": temporal_seal(),
            "aeipVersion": payload.get("aeipVersion", "1.0"),
        }
        envelope = {
            "layerId": self.layer_id,
            "applicationResponse": response,
            "dignityCompliance": self.context.dignity_compliance,
        }
        envelope["hash"] = sha3_512_hex(json_dumps({k: v for k, v in envelope.items() if k != "hash"}))
        return envelope


__all__ = ["Layer6Application"]
