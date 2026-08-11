from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.repositories.user import user_repo
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import verify_password, create_access_token

class AuthService:
    async def authenticate(self, db: AsyncSession, *, email: str, password: str) -> Optional[User]:
        user = await user_repo.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.password_hash):
            return None
        return user

    async def register(self, db: AsyncSession, *, user_in: UserCreate) -> User:
        user = await user_repo.get_by_email(db, email=user_in.email)
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The user with this email already exists in the system.",
            )
        user = await user_repo.create(db, obj_in=user_in)
        return user

auth_service = AuthService()
