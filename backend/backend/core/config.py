from typing import List

from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    BACKEND_CORS_ORIGINS: List[str] = []
    MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"


settings = Settings()
