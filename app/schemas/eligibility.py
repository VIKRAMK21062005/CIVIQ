# app/schemas/eligibility.py
from pydantic import BaseModel

class QuestionOut(BaseModel):
    id: int
    text: str
    input_type: str
    sequence_order: int

    class Config:
        from_attributes = True

# NEW CLASSES FOR CHECKING:
class AnswerSubmit(BaseModel):
    question_id: int
    answer: bool

class EligibilityResult(BaseModel):
    is_eligible: bool
    message: str