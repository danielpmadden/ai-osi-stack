"""Layer 1 — Physical Substrate orchestration."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Any

from ..common.crypto import sha3_512_hex, temporal_seal
from ..common.layer import BaseLayer, LayerContext
from ..common.schema import load_schema


class Layer1Physical(BaseLayer):
    """Models hardware availability, energy controls, and persona safety rails."""

    def __init__(self) -> None:
        super().__init__(
            layer_id="L1",
            description="Physical safeguards and telemetry normalisation",
            context=LayerContext(name="Physical"),
        )
        self.schema = load_schema(Path(__file__).with_name("schema.json"))

    def _transform(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        enriched = dict(payload)
        enriched.setdefault("layerId", self.layer_id)
        enriched.setdefault("temporalSeal", temporal_seal())
        enriched.setdefault("dignityCompliance", self.context.dignity_compliance)
        enriched.setdefault("physicalEvidence", {"power": "stable", "cooling": "nominal"})
        enriched["hash"] = sha3_512_hex(self._canonical_material(enriched))
        return enriched

    @staticmethod
    def _canonical_material(payload: Dict[str, Any]) -> str:
        from ..common.schema import json_dumps

        shadow = dict(payload)
        shadow.pop("hash", None)
        return json_dumps(shadow)


__all__ = ["Layer1Physical"]
