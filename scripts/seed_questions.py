# scripts/seed_questions.py
import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.service import Service
from app.models.eligibility import Question, ServiceQuestion

def seed_eligibility():
    db: Session = SessionLocal()
    print("🧠 Seeding Eligibility Logic...")

    # 1. Create Common Questions
    # We define the question AND the "Correct Answer" needed to pass.
    q_age = Question(text="Are you over 18 years old?", input_type="yes_no", required_answer_boolean=True)
    q_damaged = Question(text="Is your current passport damaged or lost?", input_type="yes_no", required_answer_boolean=False)
    q_insurance = Question(text="Do you have valid vehicle insurance?", input_type="yes_no", required_answer_boolean=True)
    q_resident = Question(text="Are you a resident of the state?", input_type="yes_no", required_answer_boolean=True)
    q_biz_plan = Question(text="Do you have a registered business plan?", input_type="yes_no", required_answer_boolean=True)

    # Add questions to DB
    all_questions = [q_age, q_damaged, q_insurance, q_resident, q_biz_plan]
    for q in all_questions:
        db.add(q)
    db.commit() # Commit to get IDs

    # 2. Link Questions to Services
    # We need to find the Service IDs first
    passport = db.query(Service).filter(Service.name == "Passport Renewal").first()
    vehicle = db.query(Service).filter(Service.name == "Vehicle Registration Renewal").first()
    business = db.query(Service).filter(Service.name == "Small Business Grant").first()

    if passport:
        # Passport needs: Resident? -> Over 18? -> Not Damaged?
        db.add(ServiceQuestion(service_id=passport.id, question_id=q_resident.id, sequence_order=1))
        db.add(ServiceQuestion(service_id=passport.id, question_id=q_age.id, sequence_order=2))
        db.add(ServiceQuestion(service_id=passport.id, question_id=q_damaged.id, sequence_order=3))
        print(f"   Linked 3 questions to {passport.name}")

    if vehicle:
        # Vehicle needs: Resident? -> Insurance?
        db.add(ServiceQuestion(service_id=vehicle.id, question_id=q_resident.id, sequence_order=1))
        db.add(ServiceQuestion(service_id=vehicle.id, question_id=q_insurance.id, sequence_order=2))
        print(f"   Linked 2 questions to {vehicle.name}")

    if business:
        # Business needs: Resident? -> Business Plan?
        db.add(ServiceQuestion(service_id=business.id, question_id=q_resident.id, sequence_order=1))
        db.add(ServiceQuestion(service_id=business.id, question_id=q_biz_plan.id, sequence_order=2))
        print(f"   Linked 2 questions to {business.name}")

    db.commit()
    db.close()
    print("✅ Eligibility Rules Loaded!")

if __name__ == "__main__":
    seed_eligibility()