# SPDX-License-Identifier: Apache-2.0

"""Auto-generated bridge to governance spine runtime module."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

_RUNTIME_DIR = (
    Path(__file__).resolve().parent.parent.parent
    / "govspine"
    / "runtime"
    / "layer6-application"
)

_spec = importlib.util.spec_from_file_location(
    "govspine.layer06application.__impl__",
    _RUNTIME_DIR / "__init__.py",
    submodule_search_locations=[str(_RUNTIME_DIR)],
)
assert _spec and _spec.loader
_module = importlib.util.module_from_spec(_spec)
_module.__package__ = "govspine.layer06application"
sys.modules["govspine.layer06application.__impl__"] = _module
_spec.loader.exec_module(_module)

for _name in dir(_module):
    if not _name.startswith("_"):
        globals()[_name] = getattr(_module, _name)

_validator_spec = importlib.util.spec_from_file_location(
    "govspine.layer06application.validator", _RUNTIME_DIR / "validator.py"
)
assert _validator_spec and _validator_spec.loader
_validator = importlib.util.module_from_spec(_validator_spec)
_validator.__package__ = "govspine.layer06application"
sys.modules["govspine.layer06application.validator"] = _validator
_validator_spec.loader.exec_module(_validator)
validator = _validator

__all__ = [name for name in globals() if not name.startswith("_")]
