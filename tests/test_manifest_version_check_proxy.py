# SPDX-License-Identifier: Apache-2.0

"""Pytest bridge for manifest-version-check module."""

from __future__ import annotations

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parent / "manifest-version-check.py"
_spec = importlib.util.spec_from_file_location("manifest_version_check", MODULE_PATH)
_manifest_module = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_manifest_module)  # type: ignore[misc]


def test_canonical_version_remains_five_zero_zero_proxy() -> None:
    _manifest_module.test_canonical_version_remains_five_zero_zero()


def test_interpretive_chapters_declared_proxy() -> None:
    _manifest_module.test_interpretive_chapters_declared_in_manifest()
