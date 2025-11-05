#!/usr/bin/env python3
"""Privacy conformance CLI for AEIP artifacts.

The tool validates that required privacy and consent metadata is present and
provides actionable feedback that references the canonical governance stack.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REQUIRED_KEYS = {
    "privacy": ["processingBasis", "dataCategories"],
    "consent": ["record", "scope"],
}

OPTIONAL_KEYS = {
    "privacy": ["retentionSchedule", "mitigations"],
    "consent": ["status"],
}


def load_artifact(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError as exc:
        raise SystemExit(f"Artifact not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Artifact is not valid JSON: {exc}") from exc


def validate_structure(artifact: dict) -> list[str]:
    errors: list[str] = []
    for namespace, keys in REQUIRED_KEYS.items():
        node = artifact.get(namespace)
        if node is None:
            errors.append(
                f"Missing '{namespace}' node required by Update Plan 10 privacy additions."
            )
            continue
        if not isinstance(node, dict):
            errors.append(
                f"The '{namespace}' node must be an object; received {type(node).__name__}."
            )
            continue
        for key in keys:
            if key not in node or node[key] in (None, ""):
                errors.append(
                    f"Missing '{namespace}.{key}' metadata mandated for AEIP v1.3 conformance."
                )
    return errors


def build_report(artifact: dict) -> str:
    lines = ["AEIP Privacy Conformance"]
    lines.append("-------------------------")
    for namespace, keys in REQUIRED_KEYS.items():
        lines.append(f"Namespace: {namespace}")
        node = artifact.get(namespace, {})
        for key in keys + OPTIONAL_KEYS.get(namespace, []):
            value = node.get(key)
            status = "present" if value not in (None, "") else "missing"
            lines.append(f"  - {key}: {status}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path, help="Path to the AEIP artifact JSON file")
    parser.add_argument(
        "--report",
        action="store_true",
        help="Print a conformance report regardless of validation outcome",
    )
    args = parser.parse_args(argv)

    artifact = load_artifact(args.artifact)
    errors = validate_structure(artifact)

    if args.report:
        print(build_report(artifact))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(
            "Validation failed: ensure privacy and consent metadata are captured per Update Plan 10.",
            file=sys.stderr,
        )
        return 1

    print("Artifact meets AEIP v1.3 privacy conformance requirements.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
