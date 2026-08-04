from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "PulseFlow"

    APP_VERSION: str = "1.0.0"

    DEBUG: bool = True

    DATABASE_URL: str

    SECRET_KEY: str

    JWT_ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()