from datetime import datetime, timedelta, timezone
from typing import Any

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(password: str) -> str:
    """
    Hash a plain text password.
    bcrypt supports maximum 72 bytes.
    """

    password_bytes = password.encode("utf-8")

    if len(password_bytes) > 72:
        password = password_bytes[:72].decode(
            "utf-8",
            errors="ignore"
        )

    return pwd_context.hash(password)


def verify_password(
        plain_password: str,
        hashed_password: str,
) -> bool:
    """
    Verify a plain password against its hash.
    """

    password_bytes = plain_password.encode("utf-8")

    if len(password_bytes) > 72:
        plain_password = password_bytes[:72].decode(
            "utf-8",
            errors="ignore"
        )

    return pwd_context.verify(
        plain_password,
        hashed_password,
    )


def create_access_token(
        data: dict[str, Any],
        expires_delta: timedelta | None = None,
) -> str:
    """
    Create a signed JWT access token.
    """

    payload = data.copy()

    expire = (
            datetime.now(timezone.utc)
            + (
                expires_delta
                if expires_delta
                else timedelta(
                    minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
                )
            )
    )

    payload.update({"exp": expire})

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def decode_access_token(token: str) -> dict[str, Any]:
    """
    Decode and validate a JWT access token.
    Raises JWTError if the token is invalid or expired.
    """

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
        return payload

    except JWTError:
        raise
