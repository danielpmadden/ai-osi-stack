from fastapi import APIRouter
from ..schemas.ledger_schema import LedgerEntrySchema
from ..services.ledger_service import list_entries

router = APIRouter(prefix="/ledger", tags=["ledger"])


@router.get("/entries", response_model=list[LedgerEntrySchema])
def get_entries():
  return [LedgerEntrySchema.model_validate(entry) for entry in list_entries()]
