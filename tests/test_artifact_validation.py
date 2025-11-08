# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from protocol.aeip_handshake import AEIPHandshake, AEIP_STEPS
from protocol.ledger_node import GovernanceLedgerNode
from govspine.common.artifacts import Artifact
from govspine.common.crypto import sha3_512_hex
from govspine.common.schema import json_dumps, load_schema


def _timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def _hash(payload: dict) -> str:
    return sha3_512_hex(json_dumps(payload))


def _itp() -> dict:
    payload = {
        "id": "itp-artifact",
        "version": "1.0",
        "source": "pytest",
        "personaId": "persona.1",
        "timestamp": _timestamp(),
        "dignityCompliance": True,
        "objective": "demo",
        "constraints": ["safety"],
        "evaluationCriteria": ["governance"],
    }
    payload["hash"] = _hash(payload)
    return payload


def _drr() -> dict:
    payload = {
        "id": "drr-artifact",
        "version": "1.0",
        "source": "pytest",
        "personaId": "persona.2",
        "timestamp": _timestamp(),
        "dignityCompliance": True,
        "decisionSummary": "approve",
        "rationale": [
            {"step": "analysis", "justification": "meets controls", "evidence": "tests"}
        ],
    }
    payload["hash"] = _hash(payload)
    return payload


def _gds() -> dict:
    payload = {
        "id": "gds-artifact",
        "version": "1.0",
        "source": "pytest",
        "personaId": "persona.3",
        "timestamp": _timestamp(),
        "dignityCompliance": True,
        "directives": [
            {
                "controlId": "ctrl-1",
                "title": "Log",
                "severity": "medium",
                "actions": ["log"],
            }
        ],
    }
    payload["hash"] = _hash(payload)
    return payload


def _oam() -> dict:
    payload = {
        "id": "oam-artifact",
        "version": "1.0",
        "source": "pytest",
        "personaId": "persona.4",
        "timestamp": _timestamp(),
        "dignityCompliance": True,
        "metrics": [
            {
                "metricId": "m1",
                "value": 0.95,
                "interpretation": "meets threshold",
            }
        ],
    }
    payload["hash"] = _hash(payload)
    return payload


def _ile(handshake_dict: dict) -> dict:
    payload = {
        "id": "ile-artifact",
        "version": "1.0",
        "source": "pytest",
        "personaId": "persona.ledger",
        "timestamp": _timestamp(),
        "dignityCompliance": True,
        "artifactType": "ITP",
        "artifactRef": "ITP:itp-artifact",
        "temporalSeal": handshake_dict["steps"][-1]["temporalSeal"],
        "aeipVersion": handshake_dict["aeipVersion"],
        "governanceScope": handshake_dict["governanceScope"],
        "aeipDigest": {
            "handshakeId": handshake_dict["handshakeId"],
            "steps": [step["step"] for step in handshake_dict["steps"]],
            "finalHash": handshake_dict["finalHash"],
        },
        "governanceClauses": ["v4-clause-1"],
    }
    payload["hash"] = _hash(payload)
    return payload


def test_artifact_schemas_roundtrip(tmp_path: Path) -> None:
    schemas = {
        "ITP": (_itp(), "schemas/itp-schema.json"),
        "DRR": (_drr(), "schemas/drr-schema.yaml"),
        "GDS": (_gds(), "schemas/gds-schema.json"),
        "OAM": (_oam(), "schemas/oam-schema.yaml"),
    }
    for name, (payload, schema_path) in schemas.items():
        schema = load_schema(schema_path)
        artifact = Artifact(schema=schema, payload=payload)
        artifact.validate()
        assert artifact.payload["hash"] == artifact.computed_hash

    handshake = AEIPHandshake(handshake_id="artifact-test", governance_scope="pytest")
    for step in AEIP_STEPS:
        handshake.record(
            step=step, persona_id=f"persona-{step}", payload={"detail": step}
        )
    handshake_dict = handshake.to_dict()

    ile_schema = load_schema("schemas/ile-schema.json")
    ile_artifact = Artifact(schema=ile_schema, payload=_ile(handshake_dict))
    ile_artifact.validate()

    node = GovernanceLedgerNode(
        ledger_dir=tmp_path / "ledger", registry_path=tmp_path / "registry.yaml"
    )
    result = node.submit_artifact(
        artifact_type="ITP",
        artifact_payload=_itp(),
        handshake=handshake_dict,
    )
    assert result.index == 1
    assert result.path.exists()
    assert result.entry["aeipDigest"]["finalHash"] == handshake_dict["finalHash"]
