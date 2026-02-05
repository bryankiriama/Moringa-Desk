import pytest
from sqlalchemy.exc import IntegrityError

from app.models import Answer, Question, User


def create_user(db_session, email):
    user = User(
        full_name="User",
        email=email,
        password_hash="hashed",
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


def create_question(db_session, author_id):
    question = Question(
        author_id=author_id,
        title="How does acceptance work?",
        body="Explain accepted answers.",
    )
    db_session.add(question)
    db_session.commit()
    db_session.refresh(question)
    return question


def test_create_answer_success(db_session):
    author = create_user(db_session, "a1@example.com")
    question = create_question(db_session, author.id)
    answer = Answer(
        question_id=question.id,
        author_id=author.id,
        body="This is an answer.",
    )
    db_session.add(answer)
    db_session.commit()
    db_session.refresh(answer)

    assert answer.id is not None
    assert answer.is_accepted is False


def test_answer_missing_body_fails(db_session):
    author = create_user(db_session, "a2@example.com")
    question = create_question(db_session, author.id)
    answer = Answer(question_id=question.id, author_id=author.id, body=None)
    db_session.add(answer)
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_answer_missing_question_fails(db_session):
    author = create_user(db_session, "a3@example.com")
    answer = Answer(question_id=None, author_id=author.id, body="text")
    db_session.add(answer)
    with pytest.raises(IntegrityError):
        db_session.commit()
