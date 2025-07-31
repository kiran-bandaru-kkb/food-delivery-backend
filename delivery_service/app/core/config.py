from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    USER_SERVICE_URL: str = "http://user_service:8001"
    RESTAURANT_SERVICE_URL: str = "http://restaurant_service:8002"

    class Config:
        env_file = ".env"

settings = Settings()
