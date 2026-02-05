import pytest
from sqlalchemy.exc import IntegrityError

from app.models import User


def test_create_user_success(db_session):
    user = User(
        full_name="Jane Doe",
        email="jane@example.com",
        password_hash="hashed",
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    assert user.id is not None
    assert user.role == "student"


def test_duplicate_email_fails(db_session):
    user1 = User(
        full_name="User One",
        email="dup@example.com",
        password_hash="hashed1",
    )
    user2 = User(
        full_name="User Two",
        email="dup@example.com",
        password_hash="hashed2",
    )
    db_session.add(user1)
    db_session.commit()

    db_session.add(user2)
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_missing_email_fails(db_session):
    user = User(full_name="No Email", email=None, password_hash="hashed")
    db_session.add(user)
    with pytest.raises(IntegrityError):
        db_session.commit()
