from aiogram.types import Message

from chat.assistant.llm import CodeAssistant


class AssistantHandlers:
    def __init__(self, assistant: CodeAssistant):
        self.assistant = assistant

    async def cmd_start(message: Message):
        pass

    async def answer_yes(message: Message):
        await message.answer(
            "Это здорово!",
        )
