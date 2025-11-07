"""Bridge package for shared governance spine utilities."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

_RUNTIME_BASE = (
    Path(__file__).resolve().parent.parent.parent
    / "governance-spine"
    / "runtime"
    / "common"
)

_spec = importlib.util.spec_from_file_location(
    "govspine.common.__impl__",
    _RUNTIME_BASE / "__init__.py",
    submodule_search_locations=[str(_RUNTIME_BASE)],
)
assert _spec and _spec.loader
_module = importlib.util.module_from_spec(_spec)
_module.__package__ = "govspine.common"
sys.modules["govspine.common.__impl__"] = _module
_spec.loader.exec_module(_module)

for _name in dir(_module):
    if not _name.startswith("_"):
        globals()[_name] = getattr(_module, _name)

__all__ = [name for name in globals() if not name.startswith("_")]
