from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, Integer, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Vote(Base):
    """Vote on a question or answer (+1 or -1) by a user."""

    __tablename__ = "votes"
    __table_args__ = (
        UniqueConstraint("user_id", "target_type", "target_id", name="uq_vote"),
    )

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[str] = mapped_column(UUID(as_uuid=True), nullable=False)
    target_type: Mapped[str] = mapped_column(String(20), nullable=False)
    target_id: Mapped[str] = mapped_column(UUID(as_uuid=True), nullable=False)
    value: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.utcnow, nullable=False
    )
