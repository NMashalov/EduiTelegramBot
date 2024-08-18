from aiogram.types import Message


class RegistrationHandlers:
    async def name(message: Message):
        await message.answer(
            "Имя",
        )

    async def surname(message: Message):
        await message.answer(
            "Фамилия",
        )
