# SPDX-License-Identifier: Apache-2.0

#!/usr/bin/env python3
"""Federation validator enforcing Policy Partnership Charter (Update Plan 13).

The validator inspects federation manifests to ensure that every policy partner
is properly registered with the Federated Cohort Registry (FCR) and that AEIP
integration hooks are declared for bidirectional governance updates.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None

REQUIRED_ROOT_KEYS = {"federation", "fcr"}
REQUIRED_PARTNER_KEYS = {"id", "jurisdiction", "aeipHook", "policyScope"}


def load_manifest(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"Manifest not found: {path}")

    if path.suffix.lower() in {".yaml", ".yml"}:
        if yaml is None:
            raise SystemExit("PyYAML is required to parse YAML manifests.")
        with path.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle) or {}

    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_root(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_ROOT_KEYS - manifest.keys()
    if missing:
        errors.append("Missing required top-level keys: " + ", ".join(sorted(missing)))
        return errors

    if not isinstance(manifest["federation"], dict):
        errors.append("'federation' must be an object containing charter metadata.")
    else:
        charter = manifest["federation"].get("charterVersion")
        if charter is None:
            errors.append("Federation charterVersion is required (Update Plan 13 §3).")

    fcr = manifest.get("fcr")
    if not isinstance(fcr, dict):
        errors.append("FCR section must be an object with registry metadata.")
    else:
        if "registryId" not in fcr:
            errors.append("FCR registryId is required to trace credential scope.")
        if "partnerRegistry" not in fcr or not isinstance(fcr["partnerRegistry"], list):
            errors.append(
                "FCR partnerRegistry must list registered partner identifiers."
            )
    return errors


def iter_partners(manifest: dict[str, Any]) -> Iterable[dict[str, Any]]:
    partners = manifest.get("partners", [])
    if not isinstance(partners, list):
        return []
    return [p for p in partners if isinstance(p, dict)]


def validate_partners(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    registered = set()
    fcr_registry = set(manifest.get("fcr", {}).get("partnerRegistry", []))
    for partner in iter_partners(manifest):
        partner_id = partner.get("id", "<unknown>")
        registered.add(partner_id)
        missing = [key for key in REQUIRED_PARTNER_KEYS if key not in partner]
        if missing:
            errors.append(f"Partner {partner_id} missing fields: {', '.join(missing)}")
        hook = partner.get("aeipHook")
        if hook and not hook.startswith("https://"):
            errors.append(
                f"Partner {partner_id} AEIP hook must be HTTPS endpoint; got '{hook}'."
            )
    if registered - fcr_registry:
        errors.append(
            "All partners must appear in the FCR partnerRegistry (Update Plan 13 §4)."
        )
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "manifest", type=Path, help="Path to federation manifest (JSON or YAML)"
    )
    args = parser.parse_args(argv)

    manifest = load_manifest(args.manifest)
    errors = validate_root(manifest)
    errors.extend(validate_partners(manifest))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print("Federation manifest does not comply with Policy Partnership Charter.")
        return 1

    print(
        "Federation manifest validated against FCR and AEIP integration requirements."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
