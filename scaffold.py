import os

structure = {
    "android/app/src/main/java/com/pawcare/ai/core/common": {},
    "android/app/src/main/java/com/pawcare/ai/core/constants": {},
    "android/app/src/main/java/com/pawcare/ai/core/designsystem/color": {},
    "android/app/src/main/java/com/pawcare/ai/core/designsystem/typography": {},
    "android/app/src/main/java/com/pawcare/ai/core/designsystem/theme": {},
    "android/app/src/main/java/com/pawcare/ai/core/designsystem/shapes": {},
    "android/app/src/main/java/com/pawcare/ai/core/designsystem/components": {},
    "android/app/src/main/java/com/pawcare/ai/core/designsystem/icons": {},
    "android/app/src/main/java/com/pawcare/ai/core/navigation": {},
    "android/app/src/main/java/com/pawcare/ai/core/network": {
        "ApiConfig.kt": "package com.pawcare.ai.core.network\n",
        "NetworkResult.kt": "package com.pawcare.ai.core.network\n",
        "NetworkError.kt": "package com.pawcare.ai.core.network\n",
        "NetworkModule.kt": "package com.pawcare.ai.core.network\n"
    },
    "android/app/src/main/java/com/pawcare/ai/core/datastore": {},
    "android/app/src/main/java/com/pawcare/ai/core/database/converters": {},
    "android/app/src/main/java/com/pawcare/ai/core/database": {
        "PawCareDatabase.kt": "package com.pawcare.ai.core.database\n",
        "DatabaseModule.kt": "package com.pawcare.ai.core.database\n"
    },
    "android/app/src/main/java/com/pawcare/ai/core/camera": {},
    "android/app/src/main/java/com/pawcare/ai/core/notifications": {},
    "android/app/src/main/java/com/pawcare/ai/core/utils": {},
    "android/app/src/main/java/com/pawcare/ai/data/local/dao": {},
    "android/app/src/main/java/com/pawcare/ai/data/local/database": {},
    "android/app/src/main/java/com/pawcare/ai/data/local/entity": {},
    "android/app/src/main/java/com/pawcare/ai/data/remote/api": {},
    "android/app/src/main/java/com/pawcare/ai/data/remote/dto": {},
    "android/app/src/main/java/com/pawcare/ai/data/remote/interceptor": {},
    "android/app/src/main/java/com/pawcare/ai/data/repository": {},
    "android/app/src/main/java/com/pawcare/ai/domain/model": {},
    "android/app/src/main/java/com/pawcare/ai/domain/repository": {},
    "android/app/src/main/java/com/pawcare/ai/domain/usecase/auth": {},
    "android/app/src/main/java/com/pawcare/ai/domain/usecase/pet": {},
    "android/app/src/main/java/com/pawcare/ai/domain/usecase/health": {},
    "android/app/src/main/java/com/pawcare/ai/domain/usecase/activity": {},
    "android/app/src/main/java/com/pawcare/ai/domain/usecase/nutrition": {},
    "android/app/src/main/java/com/pawcare/ai/domain/usecase/hydration": {},
    "android/app/src/main/java/com/pawcare/ai/domain/usecase/sleep": {},
    "android/app/src/main/java/com/pawcare/ai/domain/usecase/symptom": {},
    "android/app/src/main/java/com/pawcare/ai/domain/usecase/ai": {},
    "android/app/src/main/java/com/pawcare/ai/domain/usecase/care": {},
    "android/app/src/main/java/com/pawcare/ai/domain/usecase/report": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/auth/login": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/auth/register": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/auth/forgotpassword": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/onboarding": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/home": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/health/overview": {
        "HealthOverviewScreen.kt": "package com.pawcare.ai.presentation.health.overview\n",
        "HealthOverviewViewModel.kt": "package com.pawcare.ai.presentation.health.overview\n",
        "HealthOverviewUiState.kt": "package com.pawcare.ai.presentation.health.overview\n",
        "components": {}
    },
    "android/app/src/main/java/com/pawcare/ai/presentation/health/activity": {
        "ActivityScreen.kt": "package com.pawcare.ai.presentation.health.activity\n",
        "ActivityViewModel.kt": "package com.pawcare.ai.presentation.health.activity\n",
        "ActivityUiState.kt": "package com.pawcare.ai.presentation.health.activity\n",
        "components": {}
    },
    "android/app/src/main/java/com/pawcare/ai/presentation/health/nutrition": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/health/hydration": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/health/sleep": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/health/weight": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/health/symptoms": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/health/timeline": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/ai/assistant": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/ai/symptomanalysis": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/ai/visionscanner": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/care/overview": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/care/vaccinations": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/care/medications": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/care/grooming": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/care/appointments": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/reports": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/profile": {},
    "android/app/src/main/java/com/pawcare/ai/presentation/components": {},
    "android/app/src/main": {
        "AndroidManifest.xml": "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<manifest xmlns:android=\"http://schemas.android.com/apk/res/android\"\n    package=\"com.pawcare.ai\">\n    <application\n        android:allowBackup=\"true\"\n        android:icon=\"@mipmap/ic_launcher\"\n        android:label=\"@string/app_name\"\n        android:roundIcon=\"@mipmap/ic_launcher_round\"\n        android:supportsRtl=\"true\"\n        android:theme=\"@style/Theme.PawCareAI\">\n        <activity\n            android:name=\".MainActivity\"\n            android:exported=\"true\"\n            android:theme=\"@style/Theme.PawCareAI\">\n            <intent-filter>\n                <action android:name=\"android.intent.action.MAIN\" />\n                <category android:name=\"android.intent.category.LAUNCHER\" />\n            </intent-filter>\n        </activity>\n    </application>\n</manifest>\n"
    },
    "android/app/src/test": {},
    "android/gradle": {},
    "backend/app/core": {
        "config.py": "",
        "database.py": "",
        "security.py": "",
        "logging.py": "",
        "exceptions.py": ""
    },
    "backend/app/api/v1": {
        "router.py": "",
        "auth.py": "",
        "users.py": "",
        "pets.py": "",
        "health.py": "",
        "activity.py": "",
        "nutrition.py": "",
        "hydration.py": "",
        "sleep.py": "",
        "symptoms.py": "",
        "ai.py": "",
        "care.py": "",
        "analytics.py": "",
        "reports.py": ""
    },
    "backend/app/models": {},
    "backend/app/schemas": {},
    "backend/app/repositories": {},
    "backend/app/services/auth": {},
    "backend/app/services/users": {},
    "backend/app/services/pets": {},
    "backend/app/services/health": {},
    "backend/app/services/activity": {},
    "backend/app/services/nutrition": {},
    "backend/app/services/hydration": {},
    "backend/app/services/sleep": {},
    "backend/app/services/symptoms": {},
    "backend/app/services/care": {},
    "backend/app/services/analytics": {},
    "backend/app/services/ai": {},
    "backend/app/services/vision": {},
    "backend/app/services/notifications": {},
    "backend/app/services/reports": {},
    "backend/app/intelligence/baseline": {},
    "backend/app/intelligence/anomaly": {},
    "backend/app/intelligence/scoring": {},
    "backend/app/intelligence/feature_engineering": {},
    "backend/app/intelligence/risk": {},
    "backend/app/integrations/gemini": {},
    "backend/app/integrations/storage": {},
    "backend/app/integrations/fcm": {},
    "backend/app/utils": {},
    "backend/app": {
        "main.py": "from fastapi import FastAPI\n\napp = FastAPI(title=\"PawCare AI API\")\n\n@app.get(\"/\")\ndef read_root():\n    return {\"status\": \"ok\", \"message\": \"PawCare AI Backend\"}\n"
    },
    "backend/tests/unit": {},
    "backend/tests/integration": {},
    "backend/tests/api": {},
    "backend/alembic/versions": {},
    "docs/architecture": {},
    "docs/api": {},
    "docs/database": {},
    "docs/ai": {},
    "docs/ui-ux": {},
    "docs/testing": {},
    "docs/deployment": {},
    "docs/diagrams": {},
    "scripts": {}
}

