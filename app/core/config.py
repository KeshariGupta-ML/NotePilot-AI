import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


# Load .env file
load_dotenv()


class Settings(BaseSettings):

    APP_NAME: str = "NotePilot AI"

    SECRET_KEY: str = os.getenv(
        "SECRET_KEY",
        "default-secret-key"
    )

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./users.db"
    )

    GEMINI_API_KEY: str = os.getenv(
        "GEMINI_API_KEY",
        ""
    )


settings = Settings()