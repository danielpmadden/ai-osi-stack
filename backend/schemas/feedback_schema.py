from datetime import datetime
from pydantic import BaseModel


class FeedbackSchema(BaseModel):
  id: str
  source: str
  submitted_at: datetime
  message: str

  class Config:
    from_attributes = True
