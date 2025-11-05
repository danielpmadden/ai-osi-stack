
"""Bridge module for governance spine common artifacts."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

_RUNTIME_FILE = Path(__file__).resolve().parent.parent.parent / 'governance-spine' / 'runtime' / 'common' / 'artifacts.py'

_spec = importlib.util.spec_from_file_location('govspine.common.artifacts', _RUNTIME_FILE)
assert _spec and _spec.loader
_module = importlib.util.module_from_spec(_spec)
_module.__package__ = 'govspine.common'
sys.modules['govspine.common.artifacts'] = _module
_spec.loader.exec_module(_module)

globals().update({key: getattr(_module, key) for key in dir(_module) if not key.startswith('_')})

__all__ = [key for key in globals() if not key.startswith('_')]
