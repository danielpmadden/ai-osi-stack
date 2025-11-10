from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Feedback:
  id: str
  source: str
  submitted_at: datetime
  message: str


def sample_feedback() -> List[Feedback]:
  return [
    Feedback(
      id="feedback-001",
      source="Layer 8 Civic Loop",
      submitted_at=datetime.fromisoformat("2024-05-18T00:00:00"),
      message="Stakeholders request clearer handshake transparency.",
    )
  ]
