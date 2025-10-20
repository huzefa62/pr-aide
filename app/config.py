from __future__ import annotations
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
app_name: str = "pr-aide"
env: str = os.getenv("ENV", "dev")
# CACHE_BACKEND: "redis" | "memory"
cache_backend: str = os.getenv("CACHE_BACKEND", "redis")
redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")


settings = Settings()