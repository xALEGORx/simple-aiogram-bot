# - *- coding: utf- 8 - *-
from aiogram.types import Update

from loader import dp
from utils.logging import bot_logger
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from data.text import *
from keyboards.reply_all import menu_back


# Логирование ошибок
@dp.errors_handler()
async def main_errors(update: Update, exception):
    bot_logger.exception(
        f"Exception: {exception}\n"
        f"Data: {update}"
    )


# Не найден callback
@dp.callback_query_handler(state="*")
async def main_missed_callback(call: CallbackQuery, state: FSMContext):
    try:
        await call.message.delete()
    except:
        pass

    await call.message.answer(ERROR_TEXT,
                              reply_markup=menu_back())


# Не найдена команда
@dp.message_handler()
async def main_missed_message(message: Message):
    await message.answer(COMMAND_NOT_FOUND_TEXT)