root_files = {
    ".gitignore": '''# Environment variables
.env
# Secrets
secrets/
# Build outputs
build/
bin/
out/
# IDE
.idea/
.vscode/
*.iml
# Python cache
__pycache__/
*.pyc
*.pyo
.pytest_cache/
# Android
local.properties
.gradle/
# Database
*.sqlite3
*.db
# Logs
logs/
*.log
# Generated
generated/
''',
    "README.md": '''# PawCare AI – Smart Pet Health, Lifestyle & Care Management Platform

## Project Overview
PawCare AI is a comprehensive, AI-driven application designed to monitor and manage pet health, nutrition, activity, and care schedules.

## Technology Stack
- **Mobile**: Android, Kotlin, Jetpack Compose, Material 3, Clean Architecture
- **Backend**: Python, FastAPI, SQLAlchemy, PostgreSQL, Redis
- **AI/ML**: Health Intelligence Engine, Gemini API
- **Infrastructure**: Docker Compose

## Repository Structure
- `/android` - Android application source code
- `/backend` - FastAPI backend application
- `/docs` - Project documentation
- `/scripts` - Utility scripts

## How to Run the Project
(To be added)

## Development Phases
- **Phase 1**: Project Setup and Architecture Skeleton (Current)
- **Phase 2**: Database schema + ER diagram + backend foundation
- **Phase 3**: Core backend APIs
- **Phase 4**: Android App foundation
''',
    "docker-compose.yml": '''version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-pawcare_user}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-pawcare_pass}
      POSTGRES_DB: ${POSTGRES_DB:-pawcare_db}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://${POSTGRES_USER:-pawcare_user}:${POSTGRES_PASSWORD:-pawcare_pass}@postgres:5432/${POSTGRES_DB:-pawcare_db}
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - postgres
      - redis
    volumes:
      - ./backend:/app

volumes:
  postgres_data:
  redis_data:
''',
    ".env.example": '''# PostgreSQL Database
POSTGRES_DB=pawcare_db
POSTGRES_USER=pawcare_user
POSTGRES_PASSWORD=pawcare_password
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# Redis
REDIS_HOST=redis
REDIS_PORT=6379

# JWT
JWT_SECRET=your_jwt_secret_key_here

# External APIs
GEMINI_API_KEY=your_gemini_api_key_here

# Storage
STORAGE_CREDENTIALS=your_storage_credentials_here
'''
}

