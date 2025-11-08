# SPDX-License-Identifier: Apache-2.0

"""Bridge package exposing governance spine runtime modules."""

from __future__ import annotations

from importlib import import_module

__all__ = [
    "layer01physical",
    "layer02architecture",
    "layer03training",
    "layer04instruction",
    "layer05interface",
    "layer06application",
    "layer07governance",
    "layer08policy",
    "common",
]

for _name in __all__:
    if _name == "common":
        globals()[_name] = import_module(f"{__name__}.{_name}")
    else:
        globals()[_name] = import_module(f"{__name__}.{_name}")
