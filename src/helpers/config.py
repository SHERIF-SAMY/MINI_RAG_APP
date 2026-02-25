from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    
    APP_NAME: str
    APP_VERSION: str
    APP_ENV: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int
    
    model_config = SettingsConfigDict(env_file=".env")
    
    # class config:
    #     env_file = ".env"

def get_settings():
    return Settings()
