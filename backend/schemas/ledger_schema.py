from datetime import date
from pydantic import BaseModel


class LedgerEntrySchema(BaseModel):
  id: str
  title: str
  status: str
  updated_at: date

  class Config:
    from_attributes = True
