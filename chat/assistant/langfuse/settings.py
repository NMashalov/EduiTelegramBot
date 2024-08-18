from pydantic_settings import BaseSettings, SettingsConfigDict


class LangFuseSettings(BaseSettings):
    secret_key: str
    public_key: str
    host: str

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="LANGFUSE_", extra="ignore"
    )
