from typing import Any
from uuid import UUID

from langfuse.callback import CallbackHandler

from chat.assistant.langfuse.settings import LangFuseSettings


class LangFuseClient:
    def __init__(self, settings: LangFuseSettings):
        self.settings = settings

    def langfuse_callback(
        self, session_id: UUID | str, trace_metadata: dict[str, Any] | None = None
    ):
        return CallbackHandler
