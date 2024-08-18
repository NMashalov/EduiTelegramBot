from functools import cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    port: 5000

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="APP_", extra="ignore"
    )


@cache
def get_app_settinigs():
    return AppSettings()
