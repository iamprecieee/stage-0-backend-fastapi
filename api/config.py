from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import EmailStr
from functools import lru_cache
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

class Settings(BaseSettings):
    debug_value: str
    allowed_hosts: str
    csrf_trusted_origins: str
    email_value: EmailStr
    github_url: str


@lru_cache
def get_settings():
    return Settings()