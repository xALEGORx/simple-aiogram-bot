# - *- coding: utf- 8 - *-
from aiogram import Dispatcher

from middlewares.exists_user import ExistsUserMiddleware
from middlewares.throttling import ThrottlingMiddleware


# Подключение милдварей
def setup_middlewares(dp: Dispatcher):
    dp.middleware.setup(ExistsUserMiddleware())
    dp.middleware.setup(ThrottlingMiddleware())
