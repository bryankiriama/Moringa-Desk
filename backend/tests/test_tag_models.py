import pytest
from sqlalchemy.exc import IntegrityError

from app.models import Question, QuestionTag, Tag, User


def create_user(db_session):
    user = User(
        full_name="Jane Doe",
        email="author_tag@example.com",
        password_hash="hashed",
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


def create_question(db_session, user_id):
    question = Question(
        author_id=user_id,
        title="Tagging questions",
        body="How do tags work?",
    )
    db_session.add(question)
    db_session.commit()
    db_session.refresh(question)
    return question


def test_create_tag_success(db_session):
    tag = Tag(name="Python")
    db_session.add(tag)
    db_session.commit()
    db_session.refresh(tag)

    assert tag.id is not None


def test_duplicate_tag_name_fails(db_session):
    tag1 = Tag(name="React")
    tag2 = Tag(name="React")
    db_session.add(tag1)
    db_session.commit()

    db_session.add(tag2)
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_create_question_tag_success(db_session):
    user = create_user(db_session)
    question = create_question(db_session, user.id)
    tag = Tag(name="Databases")
    db_session.add(tag)
    db_session.commit()
    db_session.refresh(tag)

    link = QuestionTag(question_id=question.id, tag_id=tag.id)
    db_session.add(link)
    db_session.commit()
    db_session.refresh(link)

    assert link.question_id == question.id
    assert link.tag_id == tag.id


def test_missing_tag_id_fails(db_session):
    user = create_user(db_session)
    question = create_question(db_session, user.id)

    link = QuestionTag(question_id=question.id, tag_id=None)
    db_session.add(link)
    with pytest.raises(IntegrityError):
        db_session.commit()
