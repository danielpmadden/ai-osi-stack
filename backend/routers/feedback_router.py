from fastapi import APIRouter
from ..schemas.feedback_schema import FeedbackSchema
from ..services.feedback_service import list_feedback

router = APIRouter(prefix="/feedback", tags=["feedback"])


@router.get("", response_model=list[FeedbackSchema])
def get_feedback():
  return [FeedbackSchema.model_validate(item) for item in list_feedback()]
