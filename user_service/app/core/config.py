from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    RESTAURANT_SERVICE_URL: str = "http://restaurant_service:8000"
    DELIVERY_SERVICE_URL: str = "http://delivery_service:8000"

    class Config:
        env_file = ".env"

settings = Settings()
