# SPDX-License-Identifier: Apache-2.0

"""Artifact helpers bridging schemas and protocol metadata."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

from .crypto import HASH_ALGORITHM, PersonaSignature, sha3_512_hex, temporal_seal
from .schema import SchemaDocument, SchemaValidationError, load_schema, validate_schema, json_dumps


@dataclass(slots=True)
class Artifact:
    """A governance artifact exchanged across AI OSI layers."""

    schema: SchemaDocument
    payload: Dict[str, Any]
    dignity_compliance: bool = True
    signature: PersonaSignature | None = None
    computed_hash: str = field(init=False)

    def __post_init__(self) -> None:
        self.computed_hash = sha3_512_hex(self._canonical_payload(include_hash=False))
        payload_hash = self.payload.get("hash")
        if payload_hash and payload_hash != self.computed_hash:
            raise SchemaValidationError(
                f"Payload hash mismatch: {payload_hash} != {self.computed_hash}"
            )

    def _canonical_payload(self, *, include_hash: bool = True) -> str:
        shadow = dict(self.payload)
        if not include_hash:
            shadow.pop("hash", None)
        return json_dumps(shadow)

    def validate(self) -> None:
        validate_schema(self.payload, self.schema.schema)
        provenance_fields = {"source", "timestamp", "personaId", "hash"}
        missing = provenance_fields.difference(self.payload.keys())
        if missing:
            raise SchemaValidationError(f"Missing provenance fields: {sorted(missing)}")
        if self.payload.get("hash") != self.computed_hash:
            raise SchemaValidationError("Hash integrity failure after schema validation")
        if not self.dignity_compliance:
            raise SchemaValidationError("Artifact flagged as non-compliant with dignity guardrails")

    def sign(self, persona_id: str) -> PersonaSignature:
        self.signature = PersonaSignature.sign(persona_id=persona_id, payload=self.payload)
        return self.signature

    def verify_signature(self) -> bool:
        if not self.signature:
            return False
        return self.signature.verify(self.payload)

    def with_temporal_seal(self) -> Dict[str, Any]:
        stamped = dict(self.payload)
        stamped.setdefault("temporalSeal", temporal_seal())
        stamped.setdefault("hashAlgorithm", HASH_ALGORITHM)
        return stamped

    @classmethod
    def from_file(cls, path: str | Path) -> "Artifact":
        path = Path(path)
        schema = load_schema(Path("schemas") / f"{path.stem}_schema.json")
        if path.suffix in {".yaml", ".yml"}:
            try:
                import yaml  # type: ignore

                data = yaml.safe_load(path.read_text())
            except Exception:
                from .schema import _simple_yaml_load  # type: ignore

                data = _simple_yaml_load(path.read_text())
        else:
            import json

            data = json.loads(path.read_text())
        return cls(schema=schema, payload=data)


__all__ = ["Artifact"]
