#!/usr/bin/env python3
"""Generate AEIP-compliant manifests for governance spine assets."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Sequence

REPO_ROOT = Path(__file__).resolve().parents[1]
SPINE_ROOT = REPO_ROOT / "govspine"

ASSET_MAP: Dict[str, str] = {
    "charter": "charters",
    "compute": "compute",
    "data": "data",
    "model": "models",
    "control": "control",
    "aeip": "aeip",
    "deployment": "deployments",
}

CONTEXT = {
    "aeip": "https://danielpmadden.com/ns/aeip#",
    "schema": "http://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "security": "https://w3id.org/security#",
    "privacy": "https://danielpmadden.com/ns/privacy#",
    "consent": "https://danielpmadden.com/ns/consent#",
}


@dataclass
class ManifestOptions:
    asset_type: str
    artifact_id: str
    version: str
    lifecycle: str
    layer: str
    owner: str
    description: str
    processing_basis: str
    data_categories: Sequence[str]
    consent_scope: str
    consent_record: str
    risk_tier: str
    tags: Sequence[str]
    receipts: Sequence[str]
    links: Sequence[str]
    control_mappings: Sequence[str]
    output: Path | None


def _slugify(value: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")


def _parse_kv(values: Sequence[str]) -> List[Dict[str, str]]:
    parsed: List[Dict[str, str]] = []
    for value in values:
        if not value:
            continue
        if "::" in value:
            framework, control = value.split("::", 1)
        elif ":" in value:
            framework, control = value.split(":", 1)
        else:
            framework, control = value, ""
        parsed.append({"framework": framework.strip(), "control": control.strip()})
    return parsed


def build_manifest(opts: ManifestOptions) -> Dict[str, object]:
    data_categories = [
        item for item in (cat.strip() for cat in opts.data_categories) if item
    ]
    if not data_categories:
        data_categories = ["metadata"]

    tags = [item for item in (tag.strip() for tag in opts.tags) if item]
    receipts = [item for item in (rcpt.strip() for rcpt in opts.receipts) if item]
    links = [item for item in (lnk.strip() for lnk in opts.links) if item]
    controls = [
        mapping for mapping in _parse_kv(opts.control_mappings) if mapping["framework"]
    ]

    manifest: Dict[str, object] = {
        "@context": CONTEXT,
        "aeip:artifactId": opts.artifact_id,
        "aeip:version": opts.version,
        "aeip:lifecycleStage": opts.lifecycle,
        "aeip:layerPath": opts.layer,
        "aeip:assetType": opts.asset_type,
        "aeip:description": opts.description,
        "aeip:governanceOwner": opts.owner,
        "aeip:riskTier": opts.risk_tier,
        "aeip:lastReview": datetime.now(tz=timezone.utc).isoformat(),
        "aeip:governanceTags": tags,
        "aeip:receipts": receipts,
        "aeip:linkedManifests": links,
        "aeip:controlMappings": controls,
        "privacy:processingBasis": opts.processing_basis,
        "privacy:dataCategories": data_categories,
        "consent:record": opts.consent_record,
        "consent:scope": opts.consent_scope,
    }

    return manifest


def _resolve_output(opts: ManifestOptions) -> Path:
    target_dir = SPINE_ROOT / ASSET_MAP[opts.asset_type]
    target_dir.mkdir(parents=True, exist_ok=True)
    file_stem = _slugify(opts.artifact_id) or opts.artifact_id
    return opts.output or target_dir / f"{file_stem}.aeip.json"


def parse_args() -> ManifestOptions:
    parser = argparse.ArgumentParser(
        description="Generate AEIP manifests for governance spine assets.",
    )

    type_group = parser.add_mutually_exclusive_group(required=True)
    for asset_choice in ASSET_MAP:
        type_group.add_argument(
            f"--{asset_choice}",
            dest="asset_type",
            action="store_const",
            const=asset_choice,
            help=f"Generate a manifest for {asset_choice} assets.",
        )

    parser.add_argument(
        "--artifact-id",
        required=True,
        help="Deterministic identifier for the governed asset.",
    )
    parser.add_argument(
        "--version",
        default="1.3.0",
        help="Semantic version for the manifested artifact.",
    )
    parser.add_argument(
        "--lifecycle",
        default="design",
        help="Lifecycle state for the asset (design, validation, deployment, archive).",
    )
    parser.add_argument(
        "--layer", default="L0", help="Stack layer lineage (e.g., L3.RX)."
    )
    parser.add_argument(
        "--owner", required=True, help="Governance owner or custodial body."
    )
    parser.add_argument(
        "--description",
        default="",
        help="Short description of the asset or governance obligation.",
    )
    parser.add_argument(
        "--processing-basis",
        default="legitimate_interest",
        help="Privacy processing basis used to operate the asset.",
    )
    parser.add_argument(
        "--data-category",
        action="append",
        dest="data_categories",
        default=[],
        help="Data categories processed by the asset (repeatable).",
    )
    parser.add_argument(
        "--consent-scope",
        default="governance_spine",
        help="Consent scope linked to this manifest.",
    )
    parser.add_argument(
        "--consent-record",
        default="ledger://consent/placeholder",
        help="Reference to the consent record in the hermeneutic ledger.",
    )
    parser.add_argument(
        "--risk-tier", default="T2", help="Risk tier classification for the asset."
    )
    parser.add_argument(
        "--tag",
        action="append",
        dest="tags",
        default=[],
        help="Governance tags for discovery (repeatable).",
    )
    parser.add_argument(
        "--receipt",
        action="append",
        dest="receipts",
        default=[],
        help="Ledger receipt references that evidence compliance (repeatable).",
    )
    parser.add_argument(
        "--link",
        action="append",
        dest="links",
        default=[],
        help="Linked manifest identifiers (repeatable).",
    )
    parser.add_argument(
        "--control",
        action="append",
        dest="control_mappings",
        default=[],
        help="Control mappings in 'Framework:Control' form (repeatable).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Override output file path (defaults to govspine/<type>/<artifact>.aeip.json).",
    )

    args = parser.parse_args()

    return ManifestOptions(
        asset_type=args.asset_type,
        artifact_id=args.artifact_id,
        version=args.version,
        lifecycle=args.lifecycle,
        layer=args.layer,
        owner=args.owner,
        description=args.description,
        processing_basis=args.processing_basis,
        data_categories=args.data_categories,
        consent_scope=args.consent_scope,
        consent_record=args.consent_record,
        risk_tier=args.risk_tier,
        tags=args.tags,
        receipts=args.receipts,
        links=args.links,
        control_mappings=args.control_mappings,
        output=args.output,
    )


def main() -> int:
    opts = parse_args()
    manifest = build_manifest(opts)
    output_path = _resolve_output(opts)
    output_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"AEIP manifest generated: {output_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
