# SPDX-License-Identifier: Apache-2.0

"""Protocol helpers for the AI OSI reference stack."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

_BASE = Path(__file__).resolve().parent


_definitions = {
    "protocol.aeip_handshake": _BASE / "aeip-handshake.py",
    "protocol.ledger_node": _BASE / "ledger-node.py",
}

modules = {}
for name, file_path in _definitions.items():
    spec = importlib.util.spec_from_file_location(name, file_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    module.__package__ = "protocol"
    sys.modules[name] = module
    spec.loader.exec_module(module)
    modules[name] = module

AEIPHandshake = modules["protocol.aeip_handshake"].AEIPHandshake
AEIP_STEPS = modules["protocol.aeip_handshake"].AEIP_STEPS
HandshakeError = modules["protocol.aeip_handshake"].HandshakeError

GovernanceLedgerNode = modules["protocol.ledger_node"].GovernanceLedgerNode
LedgerVerificationError = modules["protocol.ledger_node"].LedgerVerificationError

__all__ = [
    "AEIPHandshake",
    "AEIP_STEPS",
    "GovernanceLedgerNode",
    "HandshakeError",
    "LedgerVerificationError",
]
