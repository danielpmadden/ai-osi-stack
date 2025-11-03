"""Interface contract definitions across the AI OSI stack."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from .schema import SchemaDocument, load_schema, validate_schema


@dataclass(slots=True)
class InterfaceContract:
    """Represents a contract between adjacent AI OSI layers."""

    name: str
    producer_layer: str
    consumer_layer: str
    schema: SchemaDocument

    def validate_payload(self, payload: Dict[str, Any]) -> None:
        validate_schema(payload, self.schema.schema)


def load_contract(schema_path: str, producer_layer: str, consumer_layer: str) -> InterfaceContract:
    schema_doc = load_schema(schema_path)
    return InterfaceContract(
        name=schema_doc.name,
        producer_layer=producer_layer,
        consumer_layer=consumer_layer,
        schema=schema_doc,
    )


__all__ = ["InterfaceContract", "load_contract"]
