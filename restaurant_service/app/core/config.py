from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    DELIVERY_SERVICE_URL: str = "http://delivery_service:8000"
    USER_SERVICE_URL: str = "http://user_service:8001"

    model_config = {
        "env_file": ".env"
    }

settings = Settings()
