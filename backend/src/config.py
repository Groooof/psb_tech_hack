from pydantic import BaseSettings


class Env(BaseSettings):
    """
    Переменные окружения.
    """
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


env = Env()
