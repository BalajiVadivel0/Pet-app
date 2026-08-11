from sqlalchemy import String, Float, Enum, ForeignKey, DateTime, Integer, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PGUUID, JSONB
from datetime import datetime

from app.core.database import Base, UUIDMixin, TimestampMixin
from app.models.enums import BaselineStatusEnum, AnomalySeverityEnum

class HealthBaseline(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "health_baselines"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), nullable=False)
    metric_type: Mapped[str] = mapped_column(String(100), nullable=False)
    baseline_value: Mapped[float] = mapped_column(Float, nullable=False)
    unit: Mapped[str] = mapped_column(String(50), nullable=False)
    calculation_window_days: Mapped[int] = mapped_column(Integer, nullable=False)
    sample_count: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[BaselineStatusEnum] = mapped_column(Enum(BaselineStatusEnum), nullable=False)
    calculated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="health_baselines")

    __table_args__ = (
        Index("ix_health_baselines_pet_id_metric_type", "pet_id", "metric_type"),
    )


class HealthScore(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "health_scores"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), nullable=False)
    score: Mapped[float] = mapped_column(Float, nullable=False)
    activity_score: Mapped[float] = mapped_column(Float, nullable=False)
    nutrition_score: Mapped[float] = mapped_column(Float, nullable=False)
    hydration_score: Mapped[float] = mapped_column(Float, nullable=False)
    sleep_score: Mapped[float] = mapped_column(Float, nullable=False)
    medical_compliance_score: Mapped[float] = mapped_column(Float, nullable=False)
    behavioral_score: Mapped[float] = mapped_column(Float, nullable=False)
    calculated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="health_scores")

    __table_args__ = (
        Index("ix_health_scores_pet_id_calculated_at", "pet_id", "calculated_at"),
    )


class Anomaly(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "anomalies"

    pet_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("pets.id", ondelete="CASCADE"), nullable=False)
    metric_type: Mapped[str] = mapped_column(String(100), nullable=False)
    baseline_value: Mapped[float | None] = mapped_column(Float, nullable=True)
    observed_value: Mapped[float | None] = mapped_column(Float, nullable=True)
    deviation_percentage: Mapped[float | None] = mapped_column(Float, nullable=True)
    severity: Mapped[AnomalySeverityEnum] = mapped_column(Enum(AnomalySeverityEnum), nullable=False)
    detection_method: Mapped[str] = mapped_column(String(100), nullable=False)
    detected_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    metadata_json: Mapped[dict | None] = mapped_column(JSONB, nullable=True)

    pet: Mapped["Pet"] = relationship("Pet", back_populates="anomalies")
    signals: Mapped[list["AnomalySignal"]] = relationship("AnomalySignal", back_populates="anomaly", cascade="all, delete-orphan")

    __table_args__ = (
        Index("ix_anomalies_pet_id_detected_at", "pet_id", "detected_at"),
    )


class AnomalySignal(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "anomaly_signals"

    anomaly_id: Mapped[str] = mapped_column(PGUUID(as_uuid=True), ForeignKey("anomalies.id", ondelete="CASCADE"), index=True, nullable=False)
    metric_type: Mapped[str] = mapped_column(String(100), nullable=False)
    baseline_value: Mapped[float | None] = mapped_column(Float, nullable=True)
    observed_value: Mapped[float | None] = mapped_column(Float, nullable=True)
    deviation_percentage: Mapped[float | None] = mapped_column(Float, nullable=True)
    contribution_score: Mapped[float | None] = mapped_column(Float, nullable=True)

    anomaly: Mapped["Anomaly"] = relationship("Anomaly", back_populates="signals")
