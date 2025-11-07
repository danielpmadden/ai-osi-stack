"""Manifest metadata regression tests.

The module ensures canonical metadata remains stable across updates and
verifies that interpretive chapters are declared for downstream tooling.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "meta" / "v5-manifest.yaml"


def _extract_manifest_metadata() -> Tuple[str | None, List[Tuple[str, str]]]:
    canonical_version: str | None = None
    interpretive_pairs: List[Tuple[str, str]] = []
    in_interpretive_block = False

    with MANIFEST_PATH.open("r", encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.rstrip()
            stripped = line.strip()

            if stripped.startswith("#") or not stripped:
                continue

            if stripped.startswith("canonical_version:"):
                value = stripped.split(":", 1)[1].strip()
                canonical_version = value.strip('"')
                continue

            if stripped.startswith("interpretive_and_applied_chapters:"):
                in_interpretive_block = True
                continue

            if in_interpretive_block:
                if not stripped.startswith("- "):
                    in_interpretive_block = False
                    continue
                entry = stripped[2:]
                if ":" not in entry:
                    raise ValueError("Malformed interpretive chapter entry: missing colon")
                key, value = entry.split(":", 1)
                interpretive_pairs.append((key.strip(), value.strip()))

    return canonical_version, interpretive_pairs


def _load_interpretive_dict() -> Dict[str, str]:
    canonical_version, pairs = _extract_manifest_metadata()
    assert canonical_version == "5.0.0", "Canonical version drift detected"
    manifest_map: Dict[str, str] = {}
    for key, value in pairs:
        manifest_map[key] = value
    return manifest_map


def test_canonical_version_remains_five_zero_zero() -> None:
    canonical_version, _ = _extract_manifest_metadata()
    assert canonical_version == "5.0.0"


def test_interpretive_chapters_declared_in_manifest() -> None:
    manifest_map = _load_interpretive_dict()
    expected = {
        "19A": "Usage, Trust & Social Reality",
        "20": "Rhetoric & Semantics",
        "21": "The Companion Trap",
        "22": "Persona Architecture",
        "23": "Therapy-Tech & Governance of Care",
        "24": "Governance Paradox",
    }
    assert manifest_map == expected, "Interpretive chapters must match canonical ordering and titles"
