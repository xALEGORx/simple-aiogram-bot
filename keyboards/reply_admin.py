# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup
from data.text import *


# Админ меню
def admin_main():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(ADMIN_FIND_KEYBOARD)
    keyboard.row(ADMIN_RESTART_KEYBOARD)
    return keyboard