# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from govspine.layer01physical import Layer1Physical
from govspine.layer01physical.validator import validate as validate_l1
from govspine.layer02architecture import Layer2Architecture
from govspine.layer02architecture.validator import validate as validate_l2
from govspine.layer03training import Layer3Training
from govspine.layer03training.validator import validate as validate_l3
from govspine.layer04instruction import Layer4Instruction
from govspine.layer04instruction.validator import validate as validate_l4
from govspine.layer05interface import Layer5Interface
from govspine.layer05interface.validator import validate as validate_l5
from govspine.layer06application import Layer6Application
from govspine.layer06application.validator import validate as validate_l6
from govspine.layer07governance import Layer7Governance
from govspine.layer07governance.validator import validate as validate_l7
from govspine.layer08policy import Layer8Policy
from govspine.layer08policy.validator import validate as validate_l8


def test_layer_chain_contracts() -> None:
    l1 = Layer1Physical()
    l2 = Layer2Architecture()
    l3 = Layer3Training()
    l4 = Layer4Instruction()
    l5 = Layer5Interface()
    l6 = Layer6Application()
    l7 = Layer7Governance()
    l8 = Layer8Policy()

    payload = {"physicalEvidence": {"power": "ok", "cooling": "ok"}}
    out1 = l1.process(payload)
    validate_l1(out1)

    out2 = l2.process(out1)
    validate_l2(out2)

    out3 = l3.process(out2)
    validate_l3(out3)

    out4 = l4.process(out3)
    validate_l4(out4)
    assert "temporalSeal" in out4["instructionPacket"]

    out5 = l5.process(out4)
    validate_l5(out5)

    out6 = l6.process(out5)
    validate_l6(out6)

    out7 = l7.process(out6)
    validate_l7(out7)

    out8 = l8.process(out7)
    validate_l8(out8)
    assert out8["policyDirective"]["policyIntent"]
    assert "temporalSeal" in out8["policyDirective"]
