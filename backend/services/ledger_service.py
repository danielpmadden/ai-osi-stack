from typing import List
from ..models.ledger import LedgerEntry, sample_ledger


def list_entries() -> List[LedgerEntry]:
  return sample_ledger()
