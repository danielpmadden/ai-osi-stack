# SPDX-License-Identifier: Apache-2.0

"""Lightweight schema loader and validator for AI OSI artifacts."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable

from .crypto import sha3_512_hex


class SchemaValidationError(ValueError):
    """Raised when an artifact does not match the declared schema."""


@dataclass(slots=True)
class SchemaDocument:
    name: str
    version: str
    schema: Dict[str, Any]

    def validate(self, payload: Dict[str, Any]) -> None:
        validate_schema(payload, self.schema)


TYPE_MAP = {
    "string": str,
    "integer": int,
    "number": (int, float),
    "object": dict,
    "array": list,
    "boolean": bool,
}


def _ensure_type(value: Any, expected: str, path: str) -> None:
    python_type = TYPE_MAP.get(expected)
    if python_type is None:
        raise SchemaValidationError(f"Unsupported schema type '{expected}' at {path}")
    if not isinstance(value, python_type):
        raise SchemaValidationError(
            f"Value at {path} expected type {expected} but received {type(value).__name__}"
        )


def validate_schema(payload: Any, schema: Dict[str, Any], path: str = "root") -> None:
    schema_type = schema.get("type")
    if schema_type and schema_type != "object":
        _ensure_type(payload, schema_type, path)
        if schema_type == "array" and "items" in schema:
            for index, item in enumerate(payload):
                validate_schema(item, schema["items"], f"{path}[{index}]")
        return

    if schema_type not in {None, "object"}:
        raise SchemaValidationError("Unsupported schema declaration")
    properties: Dict[str, Dict[str, Any]] = schema.get("properties", {})
    required: Iterable[str] = schema.get("required", [])

    for key in required:
        if key not in payload:
            raise SchemaValidationError(f"Missing required field '{key}' at {path}")

    for key, value in payload.items():
        if key not in properties:
            continue  # Allow extensibility while we stabilise the protocol
        property_schema = properties[key]
        expected_type = property_schema.get("type")
        if expected_type:
            _ensure_type(value, expected_type, f"{path}.{key}")
        if expected_type == "object" and "properties" in property_schema:
            validate_schema(value, property_schema, f"{path}.{key}")
        if expected_type == "array" and "items" in property_schema:
            for index, item in enumerate(value):
                validate_schema(item, property_schema["items"], f"{path}.{key}[{index}]")
        if property_schema.get("format") == "hash-SHA3-512":
            expected_hash = sha3_512_hex(property_schema.get("hashSeed", "") + json_dumps(value))
            if value != expected_hash:
                raise SchemaValidationError(
                    f"Hash mismatch for {path}.{key}; expected {expected_hash}"
                )


def json_dumps(value: Any) -> str:
    import json

    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _simple_yaml_load(raw: str) -> Dict[str, Any]:
    stripped = raw.strip()
    if stripped.startswith("{") or stripped.startswith("["):
        import json

        return json.loads(raw)
    raise SchemaValidationError("YAML parsing requires PyYAML when non-JSON syntax is used")


def load_schema(path: str | Path) -> SchemaDocument:
    path = Path(path)
    raw = path.read_text()
    if path.suffix in {".yaml", ".yml"}:
        try:
            import yaml  # type: ignore

            data = yaml.safe_load(raw)
        except Exception:
            data = _simple_yaml_load(raw)
    else:
        import json

        data = json.loads(raw)

    metadata = data.get("$metadata", {})
    name = metadata.get("name", path.stem)
    version = metadata.get("version", "0.0.0")
    schema = data.get("schema", data)
    return SchemaDocument(name=name, version=version, schema=schema)


__all__ = [
    "SchemaDocument",
    "SchemaValidationError",
    "json_dumps",
    "load_schema",
    "validate_schema",
]
