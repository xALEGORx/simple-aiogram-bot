# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from data.text import *
from data.config import get_admins


# Главное меню
def menu_main(userid):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(PROFILE_KEYBOARD)

    if userid in get_admins():
        keyboard.row(ADMIN_MENU_KEYBOARD)

    return keyboard

# Inline возврат к меню
def menu_back():
    keyboard = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton(BACK_BUTTON, callback_data=f"menu")
    )

    return keyboard
