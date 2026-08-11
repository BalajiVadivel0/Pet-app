from sqlalchemy import String, Float, Enum, Text, ForeignKey, DateTime, Integer, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from datetime import datetime

from app.core.database import Base, UUIDMixin, TimestampMixin
from app.models.enums import ActivityIntensityEnum, SymptomSeverityEnum

class HealthRecord(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "health_records"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), index=True, nullable=False)
    record_type: Mapped[str] = mapped_column(String(100), nullable=False)
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="health_records")


class ActivityRecord(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "activity_records"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), nullable=False)
    activity_type: Mapped[str] = mapped_column(String(100), nullable=False)
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=False)
    intensity: Mapped[ActivityIntensityEnum] = mapped_column(Enum(ActivityIntensityEnum), nullable=False)
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="activity_records")

    __table_args__ = (
        Index("ix_activity_records_pet_id_recorded_at", "pet_id", "recorded_at"),
    )


class NutritionRecord(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "nutrition_records"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), nullable=False)
    meal_type: Mapped[str] = mapped_column(String(100), nullable=False)
    food_name: Mapped[str] = mapped_column(String(255), nullable=False)
    quantity: Mapped[float] = mapped_column(Float, nullable=False)
    unit: Mapped[str] = mapped_column(String(50), nullable=False)
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="nutrition_records")

    __table_args__ = (
        Index("ix_nutrition_records_pet_id_recorded_at", "pet_id", "recorded_at"),
    )


class HydrationRecord(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "hydration_records"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    unit: Mapped[str] = mapped_column(String(50), nullable=False)
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="hydration_records")

    __table_args__ = (
        Index("ix_hydration_records_pet_id_recorded_at", "pet_id", "recorded_at"),
    )


class SleepRecord(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "sleep_records"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), nullable=False)
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=False)
    quality: Mapped[str | None] = mapped_column(String(100), nullable=True)
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="sleep_records")

    __table_args__ = (
        Index("ix_sleep_records_pet_id_start_time", "pet_id", "start_time"),
    )


class Symptom(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "symptoms"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), nullable=False)
    symptom_type: Mapped[str] = mapped_column(String(255), nullable=False)
    severity: Mapped[SymptomSeverityEnum] = mapped_column(Enum(SymptomSeverityEnum), nullable=False)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    ended_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="symptoms")

    __table_args__ = (
        Index("ix_symptoms_pet_id_started_at", "pet_id", "started_at"),
    )


class Medication(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "medications"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), index=True, nullable=False)
    medication_name: Mapped[str] = mapped_column(String(255), nullable=False)
    dosage: Mapped[float] = mapped_column(Float, nullable=False)
    dosage_unit: Mapped[str] = mapped_column(String(50), nullable=False)
    frequency: Mapped[str] = mapped_column(String(100), nullable=False)
    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    end_date: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    instructions: Mapped[str | None] = mapped_column(Text, nullable=True)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="medications")


class Vaccination(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "vaccinations"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), nullable=False)
    vaccine_name: Mapped[str] = mapped_column(String(255), nullable=False)
    administered_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    next_due_date: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    veterinarian: Mapped[str | None] = mapped_column(String(255), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="vaccinations")

    __table_args__ = (
        Index("ix_vaccinations_pet_id_next_due_date", "pet_id", "next_due_date"),
    )


class VetVisit(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "vet_visits"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), index=True, nullable=False)
    veterinarian_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    clinic_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    visit_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    reason: Mapped[str] = mapped_column(String(255), nullable=False)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    diagnosis_notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="vet_visits")


class PetImage(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "pet_images"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), index=True, nullable=False)
    image_url: Mapped[str] = mapped_column(String, nullable=False)
    storage_provider: Mapped[str] = mapped_column(String(100), nullable=False)
    image_type: Mapped[str] = mapped_column(String(100), nullable=False)
    uploaded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="images")


class HealthReport(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "health_reports"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), index=True, nullable=False)
    report_type: Mapped[str] = mapped_column(String(100), nullable=False)
    period_start: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    period_end: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    file_url: Mapped[str] = mapped_column(String, nullable=False)
    generated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="health_reports")
