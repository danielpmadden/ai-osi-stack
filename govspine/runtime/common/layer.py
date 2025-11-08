# SPDX-License-Identifier: Apache-2.0

"""Layer abstractions for the AI OSI reference stack."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Optional

from .interface import InterfaceContract, load_contract
from .schema import SchemaDocument, load_schema, validate_schema


@dataclass(slots=True)
class LayerContext:
    name: str
    dignity_compliance: bool = True
    temporal_governance_clause: str | None = None


@dataclass(slots=True)
class BaseLayer:
    layer_id: str
    description: str
    input_contract: InterfaceContract | None = None
    output_contract: InterfaceContract | None = None
    context: LayerContext = field(default_factory=lambda: LayerContext(name="unspecified"))

    def process(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        if not self.context.dignity_compliance:
            raise PermissionError(f"Layer {self.layer_id} refuses processing; dignity compliance off")
        if self.input_contract:
            self.input_contract.validate_payload(payload)
        result = self._transform(payload)
        if self.output_contract:
            self.output_contract.validate_payload(result)
        return result

    def _transform(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

    def set_contracts(
        self,
        *,
        input_schema: str | Path | None = None,
        output_schema: str | Path | None = None,
        producer: str | None = None,
        consumer: str | None = None,
    ) -> None:
        if input_schema:
            self.input_contract = load_contract(input_schema, producer or "upstream", self.layer_id)
        if output_schema:
            self.output_contract = load_contract(output_schema, self.layer_id, consumer or "downstream")


__all__ = ["BaseLayer", "LayerContext"]
