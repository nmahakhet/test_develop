from pydantic import BaseSettings

class Settings(BaseSettings):
    API_PATH_STR: str
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    class Config:
        env_file = "./app/.env"

settings = Settings()