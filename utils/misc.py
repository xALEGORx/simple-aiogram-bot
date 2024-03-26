# - *- coding: utf- 8 - *-
from aiogram import Dispatcher

from data.config import get_admins
from data.text import *
from loader import bot
from services.database import get_user


async def on_startup_notify(dp: Dispatcher):
    await send_admins(START_ADMIN_TEXT)


async def send_admins(message):
    for admin in get_admins():
        try:
            await bot.send_message(admin, message, disable_web_page_preview=True)
        except:
            pass


def open_profile(user_id):
    user = get_user(user_id=user_id)

    return PROFILE_TEXT.format(user_id=user_id, balance=user['balance'])
