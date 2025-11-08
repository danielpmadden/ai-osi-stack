# SPDX-License-Identifier: Apache-2.0

#!/usr/bin/env python3
"""Generate governance artifacts that conform to the published schemas."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

from govspine.common.crypto import sha3_512_hex, temporal_seal
from govspine.common.schema import json_dumps, load_schema

SCHEMA_FILES = {
    "ITP": "schemas/itp-schema.json",
    "DRR": "schemas/drr-schema.yaml",
    "GDS": "schemas/gds-schema.json",
    "OAM": "schemas/oam-schema.yaml",
    "ILE": "schemas/ile-schema.json",
}


def build_payload(artifact_type: str, overrides: Dict[str, Any]) -> Dict[str, Any]:
    timestamp = datetime.now(timezone.utc).isoformat()
    base = {
        "id": overrides.get("id", f"{artifact_type.lower()}-{timestamp}"),
        "version": overrides.get("version", "1.0"),
        "source": overrides.get("source", "generator"),
        "personaId": overrides.get("personaId", "persona.generator"),
        "timestamp": overrides.get("timestamp", timestamp),
        "dignityCompliance": overrides.get("dignityCompliance", True),
        "temporalSeal": overrides.get("temporalSeal", temporal_seal()),
    }
    base.update(overrides)
    return base


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact_type", choices=SCHEMA_FILES.keys())
    parser.add_argument("--output", "-o", type=Path, help="File to write JSON artifact")
    parser.add_argument(
        "--set", action="append", default=[], help="Override key=value pairs"
    )
    args = parser.parse_args()

    overrides: Dict[str, Any] = {}
    for pair in args.set:
        if "=" not in pair:
            raise SystemExit(f"Invalid override '{pair}', expected key=value")
        key, value = pair.split("=", 1)
        overrides[key] = value

    payload = build_payload(args.artifact_type, overrides)
    payload.setdefault("objective", "demonstrate")
    payload.setdefault("constraints", ["dignity"])
    payload.setdefault("evaluationCriteria", ["pass"])
    payload["hash"] = sha3_512_hex(json_dumps(dict(payload)))

    schema = load_schema(SCHEMA_FILES[args.artifact_type])
    schema.validate(payload)

    output = args.output or Path(f"{payload['id']}.json")
    output.write_text(json.dumps(payload, indent=2, sort_keys=True))
    print(f"Wrote {args.artifact_type} artifact to {output}")


if __name__ == "__main__":
    main()
