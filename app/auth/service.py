from sqlalchemy.orm import Session

from app.auth.models import User
from app.auth.repository import UserRepository
from app.auth.schemas import UserCreate
from app.core.security import hash_password
from app.core.security import verify_password


class AuthService:

    @staticmethod
    def register(
        db: Session,
        request: UserCreate
    ) -> User:

        existing = UserRepository.get_by_email(
            db,
            request.email
        )

        if existing:
            raise ValueError("Email already registered")

        user = User(
            full_name=request.full_name,
            email=request.email,
            hashed_password=hash_password(
                request.password
            ),
        )

        return UserRepository.create(
            db,
            user
        )

    @staticmethod
    def authenticate(
        db: Session,
        email: str,
        password: str
    ) -> User | None:

        user = UserRepository.get_by_email(
            db,
            email
        )

        if not user:
            return None

        if not verify_password(
            password,
            user.hashed_password
        ):
            return None

        return user