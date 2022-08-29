# - *- coding: utf- 8 - *-
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from loader import dp
from utils.filters import IsAdmin
from data.text import *
from keyboards.reply_admin import admin_main
from keyboards.inline_admin import restart_confirm


##################################
#  _______ ________   _________  #
# |__   __|  ____\ \ / /__   __| #
#    | |  | |__   \ V /   | |    #
#    | |  |  __|   > <    | |    #
#    | |  | |____ / . \   | |    #
#    |_|  |______/_/ \_\  |_|    #
##################################
# Вызов меню
@dp.message_handler(IsAdmin(), text=ADMIN_MENU_KEYBOARD, state="*")
async def admin_menu(message: Message, state: FSMContext):
    await state.finish()

    await message.answer(ADMIN_INFORMATION_TEXT,
                         reply_markup=admin_main())

# Перезагрузка бота
@dp.message_handler(IsAdmin(), text=ADMIN_RESTART_KEYBOARD, state="*")
async def admin_restart(message: Message, state: FSMContext):
    await state.finish()

    await message.answer(ADMIN_RESTART_CONFIRM_TEXT,
                         reply_markup=restart_confirm())
