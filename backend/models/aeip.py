from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Handshake:
  counterpart: str
  next_action: str


@dataclass
class AEIPReceipt:
  id: str
  layer_id: str
  issued_at: datetime
  status: str
  summary: str
  handshake: Handshake


def sample_receipts() -> List[AEIPReceipt]:
  return [
    AEIPReceipt(
      id="aeip-001",
      layer_id="layer-1",
      issued_at=datetime.fromisoformat("2024-05-16T10:00:00"),
      status="complete",
      summary="Handshake with Civic Signals confirmed",
      handshake=Handshake(counterpart="City Data Office", next_action="Deliver weekly brief"),
    ),
    AEIPReceipt(
      id="aeip-099",
      layer_id="layer-8",
      issued_at=datetime.fromisoformat("2024-05-18T08:30:00"),
      status="pending",
      summary="Awaiting sign-off from Policy & Federation",
      handshake=Handshake(counterpart="Federal Liaison", next_action="Schedule review"),
    ),
  ]
