import pytest
from sqlalchemy.exc import IntegrityError

from app.models import Follow, Question, User


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
        title="Follow question",
        body="Testing follows.",
    )
    db_session.add(question)
    db_session.commit()
    db_session.refresh(question)
    return question


def test_create_follow_success(db_session):
    author = create_user(db_session, "f1@example.com")
    follower = create_user(db_session, "f2@example.com")
    question = create_question(db_session, author.id)

    follow = Follow(user_id=follower.id, question_id=question.id)
    db_session.add(follow)
    db_session.commit()
    db_session.refresh(follow)

    assert follow.id is not None


def test_duplicate_follow_fails(db_session):
    author = create_user(db_session, "f3@example.com")
    follower = create_user(db_session, "f4@example.com")
    question = create_question(db_session, author.id)

    follow1 = Follow(user_id=follower.id, question_id=question.id)
    follow2 = Follow(user_id=follower.id, question_id=question.id)
    db_session.add(follow1)
    db_session.commit()

    db_session.add(follow2)
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_missing_question_fails(db_session):
    follower = create_user(db_session, "f5@example.com")
    follow = Follow(user_id=follower.id, question_id=None)
    db_session.add(follow)
    with pytest.raises(IntegrityError):
        db_session.commit()
