"""Utilities for loading and validating governance schemas."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Mapping

import json
import pathlib


@dataclass
class ValidationError(Exception):
    """Represents a manifest validation failure."""

    message: str
    path: tuple[str, ...] = ()

    def __str__(self) -> str:  # pragma: no cover - human readable path only
        if not self.path:
            return self.message
        joined = "/".join(self.path)
        return f"{joined}: {self.message}"


class SimpleValidator:
    """A deliberately small JSON Schema validator for the Governance Spine."""

    def __init__(self, schema: Mapping[str, Any]) -> None:
        self._schema = schema

    def validate(self, instance: Any) -> None:
        self._validate(instance, self._schema, path=())

    def _validate(self, instance: Any, schema: Mapping[str, Any], path: tuple[str, ...]) -> None:
        schema_type = schema.get("type")
        if schema_type:
            self._check_type(instance, schema_type, path)

        if schema_type == "object":
            self._validate_object(instance, schema, path)
        elif schema_type == "array":
            self._validate_array(instance, schema, path)

        enum = schema.get("enum")
        if enum is not None and instance not in enum:
            raise ValidationError(f"Expected one of {enum!r} but received {instance!r}", path)

    def _check_type(self, instance: Any, schema_type: str | list[str], path: tuple[str, ...]) -> None:
        types = [schema_type] if isinstance(schema_type, str) else schema_type
        matches = False
        for type_name in types:
            if type_name == "object" and isinstance(instance, dict):
                matches = True
            elif type_name == "array" and isinstance(instance, list):
                matches = True
            elif type_name == "string" and isinstance(instance, str):
                matches = True
            elif type_name == "number" and isinstance(instance, (int, float)):
                matches = True
            elif type_name == "integer" and isinstance(instance, int) and not isinstance(instance, bool):
                matches = True
            elif type_name == "boolean" and isinstance(instance, bool):
                matches = True
            elif type_name == "null" and instance is None:
                matches = True
        if not matches:
            raise ValidationError(f"Value does not match expected type(s) {types}", path)

    def _validate_object(self, instance: Mapping[str, Any], schema: Mapping[str, Any], path: tuple[str, ...]) -> None:
        if not isinstance(instance, Mapping):
            raise ValidationError("Expected object", path)
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                raise ValidationError("Missing required property", path + (key,))
        properties = schema.get("properties", {})
        for key, value in instance.items():
            if key in properties:
                self._validate(value, properties[key], path + (key,))

    def _validate_array(self, instance: Iterable[Any], schema: Mapping[str, Any], path: tuple[str, ...]) -> None:
        if not isinstance(instance, list):
            raise ValidationError("Expected array", path)
        items_schema = schema.get("items")
        if items_schema is None:
            return
        for index, value in enumerate(instance):
            self._validate(value, items_schema, path + (str(index),))


class SchemaRegistry:
    """Loads schema files and returns validators."""

    def __init__(self, root: pathlib.Path) -> None:
        self._root = root
        self._cache: dict[str, SimpleValidator] = {}

    def validator_for(self, schema_ref: str) -> SimpleValidator:
        if schema_ref not in self._cache:
            schema_path = self._root / schema_ref
            with schema_path.open("r", encoding="utf-8") as handle:
                schema = json.load(handle)
            self._cache[schema_ref] = SimpleValidator(schema)
        return self._cache[schema_ref]


def validate_manifest(manifest: Mapping[str, Any], registry: SchemaRegistry) -> None:
    schema_ref = manifest.get("schema_ref")
    if not schema_ref:
        raise ValidationError("Missing schema_ref on manifest")
    validator = registry.validator_for(schema_ref)
    validator.validate(manifest)
