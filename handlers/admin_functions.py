# - *- coding: utf- 8 - *-
import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from loader import dp, bot
from services.database import *
from utils.filters import IsAdmin
from utils.misc import open_profile
from utils.other import restart_bot
from data.text import *

##################################
#  _______ ________   _________  #
# |__   __|  ____\ \ / /__   __| #
#    | |  | |__   \ V /   | |    #
#    | |  |  __|   > <    | |    #
#    | |  | |____ / . \   | |    #
#    |_|  |______/_/ \_\  |_|    #
##################################
# Прмск пользователя
@dp.message_handler(IsAdmin(), text=ADMIN_FIND_KEYBOARD, state="*")
async def admin_func_find(message: Message, state: FSMContext):
    await state.finish()

    await state.set_state("admin_wait_user")
    await message.answer(ADMIN_FIND_USER_TEXT)


###################################
#   _____          _      _       #
#  / ____|   /\   | |    | |      #
# | |       /  \  | |    | |      #
# | |      / /\ \ | |    | |      #
# | |____ / ____ \| |____| |____  #
#  \_____/_/    \_\______|______| #
###################################
# Подтверждение перезагрузки скрипта
@dp.callback_query_handler(IsAdmin(), text_startswith="restart_confirm", state="*")
async def admin_call_confirm_restart(call: CallbackQuery, state: FSMContext):
    action = call.data.split(":")[1]

    await state.finish()
    if action == "yes":
        await call.message.edit_text(ADMIN_RESTART_START_TEXT)
        asyncio.create_task(restart_bot(call.from_user.id))
    else:
        await call.message.edit_text(CANCEL_TEXT)

#############################################
#   _____ _______    _______ ______  _____  #
#  / ____|__   __|/\|__   __|  ____|/ ____| #
# | (___    | |  /  \  | |  | |__  | (___   #
#  \___ \   | | / /\ \ | |  |  __|  \___ \  #
#  ____) |  | |/ ____ \| |  | |____ ____) | #
# |_____/   |_/_/    \_\_|  |______|_____/  #
#############################################
# Поиск пользователя
@dp.message_handler(IsAdmin(), state="admin_wait_user")
async def admin_find_user(message: Message, state: FSMContext):
    data = message.text

    if data.isdigit():
        user = get_user(user_id=data)
    else:
        if data.startswith("@"):
            data = data[1:]
        user = get_user(username=data.lower())

    await state.finish()

    if user is not None:
        await message.answer(open_profile(user['user_id']))
    else:
        await message.answer(USER_NOT_FOUND_TEXT)
