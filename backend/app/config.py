from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GRAFANA_URL: str
    GRAFANA_SERVICE_ACCOUNT_TOKEN: str
    SERVER_PORT: int = 8000

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
