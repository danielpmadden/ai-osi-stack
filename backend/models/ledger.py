from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class LedgerEntry:
  id: str
  title: str
  status: str
  updated_at: date


def sample_ledger() -> List[LedgerEntry]:
  return [
    LedgerEntry(id="ledger-001", title="Civic Signals Ledger Snapshot", status="verified", updated_at=date(2024, 5, 10)),
    LedgerEntry(id="ledger-002", title="Policy Federation Commitment", status="draft", updated_at=date(2024, 5, 18)),
  ]
