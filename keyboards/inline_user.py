# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.text import BACK_BUTTON


# Кнопки профиля
def profile_control():
    keyboard = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton(BACK_BUTTON, callback_data=f"menu")
    )

    return keyboard
