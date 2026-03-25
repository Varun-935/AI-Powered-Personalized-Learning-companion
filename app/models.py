from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from app.db import Base
import datetime

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    interest = Column(String)


class QuizResult(Base):
    __tablename__ = "quiz_results"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    topic = Column(String)
    score = Column(Float)


class Flashcard(Base):
    __tablename__ = "flashcards"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    question = Column(String)
    answer = Column(String)
    next_review = Column(DateTime, default=datetime.datetime.utcnow)