backend_files = {
    "requirements.txt": "fastapi\nuvicorn\nsqlalchemy\nalembic\npsycopg2-binary\npydantic\npython-jose[cryptography]\npasslib[bcrypt]\nredis\npytest\nhttpx\n",
    "Dockerfile": '''FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
''',
    ".env.example": "# Backend specific env"
}

android_files = {
    "build.gradle.kts": '''// Top-level build file where you can add configuration options common to all sub-projects/modules.
plugins {
    id("com.android.application") version "8.2.0" apply false
    id("org.jetbrains.kotlin.android") version "1.9.20" apply false
}
''',
    "settings.gradle.kts": '''pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
rootProject.name = "PawCareAI"
include(":app")
''',
    "gradle.properties": '''# Project-wide Gradle settings.
org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
android.useAndroidX=true
kotlin.code.style=official
''',
    "app/build.gradle.kts": '''plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.pawcare.ai"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.pawcare.ai"
        minSdk = 26
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
        vectorDrawables {
            useSupportLibrary = true
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions {
        jvmTarget = "17"
    }
    buildFeatures {
        compose = true
    }
    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.4"
    }
}

dependencies {
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.6.2")
    implementation("androidx.activity:activity-compose:1.8.1")
    implementation(platform("androidx.compose:compose-bom:2023.10.01"))
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.ui:ui-graphics")
    implementation("androidx.compose.ui:ui-tooling-preview")
    implementation("androidx.compose.material3:material3")
}
''',
    "app/src/main/java/com/pawcare/ai/MainActivity.kt": '''package com.pawcare.ai

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    Greeting("PawCare AI")
                }
            }
        }
    }
}

@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Welcome to $name!",
        modifier = modifier
    )
}
'''
}

def create_structure(base_dir, struct):
    for path, content in struct.items():
        full_path = os.path.join(base_dir, path)
        if isinstance(content, dict):
            os.makedirs(full_path, exist_ok=True)
            create_structure(full_path, content)
        else:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "w") as f:
                f.write(content)

# Create root files
for filename, content in root_files.items():
    with open(filename, "w") as f:
        f.write(content)

# Create backend files
os.makedirs("backend", exist_ok=True)
for filename, content in backend_files.items():
    full_path = os.path.join("backend", filename)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

# Create android files
os.makedirs("android", exist_ok=True)
for filename, content in android_files.items():
    full_path = os.path.join("android", filename)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

# Create main folder structure
create_structure(".", structure)

print("Scaffolding complete.")
