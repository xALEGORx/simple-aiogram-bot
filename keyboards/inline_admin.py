# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Подтверджение перезагрузки бота
def restart_confirm():
    keyboard = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton("✅", callback_data=f"restart_confirm:yes"),
        InlineKeyboardButton("❌", callback_data=f"restart_confirm:no")
    )

    return keyboard
