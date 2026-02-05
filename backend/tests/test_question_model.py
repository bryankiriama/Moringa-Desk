import pytest
from sqlalchemy.exc import IntegrityError

from app.models import Question, User


def create_user(db_session):
    user = User(
        full_name="Jane Doe",
        email="author@example.com",
        password_hash="hashed",
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


def test_create_question_success(db_session):
    user = create_user(db_session)
    question = Question(
        author_id=user.id,
        title="How to use SQLAlchemy?",
        body="I need help with relationships.",
        category="technical",
        stage="phase-3",
    )
    db_session.add(question)
    db_session.commit()
    db_session.refresh(question)

    assert question.id is not None
    assert question.status == "open"


def test_question_missing_title_fails(db_session):
    user = create_user(db_session)
    question = Question(author_id=user.id, title=None, body="Body")
    db_session.add(question)
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_question_missing_body_fails(db_session):
    user = create_user(db_session)
    question = Question(author_id=user.id, title="Title", body=None)
    db_session.add(question)
    with pytest.raises(IntegrityError):
        db_session.commit()
