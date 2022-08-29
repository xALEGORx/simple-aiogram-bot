# - *- coding: utf- 8 - *-
from aiogram import executor, Dispatcher

from handlers import dp
from middlewares import setup_middlewares
from utils.commands import set_commands
from utils.logging import bot_logger
from utils.misc import on_startup_notify


async def on_startup(dp: Dispatcher):
    await dp.bot.delete_webhook()
    await dp.bot.get_updates(offset=-1)

    await set_commands(dp)
    await on_startup_notify(dp)

    bot_logger.warning("BOT WAS STARTED")


async def on_shutdown(dp: Dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == "__main__":
    setup_middlewares(dp)
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
