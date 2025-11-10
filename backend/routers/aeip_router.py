from fastapi import APIRouter
from ..schemas.aeip_schema import AEIPReceiptSchema
from ..services.aeip_service import list_receipts

router = APIRouter(prefix="/aeip", tags=["aeip"])


@router.get("/receipts", response_model=list[AEIPReceiptSchema])
def get_receipts():
  return [AEIPReceiptSchema.model_validate(receipt) for receipt in list_receipts()]
