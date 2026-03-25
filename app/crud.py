from app import models

def create_student(db, student):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def get_students(db):
    return db.query(models.Student).all()

def add_quiz_result(db, data):
    result = models.QuizResult(**data.dict())
    db.add(result)
    db.commit()
    db.refresh(result)
    return result


def get_quiz_results(db):
    return db.query(models.QuizResult).all()

from datetime import datetime, timedelta

def create_flashcard(db, data):
    next_review = datetime.utcnow() + timedelta(days=1)

    flashcard = models.Flashcard(
        student_id=data.student_id,
        question=data.question,
        answer=data.answer,
        next_review=next_review
    )

    db.add(flashcard)
    db.commit()
    db.refresh(flashcard)
    return flashcard


def get_flashcards(db):
    return db.query(models.Flashcard).all()