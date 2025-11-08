# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from datetime import datetime, timezone

from protocol.aeip_handshake import AEIPHandshake, AEIP_STEPS
from govspine.common.artifacts import Artifact
from govspine.common.crypto import sha3_512_hex
from govspine.common.schema import json_dumps, load_schema


def _itp_payload() -> dict:
    timestamp = datetime.now(timezone.utc).isoformat()
    payload = {
        "id": "itp-test",
        "version": "1.0",
        "source": "pytest",
        "personaId": "persona.test",
        "timestamp": timestamp,
        "temporalSeal": f"{timestamp}::{sha3_512_hex(timestamp)}",
        "dignityCompliance": True,
        "objective": "unit-test",
        "constraints": ["safety"],
        "evaluationCriteria": ["integrity"],
    }
    payload["hash"] = sha3_512_hex(json_dumps(payload))
    return payload


def test_handshake_full_cycle() -> None:
    handshake = AEIPHandshake(handshake_id="test", governance_scope="pytest")
    for index, step in enumerate(AEIP_STEPS):
        payload = {"message": step, "sequence": index}
        message = handshake.record(
            step=step, persona_id=f"persona-{index}", payload=payload
        )
        assert message.signature is not None
        assert message.dignity_compliance is True
    transcript = handshake.to_dict()
    assert transcript["finalised"] is True
    assert transcript["handshakeId"] == "test"
    assert transcript["steps"][0]["step"] == "Intent"

    schema = load_schema("schemas/itp-schema.json")
    artifact = Artifact(schema=schema, payload=_itp_payload())
    artifact.validate()
    ledger_payload = handshake.attach_artifact(artifact)
    assert ledger_payload["artifactType"] == schema.name
    assert ledger_payload["handshake"]["finalHash"] == transcript["finalHash"]

    json_text = handshake.serialize(fmt="json")
    yaml_text = handshake.serialize(fmt="yaml")
    assert "handshakeId" in json_text
    assert "handshakeId" in yaml_text
