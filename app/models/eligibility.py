# app/models/eligibility.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    input_type = Column(String)
    required_answer_boolean = Column(Boolean, nullable=True)

class ServiceQuestion(Base):
    __tablename__ = "service_questions"

    id = Column(Integer, primary_key=True, index=True)
    service_id = Column(Integer, ForeignKey("services.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    sequence_order = Column(Integer)

    # Relationships
    question = relationship("Question")