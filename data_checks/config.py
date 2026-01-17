from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    csv_path: str = "data/users.csv"
    report_path: str = "reports/latest.json"

    model_config = SettingsConfigDict(
        env_prefix="DATA_CHECKS_",
        env_file=".env",
        extra="ignore",
    )
