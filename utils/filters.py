# - *- coding: utf- 8 - *-
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import get_admins
from services.database import get_settings


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        if message.from_user.id in get_admins():
            return True
        else:
            return False


class IsWork(BoundFilter):
    async def check(self, message: types.Message):
        settings = get_settings()

        if settings['status_work'] == 1 or message.from_user.id in get_admins():
            return False
        else:
            return True
