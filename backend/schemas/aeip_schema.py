from datetime import datetime
from pydantic import BaseModel


class HandshakeSchema(BaseModel):
  counterpart: str
  next_action: str


class AEIPReceiptSchema(BaseModel):
  id: str
  layer_id: str
  issued_at: datetime
  status: str
  summary: str
  handshake: HandshakeSchema

  class Config:
    from_attributes = True
