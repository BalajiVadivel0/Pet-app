import enum

class SpeciesEnum(str, enum.Enum):
    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"
    REPTILE = "reptile"
    OTHER = "other"

class GenderEnum(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"

class ActivityLevelEnum(str, enum.Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    VERY_HIGH = "very_high"

class ActivityIntensityEnum(str, enum.Enum):
    LIGHT = "light"
    MODERATE = "moderate"
    VIGOROUS = "vigorous"

class SymptomSeverityEnum(str, enum.Enum):
    MILD = "mild"
    MODERATE = "moderate"
    SEVERE = "severe"

class BaselineStatusEnum(str, enum.Enum):
    INITIAL = "initial"
    EMERGING = "emerging"
    ESTABLISHED = "established"

class AnomalySeverityEnum(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class AIAssessmentTypeEnum(str, enum.Enum):
    SYMPTOM_ANALYSIS = "symptom_analysis"
    HEALTH_SUMMARY = "health_summary"
    ANOMALY_EXPLANATION = "anomaly_explanation"
    IMAGE_ANALYSIS = "image_analysis"
    WEEKLY_SUMMARY = "weekly_summary"

class MessageRoleEnum(str, enum.Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

class CareTaskCategoryEnum(str, enum.Enum):
    VACCINATION = "vaccination"
    MEDICATION = "medication"
    GROOMING = "grooming"
    FEEDING = "feeding"
    EXERCISE = "exercise"
    VET_VISIT = "vet_visit"
    CUSTOM = "custom"

class CareTaskStatusEnum(str, enum.Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    MISSED = "missed"

class NotificationPriorityEnum(str, enum.Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    URGENT = "urgent"
