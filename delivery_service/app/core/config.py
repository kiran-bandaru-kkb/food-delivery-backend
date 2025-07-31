from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    DELIVERY_SERVICE_URL: str = "http://delivery_service:8000"
    class Config:
        env_file = ".env"

settings = Settings()
