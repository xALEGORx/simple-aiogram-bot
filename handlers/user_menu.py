# - *- coding: utf- 8 - *-
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from data.text import PROFILE_KEYBOARD

from loader import dp
from utils.misc import open_profile
from keyboards.inline_user import profile_control


##################################
#  _______ ________   _________  #
# |__   __|  ____\ \ / /__   __| #
#    | |  | |__   \ V /   | |    #
#    | |  |  __|   > <    | |    #
#    | |  | |____ / . \   | |    #
#    |_|  |______/_/ \_\  |_|    #
##################################
# Профиль пользователя
@dp.message_handler(text=PROFILE_KEYBOARD, state="*")
async def user_profile(message: Message, state: FSMContext):
    await state.finish()

    await message.answer(open_profile(message.from_user.id), reply_markup=profile_control())
