import os
from typing import Literal

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DOTENV = os.path.join(os.path.dirname(__file__), os.path.pardir, ".env")


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST"]
    CORS_ORIGINS: list[str]
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    TEST_DATABASE_URL: str
    DATABASE_URL: str
    PGADMIN_DEFAULT_PASSWORD: str
    CSRF_ENABLED: bool
    PGADMIN_DEFAULT_EMAIL: str
    PGADMIN_OUT_PORT: str
    POSTGRES_OUT_PORT: str
    FASTAPI_OUT_PORT: str

    @property
    def DATABASE_URL(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            path=f"{self.POSTGRES_DB}",
        )

    model_config = SettingsConfigDict(env_file=DOTENV)


settings = Settings()
if settings.MODE == "TEST":
    engine = create_engine(
        settings.TEST_DATABASE_URL,
        echo=False,
    )
else:
    engine = create_engine(
        str(settings.DATABASE_URL),
        future=True,
        echo=False,
        pool_size=20,
        max_overflow=20,
        pool_timeout=30,
    )

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
