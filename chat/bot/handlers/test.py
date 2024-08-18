from aiogram.types import KeyboardButton, KeyboardButtonPollType, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class PollHandlers:
    async def cmd_start(message: Message):
        builder = ReplyKeyboardBuilder()
        builder.row(
            KeyboardButton(
                text="Пройти тест", request_poll=KeyboardButtonPollType(type="quiz")
            )
        )

        await message.answer(
            "Выберите действие:",
            reply_markup=builder.as_markup(resize_keyboard=True),
        )
