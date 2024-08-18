from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    bot_token: str
    admin_ids: str

    model_config = SettingsConfigDict(env_file=".env", env_prefix="TG_", extra="ignore")
