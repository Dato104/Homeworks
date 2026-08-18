from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    DEBUG: str
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_LIFETIME_MINUTES: int
    REFRESH_TOKEN_LIFETIME_DAYS: int
    ALGORITHM: str

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

settings = Settings()














