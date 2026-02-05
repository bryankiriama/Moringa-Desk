from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class RelatedQuestion(Base):
    """Manual link between two questions to show related items."""

    __tablename__ = "related_questions"

    question_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), ForeignKey("questions.id"), primary_key=True
    )
    related_question_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), ForeignKey("questions.id"), primary_key=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.utcnow, nullable=False
    )
