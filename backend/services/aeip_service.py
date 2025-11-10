from typing import List
from ..models.aeip import AEIPReceipt, sample_receipts


def list_receipts() -> List[AEIPReceipt]:
  return sample_receipts()
