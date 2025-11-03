"""AEIP v1 five-step handshake implementation."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
import json
from typing import Any, Dict, List, Sequence

from src.common.artifacts import Artifact
from src.common.crypto import HASH_ALGORITHM, PersonaSignature, sha3_512_hex, temporal_seal
from src.common.schema import json_dumps

AEIP_STEPS: Sequence[str] = ("Intent", "Justify", "CounterSign", "Commit", "Update")


class HandshakeError(RuntimeError):
    """Raised when the AEIP handshake violates the protocol contract."""


@dataclass(slots=True)
class HandshakeMessage:
    step: str
    persona_id: str
    payload: Dict[str, Any]
    dignity_compliance: bool
    temporal_seal: str = field(default_factory=temporal_seal)
    signature: PersonaSignature | None = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "step": self.step,
            "personaId": self.persona_id,
            "payload": self.payload,
            "dignityCompliance": self.dignity_compliance,
            "temporalSeal": self.temporal_seal,
            "signature": None if self.signature is None else {
                "personaId": self.signature.persona_id,
                "signature": self.signature.signature,
                "algorithm": self.signature.algorithm,
            },
        }


class AEIPHandshake:
    """State machine modelling the AEIP v1 transport handshake."""

    def __init__(
        self,
        *,
        handshake_id: str,
        aeip_version: str = "1.0",
        governance_scope: str = "default",
    ) -> None:
        self.handshake_id = handshake_id
        self.aeip_version = aeip_version
        self.governance_scope = governance_scope
        self._messages: List[HandshakeMessage] = []
        self._finalised = False

    @property
    def current_step(self) -> str | None:
        return self._messages[-1].step if self._messages else None

    def record(
        self,
        *,
        step: str,
        persona_id: str,
        payload: Dict[str, Any],
        dignity_compliance: bool = True,
    ) -> HandshakeMessage:
        if self._finalised:
            raise HandshakeError("Handshake already finalised")
        expected = AEIP_STEPS[len(self._messages)]
        if step != expected:
            raise HandshakeError(f"Expected step '{expected}' but received '{step}'")
        message = HandshakeMessage(
            step=step,
            persona_id=persona_id,
            payload=payload,
            dignity_compliance=dignity_compliance,
        )
        message.signature = PersonaSignature.sign(persona_id, self._canonical_message_payload(message))
        if not message.signature.verify(self._canonical_message_payload(message)):
            raise HandshakeError("Unable to verify freshly generated signature")
        self._messages.append(message)
        if len(self._messages) == len(AEIP_STEPS):
            self._finalised = True
        return message

    def _canonical_message_payload(self, message: HandshakeMessage) -> Dict[str, Any]:
        return {
            "handshakeId": self.handshake_id,
            "aeipVersion": self.aeip_version,
            "governanceScope": self.governance_scope,
            "step": message.step,
            "payload": message.payload,
            "temporalSeal": message.temporal_seal,
        }

    def to_dict(self) -> Dict[str, Any]:
        transcript = [msg.to_dict() for msg in self._messages]
        digest = sha3_512_hex(json_dumps(transcript))
        return {
            "handshakeId": self.handshake_id,
            "aeipVersion": self.aeip_version,
            "governanceScope": self.governance_scope,
            "steps": transcript,
            "finalHash": digest,
            "hashAlgorithm": HASH_ALGORITHM,
            "finalised": self._finalised,
        }

    def attach_artifact(self, artifact: Artifact) -> Dict[str, Any]:
        artifact.validate()
        transcript = self.to_dict()
        ledger_payload = {
            "artifactId": artifact.payload.get("id"),
            "artifactType": artifact.schema.name,
            "handshake": transcript,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        ledger_payload["hash"] = sha3_512_hex(json_dumps(ledger_payload))
        return ledger_payload

    def serialize(self, *, fmt: str = "json") -> str:
        document = self.to_dict()
        if fmt == "json":
            return json.dumps(document, indent=2, sort_keys=True)
        if fmt in {"yaml", "json-ld"}:
            try:
                import yaml  # type: ignore

                return yaml.safe_dump(document, sort_keys=True)
            except Exception:
                # degrade gracefully to JSON text when YAML is unavailable
                return json.dumps(document, indent=2, sort_keys=True)
        raise ValueError(f"Unsupported serialization format: {fmt}")


__all__ = ["AEIPHandshake", "AEIP_STEPS", "HandshakeError"]

# Backwards compatibility helpers for notebooks and downstream integrations.
AEIPHandshake.AEIP_STEPS = AEIP_STEPS  # type: ignore[attr-defined]
AEIPHandshake.STEPS = AEIP_STEPS  # type: ignore[attr-defined]
