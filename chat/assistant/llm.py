from langchain_core.language_models import BaseChatModel
from langchain_core.messages import BaseMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from chat.assistant.langfuse.client import LangFuseClient
from chat.assistant.prompt import CODE_PROMPT
from chat.assistant.settings import AssistantSettings
from chat.db.db import ChatHistoryManager


class CodeAssistant:
    def __init__(
        self,
        settings: AssistantSettings,
        langfuse_client: LangFuseClient,
        chat_history_manager: ChatHistoryManager,
    ):
        self.settings = settings
        self.chain = self.prepare_assistant(self.settings)
        self.langfuse_client = langfuse_client
        self.chat_history_manager = chat_history_manager

    def prepare_llm(self):
        return ChatOpenAI(
            api_key=self.settings.api_token,
            temperature=self.settings.temperature,
            model=self.settings.llm_model_name,
        )

    def prepare_assistant(self, main_prompt: str = CODE_PROMPT):
        return (
            ChatPromptTemplate(
                input_varables=["messages"],
                messages=[
                    SystemMessage(content=main_prompt),
                    MessagesPlaceholder(variable_name="messages"),
                ],
            )
            | self.prepare_llm()
        )

    async def aresponse(self, messages: list[BaseMessage], session_id: str):
        msg = await self.chain.ainvoke(input={"messages": messages})
        async with self.chat_history_manager.create_message_history(
            session_id=session_id
        ) as history:
            history.aadd_messages(msg)
        return msg
