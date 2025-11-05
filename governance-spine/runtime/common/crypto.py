"""Common cryptographic utilities for the AI OSI reference implementation."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import secrets
from typing import Any, Dict

import hashlib


HASH_ALGORITHM = "SHA3-512"


def sha3_512_hex(value: str | bytes) -> str:
    """Return a hex encoded SHA3-512 digest for *value*."""
    if isinstance(value, str):
        value = value.encode("utf-8")
    return hashlib.sha3_512(value).hexdigest()


def temporal_seal(timestamp: datetime | None = None) -> str:
    """Create a deterministic temporal seal string.

    The seal concatenates the ISO timestamp and a keyed digest to guarantee
    monotonicity across the governance network.
    """
    if timestamp is None:
        timestamp = datetime.now(timezone.utc)
    iso_time = timestamp.isoformat()
    digest = sha3_512_hex(iso_time)
    return f"{iso_time}::{digest}"


@dataclass(slots=True)
class PersonaSignature:
    """Placeholder Ed25519 style signature used for protocol conformance.

    The implementation intentionally keeps the algorithm deterministic for
    reproducible tests while exposing an interface that can be swapped for a
    real signing backend in production deployments.
    """

    persona_id: str
    signature: str
    algorithm: str = "Ed25519-Deterministic"

    @classmethod
    def sign(cls, persona_id: str, payload: Dict[str, Any]) -> "PersonaSignature":
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        material = f"{persona_id}::{canonical}"
        signature = sha3_512_hex(material)
        return cls(persona_id=persona_id, signature=signature)

    def verify(self, payload: Dict[str, Any]) -> bool:
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        material = f"{self.persona_id}::{canonical}"
        expected = sha3_512_hex(material)
        return secrets.compare_digest(expected, self.signature)


__all__ = [
    "HASH_ALGORITHM",
    "PersonaSignature",
    "sha3_512_hex",
    "temporal_seal",
]
