import pytest
from sqlalchemy.exc import IntegrityError

from app.models import Vote


def test_create_vote_success(db_session):
    vote = Vote(
        user_id="00000000-0000-0000-0000-000000000001",
        target_type="question",
        target_id="00000000-0000-0000-0000-000000000002",
        value=1,
    )
    db_session.add(vote)
    db_session.commit()
    db_session.refresh(vote)

    assert vote.id is not None


def test_duplicate_vote_fails(db_session):
    vote1 = Vote(
        user_id="00000000-0000-0000-0000-000000000003",
        target_type="answer",
        target_id="00000000-0000-0000-0000-000000000004",
        value=1,
    )
    vote2 = Vote(
        user_id="00000000-0000-0000-0000-000000000003",
        target_type="answer",
        target_id="00000000-0000-0000-0000-000000000004",
        value=-1,
    )
    db_session.add(vote1)
    db_session.commit()

    db_session.add(vote2)
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_missing_value_fails(db_session):
    vote = Vote(
        user_id="00000000-0000-0000-0000-000000000005",
        target_type="question",
        target_id="00000000-0000-0000-0000-000000000006",
        value=None,
    )
    db_session.add(vote)
    with pytest.raises(IntegrityError):
        db_session.commit()
