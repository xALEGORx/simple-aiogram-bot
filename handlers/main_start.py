# - *- coding: utf- 8 - *-
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from loader import dp
from utils.filters import IsWork
from data.text import *
from keyboards.reply_all import menu_main


# Проверка на тех. работы
@dp.message_handler(IsWork(), state="*")
async def filter_work_message(message: Message, state: FSMContext):
    await state.finish()

    await message.answer(WORK_TEXT)


# Проверка на тех. работы
@dp.callback_query_handler(IsWork(), state="*")
async def filter_work_callback(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.answer(WORK_TEXT, True)


##################################
#  _______ ________   _________  #
# |__   __|  ____\ \ / /__   __| #
#    | |  | |__   \ V /   | |    #
#    | |  |  __|   > <    | |    #
#    | |  | |____ / . \   | |    #
#    |_|  |______/_/ \_\  |_|    #
##################################
# Команда /start
@dp.message_handler(text="/start", state="*")
async def start_command(message: Message, state: FSMContext):
    await state.finish()

    await message.answer(MENU_TEXT,
                         reply_markup=menu_main(message.from_user.id))


###################################
#   _____          _      _       #
#  / ____|   /\   | |    | |      #
# | |       /  \  | |    | |      #
# | |      / /\ \ | |    | |      #
# | |____ / ____ \| |____| |____  #
#  \_____/_/    \_\______|______| #
###################################
# Вызов меню через кнопку
@dp.callback_query_handler(text="menu", state="*")
async def menu_return(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(MENU_TEXT)
