import pytest
from sqlalchemy.exc import IntegrityError

from app.models import Notification


def test_create_notification_success(db_session):
    note = Notification(
        user_id="00000000-0000-0000-0000-000000000011",
        type="answer_on_my_question",
        payload={"question_id": "00000000-0000-0000-0000-000000000012"},
    )
    db_session.add(note)
    db_session.commit()
    db_session.refresh(note)

    assert note.id is not None
    assert note.is_read is False


def test_missing_type_fails(db_session):
    note = Notification(
        user_id="00000000-0000-0000-0000-000000000013",
        type=None,
        payload={"key": "value"},
    )
    db_session.add(note)
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_missing_payload_fails(db_session):
    note = Notification(
        user_id="00000000-0000-0000-0000-000000000014",
        type="vote_on_my_post",
        payload=None,
    )
    db_session.add(note)
    with pytest.raises(IntegrityError):
        db_session.commit()
