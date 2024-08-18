from pydantic_settings import BaseSettings, SettingsConfigDict


class AssistantSettings(BaseSettings):
    llm_model_name: str = "gpt-4o"
    temperature: float = 0
    api_token: str

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="LLM_", extra="ignore"
    )
