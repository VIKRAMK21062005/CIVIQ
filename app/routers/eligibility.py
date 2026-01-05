# app/routers/eligibility.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db

# 1. Correct Model Imports (Database Tables)
from app.models.eligibility import ServiceQuestion, Question 

# 2. Correct Schema Imports (Pydantic Models)
from app.schemas.eligibility import QuestionOut, AnswerSubmit, EligibilityResult

router = APIRouter()

# --- Endpoint 1: CHECK ANSWERS (POST) ---
@router.post("/services/{service_id}/check", response_model=EligibilityResult)
def check_eligibility(
    service_id: int, 
    answers: List[AnswerSubmit], 
    db: Session = Depends(get_db)
):
    """
    Receives user answers and checks if they match the requirements.
    """
    is_eligible = True
    fail_reasons = []

    for user_ans in answers:
        # Get the real question from DB to check the correct answer
        question_db = db.query(Question).filter(Question.id == user_ans.question_id).first()
        
        if question_db and question_db.required_answer_boolean is not None:
            # Compare User Answer vs Required Answer
            if user_ans.answer != question_db.required_answer_boolean:
                is_eligible = False
                fail_reasons.append(f"Failed requirement: {question_db.text}")

    if is_eligible:
        return {"is_eligible": True, "message": "You are eligible for this service!"}
    else:
        return {"is_eligible": False, "message": "Not Eligible. " + " ".join(fail_reasons)}


# --- Endpoint 2: GET QUESTIONS (GET) ---
@router.get("/services/{service_id}/questions", response_model=List[QuestionOut])
def get_questions_for_service(service_id: int, db: Session = Depends(get_db)):
    """
    Fetch the list of eligibility questions for a specific service.
    """
    service_questions = db.query(ServiceQuestion).filter(
        ServiceQuestion.service_id == service_id
    ).order_by(ServiceQuestion.sequence_order).all()

    results = []
    for sq in service_questions:
        results.append({
            "id": sq.question.id,
            "text": sq.question.text,
            "input_type": sq.question.input_type,
            "sequence_order": sq.sequence_order
        })
    
    return results