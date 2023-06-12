from pydantic import BaseSettings, PostgresDsn
from pathlib import Path, PurePath


class Config(BaseSettings):
    DATABASE_URL: PostgresDsn = "postgresql://postgres:postgres@postgres:5432/"
    SITE_DOMAIN: str = "localhost"
    SITE_PORT: str = "8000"
    DEBUG: bool = True
    APP_VERSION: str = "1"
    BASE_DIR: PurePath = Path(__file__).resolve().parent.parent


settings = Config()
