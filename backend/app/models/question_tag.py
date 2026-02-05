from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class QuestionTag(Base):
    """Join table for the many-to-many relationship between questions and tags."""

    __tablename__ = "question_tags"

    question_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), ForeignKey("questions.id"), primary_key=True
    )
    tag_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), ForeignKey("tags.id"), primary_key=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.utcnow, nullable=False
    )
