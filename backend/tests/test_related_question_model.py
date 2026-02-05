import pytest
from sqlalchemy.exc import IntegrityError

from app.models import Question, RelatedQuestion, User


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


def create_question(db_session, author_id, title):
    question = Question(
        author_id=author_id,
        title=title,
        body="Body",
    )
    db_session.add(question)
    db_session.commit()
    db_session.refresh(question)
    return question


def test_create_related_question_success(db_session):
    author = create_user(db_session, "rq1@example.com")
    q1 = create_question(db_session, author.id, "Question 1")
    q2 = create_question(db_session, author.id, "Question 2")

    link = RelatedQuestion(question_id=q1.id, related_question_id=q2.id)
    db_session.add(link)
    db_session.commit()
    db_session.refresh(link)

    assert link.question_id == q1.id
    assert link.related_question_id == q2.id


def test_missing_related_question_fails(db_session):
    author = create_user(db_session, "rq2@example.com")
    q1 = create_question(db_session, author.id, "Question 1")

    link = RelatedQuestion(question_id=q1.id, related_question_id=None)
    db_session.add(link)
    with pytest.raises(IntegrityError):
        db_session.commit()
