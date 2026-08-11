from sqlalchemy import String, Enum, Text, ForeignKey, DateTime, Integer, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PGUUID, JSONB
from datetime import datetime

from app.core.database import Base, UUIDMixin, TimestampMixin
from app.models.enums import (
    AIAssessmentTypeEnum, 
    MessageRoleEnum, 
    CareTaskCategoryEnum, 
    CareTaskStatusEnum, 
    NotificationPriorityEnum
)

class AIAssessment(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "ai_assessments"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), index=True, nullable=False)
    assessment_type: Mapped[AIAssessmentTypeEnum] = mapped_column(Enum(AIAssessmentTypeEnum), nullable=False)
    input_context: Mapped[dict] = mapped_column(JSONB, nullable=False)
    output_summary: Mapped[str] = mapped_column(Text, nullable=False)
    care_priority: Mapped[str | None] = mapped_column(String(100), nullable=True)
    model_provider: Mapped[str] = mapped_column(String(100), nullable=False)
    model_name: Mapped[str] = mapped_column(String(100), nullable=False)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="ai_assessments")


class AIConversation(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "ai_conversations"

    user_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    pet_id: Mapped[str | None] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), index=True, nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="ai_conversations")
    pet: Mapped["Pet"] = relationship("Pet", back_populates="ai_conversations")
    messages: Mapped[list["AIMessage"]] = relationship("AIMessage", back_populates="conversation", cascade="all, delete-orphan")


class AIMessage(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "ai_messages"

    conversation_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("ai_conversations.id", ondelete="CASCADE"), index=True, nullable=False)
    role: Mapped[MessageRoleEnum] = mapped_column(Enum(MessageRoleEnum), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    conversation: Mapped["AIConversation"] = relationship("AIConversation", back_populates="messages")


class CareTask(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "care_tasks"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[CareTaskCategoryEnum] = mapped_column(Enum(CareTaskCategoryEnum), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    scheduled_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    recurrence_rule: Mapped[str | None] = mapped_column(String(255), nullable=True)
    priority: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[CareTaskStatusEnum] = mapped_column(Enum(CareTaskStatusEnum), nullable=False)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="care_tasks")

    __table_args__ = (
        Index("ix_care_tasks_pet_id_scheduled_at", "pet_id", "scheduled_at"),
    )


class Notification(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "notifications"

    user_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    pet_id: Mapped[str | None] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), index=True, nullable=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    type: Mapped[str] = mapped_column(String(100), nullable=False)
    priority: Mapped[NotificationPriorityEnum] = mapped_column(Enum(NotificationPriorityEnum), nullable=False)
    scheduled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    sent_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    read_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="notifications")

    __table_args__ = (
        Index("ix_notifications_user_id_read_at", "user_id", "read_at"),
    )
