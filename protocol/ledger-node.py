"""Governance ledger node daemon."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, Tuple

from govspine.common.artifacts import Artifact
from govspine.common.crypto import HASH_ALGORITHM, sha3_512_hex, temporal_seal
from govspine.common.schema import SchemaValidationError, json_dumps, load_schema
from .aeip_handshake import AEIP_STEPS

SCHEMA_FILES: Dict[str, Path] = {
    "ITP": Path("schemas/itp-schema.json"),
    "DRR": Path("schemas/drr-schema.yaml"),
    "GDS": Path("schemas/gds-schema.json"),
    "OAM": Path("schemas/oam-schema.yaml"),
    "ILE": Path("schemas/ile-schema.json"),
}


class LedgerVerificationError(RuntimeError):
    """Raised when incoming payloads fail governance verification."""


@dataclass(slots=True)
class LedgerResult:
    index: int
    path: Path
    entry: Dict[str, Any]


class GovernanceLedgerNode:
    """Core ledger orchestration service used by the daemon and tests."""

    def __init__(
        self,
        *,
        ledger_dir: str | Path = "ledger",
        registry_path: str | Path = "protocol/registry_gns.yaml",
        node_identifier: str = "gns://local/ledger",
    ) -> None:
        self.ledger_dir = Path(ledger_dir)
        self.registry_path = Path(registry_path)
        self.node_identifier = node_identifier
        self.ledger_dir.mkdir(parents=True, exist_ok=True)
        if not self.registry_path.exists():
            self.registry_path.write_text("nodes: []\n")

    def submit_artifact(
        self,
        *,
        artifact_type: str,
        artifact_payload: Dict[str, Any],
        handshake: Dict[str, Any],
    ) -> LedgerResult:
        schema_path = SCHEMA_FILES.get(artifact_type.upper())
        if not schema_path:
            raise LedgerVerificationError(f"Unknown artifact type '{artifact_type}'")
        schema_doc = load_schema(schema_path)
        artifact = Artifact(schema=schema_doc, payload=artifact_payload)
        artifact.validate()
        self._verify_handshake(handshake)
        entry = self._build_ledger_entry(artifact_type, artifact_payload, handshake)
        index = self._next_index()
        entry["ledgerIndex"] = index
        entry["hash"] = sha3_512_hex(json_dumps({k: v for k, v in entry.items() if k != "hash"}))
        path = self.ledger_dir / f"entry_{index:05d}.json"
        path.write_text(json.dumps(entry, indent=2, sort_keys=True))
        self._update_registry(index)
        return LedgerResult(index=index, path=path, entry=entry)

    # ------------------------------------------------------------------
    # Internal helpers

    def _next_index(self) -> int:
        existing = sorted(self.ledger_dir.glob("entry_*.json"))
        if not existing:
            return 1
        last = existing[-1].stem.split("_")[-1]
        return int(last) + 1

    def _verify_handshake(self, handshake: Dict[str, Any]) -> None:
        steps = handshake.get("steps")
        if not isinstance(steps, list) or len(steps) != len(AEIP_STEPS):
            raise LedgerVerificationError("Handshake must contain all AEIP steps")
        for expected, received in zip(AEIP_STEPS, steps):
            if received.get("step") != expected:
                raise LedgerVerificationError(
                    f"Handshake step mismatch: expected {expected} but found {received.get('step')}"
                )
            signature = received.get("signature")
            if signature:
                persona_id = signature.get("personaId")
                signature_value = signature.get("signature")
                if not persona_id or not signature_value:
                    raise LedgerVerificationError("Incomplete signature material")
                canonical = json_dumps(
                    {
                        "handshakeId": handshake.get("handshakeId"),
                        "aeipVersion": handshake.get("aeipVersion"),
                        "governanceScope": handshake.get("governanceScope"),
                        "step": received.get("step"),
                        "payload": received.get("payload"),
                        "temporalSeal": received.get("temporalSeal"),
                    }
                )
                expected_signature = sha3_512_hex(f"{persona_id}::{canonical}")
                if signature_value != expected_signature:
                    raise LedgerVerificationError("Persona signature integrity failure")
            else:
                raise LedgerVerificationError("Handshake step missing signature")
        computed_final = sha3_512_hex(json_dumps(steps))
        if handshake.get("finalHash") != computed_final:
            raise LedgerVerificationError("Handshake digest mismatch")

    def _build_ledger_entry(
        self,
        artifact_type: str,
        payload: Dict[str, Any],
        handshake: Dict[str, Any],
    ) -> Dict[str, Any]:
        governance_clauses = payload.get("governanceClauses") or ["v4-clause-1"]
        entry = {
            "id": payload.get("id"),
            "version": payload.get("version"),
            "source": payload.get("source"),
            "personaId": payload.get("personaId"),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "hash": payload.get("hash"),
            "hashAlgorithm": HASH_ALGORITHM,
            "temporalSeal": payload.get("temporalSeal", temporal_seal()),
            "aeipVersion": handshake.get("aeipVersion"),
            "governanceScope": handshake.get("governanceScope"),
            "dignityCompliance": payload.get("dignityCompliance", True),
            "artifactType": artifact_type,
            "artifactRef": f"{artifact_type}:{payload.get('id')}",
            "aeipDigest": {
                "handshakeId": handshake.get("handshakeId"),
                "steps": [step.get("step") for step in handshake.get("steps", [])],
                "finalHash": handshake.get("finalHash"),
            },
            "governanceClauses": governance_clauses,
            "personaSignature": handshake.get("steps", [])[-1].get("signature"),
        }
        return entry

    def _update_registry(self, index: int) -> None:
        try:
            import yaml  # type: ignore

            registry = yaml.safe_load(self.registry_path.read_text()) or {}
        except Exception:
            registry = {}
        nodes = registry.get("nodes", [])
        summary = {
            "id": self.node_identifier,
            "ledgerPath": str(self.ledger_dir.resolve()),
            "lastEntry": index,
            "lastUpdated": datetime.now(timezone.utc).isoformat(),
        }
        filtered = [node for node in nodes if node.get("id") != self.node_identifier]
        filtered.append(summary)
        registry["nodes"] = filtered
        try:
            import yaml  # type: ignore

            self.registry_path.write_text(yaml.safe_dump(registry, sort_keys=True))
        except Exception:
            self.registry_path.write_text(json.dumps(registry, indent=2, sort_keys=True))

    # ------------------------------------------------------------------
    # HTTP daemon

    def serve(self, host: str = "0.0.0.0", port: int = 8080) -> None:
        node = self

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):  # type: ignore[override]
                if self.path != "/artifacts":
                    self.send_response(404)
                    self.end_headers()
                    return
                content_length = int(self.headers.get("Content-Length", "0"))
                body = self.rfile.read(content_length)
                try:
                    request = json.loads(body)
                    result = node.submit_artifact(
                        artifact_type=request["artifactType"],
                        artifact_payload=request["artifact"],
                        handshake=request["handshake"],
                    )
                except (KeyError, LedgerVerificationError, SchemaValidationError) as exc:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": str(exc)}).encode("utf-8"))
                    return
                except Exception as exc:  # pragma: no cover - safety net
                    self.send_response(500)
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": str(exc)}).encode("utf-8"))
                    return
                self.send_response(201)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"index": result.index, "path": str(result.path)}).encode("utf-8"))

            def log_message(self, format: str, *args: Any) -> None:  # pragma: no cover
                return  # Quiet logs for deterministic tests

        server = ThreadingHTTPServer((host, port), Handler)
        print(f"Governance ledger node listening on http://{host}:{port}")
        try:
            server.serve_forever()
        except KeyboardInterrupt:  # pragma: no cover - manual shutdown
            pass


def main() -> None:
    node = GovernanceLedgerNode()
    node.serve()


if __name__ == "__main__":  # pragma: no cover
    main()
