from sqlalchemy import String, Date, Float, Enum, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PGUUID

from app.core.database import Base, UUIDMixin, TimestampMixin
from app.models.enums import SpeciesEnum, GenderEnum, ActivityLevelEnum

class Pet(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "pets"

    owner_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    species: Mapped[SpeciesEnum] = mapped_column(Enum(SpeciesEnum), nullable=False)
    breed: Mapped[str | None] = mapped_column(String(255), nullable=True)
    gender: Mapped[GenderEnum] = mapped_column(Enum(GenderEnum), nullable=False)
    date_of_birth: Mapped[Date | None] = mapped_column(Date, nullable=True)
    weight: Mapped[float | None] = mapped_column(Float, nullable=True) # in kg
    activity_level: Mapped[ActivityLevelEnum | None] = mapped_column(Enum(ActivityLevelEnum), nullable=True)
    allergies: Mapped[str | None] = mapped_column(Text, nullable=True)
    existing_conditions: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Relationships
    owner: Mapped["User"] = relationship("User", back_populates="pets")
    
    health_records: Mapped[list["HealthRecord"]] = relationship("HealthRecord", back_populates="pet", cascade="all, delete-orphan")
    activity_records: Mapped[list["ActivityRecord"]] = relationship("ActivityRecord", back_populates="pet", cascade="all, delete-orphan")
    nutrition_records: Mapped[list["NutritionRecord"]] = relationship("NutritionRecord", back_populates="pet", cascade="all, delete-orphan")
    hydration_records: Mapped[list["HydrationRecord"]] = relationship("HydrationRecord", back_populates="pet", cascade="all, delete-orphan")
    sleep_records: Mapped[list["SleepRecord"]] = relationship("SleepRecord", back_populates="pet", cascade="all, delete-orphan")
    symptoms: Mapped[list["Symptom"]] = relationship("Symptom", back_populates="pet", cascade="all, delete-orphan")
    medications: Mapped[list["Medication"]] = relationship("Medication", back_populates="pet", cascade="all, delete-orphan")
    vaccinations: Mapped[list["Vaccination"]] = relationship("Vaccination", back_populates="pet", cascade="all, delete-orphan")
    vet_visits: Mapped[list["VetVisit"]] = relationship("VetVisit", back_populates="pet", cascade="all, delete-orphan")
    health_baselines: Mapped[list["HealthBaseline"]] = relationship("HealthBaseline", back_populates="pet", cascade="all, delete-orphan")
    health_scores: Mapped[list["HealthScore"]] = relationship("HealthScore", back_populates="pet", cascade="all, delete-orphan")
    anomalies: Mapped[list["Anomaly"]] = relationship("Anomaly", back_populates="pet", cascade="all, delete-orphan")
    ai_assessments: Mapped[list["AIAssessment"]] = relationship("AIAssessment", back_populates="pet", cascade="all, delete-orphan")
    care_tasks: Mapped[list["CareTask"]] = relationship("CareTask", back_populates="pet", cascade="all, delete-orphan")
    images: Mapped[list["PetImage"]] = relationship("PetImage", back_populates="pet", cascade="all, delete-orphan")
    ai_conversations: Mapped[list["AIConversation"]] = relationship("AIConversation", back_populates="pet", cascade="all, delete-orphan")
    health_reports: Mapped[list["HealthReport"]] = relationship("HealthReport", back_populates="pet", cascade="all, delete-orphan")
