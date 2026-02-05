import pytest
from sqlalchemy.exc import IntegrityError

from app.models import Faq, User


def create_admin(db_session):
    admin = User(
        full_name="Admin",
        email="admin@example.com",
        password_hash="hashed",
        role="admin",
    )
    db_session.add(admin)
    db_session.commit()
    db_session.refresh(admin)
    return admin


def test_create_faq_success(db_session):
    admin = create_admin(db_session)
    faq = Faq(question="How to reset password?", answer="Use settings.", created_by=admin.id)
    db_session.add(faq)
    db_session.commit()
    db_session.refresh(faq)

    assert faq.id is not None


def test_missing_question_fails(db_session):
    admin = create_admin(db_session)
    faq = Faq(question=None, answer="Answer", created_by=admin.id)
    db_session.add(faq)
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_missing_answer_fails(db_session):
    admin = create_admin(db_session)
    faq = Faq(question="Q", answer=None, created_by=admin.id)
    db_session.add(faq)
    with pytest.raises(IntegrityError):
        db_session.commit()
