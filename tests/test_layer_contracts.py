from __future__ import annotations

from src.layer1_physical import Layer1Physical
from src.layer1_physical.validator import validate as validate_l1
from src.layer2_architecture import Layer2Architecture
from src.layer2_architecture.validator import validate as validate_l2
from src.layer3_training import Layer3Training
from src.layer3_training.validator import validate as validate_l3
from src.layer4_instruction import Layer4Instruction
from src.layer4_instruction.validator import validate as validate_l4
from src.layer5_interface import Layer5Interface
from src.layer5_interface.validator import validate as validate_l5
from src.layer6_application import Layer6Application
from src.layer6_application.validator import validate as validate_l6
from src.layer7_governance import Layer7Governance
from src.layer7_governance.validator import validate as validate_l7
from src.layer8_policy import Layer8Policy
from src.layer8_policy.validator import validate as validate_l8


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
