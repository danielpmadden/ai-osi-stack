from typing import List
from ..models.feedback import Feedback, sample_feedback


def list_feedback() -> List[Feedback]:
  return sample_feedback()
