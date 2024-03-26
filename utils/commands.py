# - *- coding: utf- 8 - *-
from aiogram import Dispatcher
from aiogram.types import BotCommand
from data.text import START_COMMAND


async def set_commands(dp: Dispatcher):
    commands = [
        BotCommand("start", START_COMMAND)
    ]
    
    await dp.bot.set_my_commands(commands)
