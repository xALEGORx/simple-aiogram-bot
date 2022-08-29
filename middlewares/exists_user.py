# - *- coding: utf- 8 - *-
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Update

from data.config import get_admins
from services.database import get_user, add_user, update_user, get_settings


class ExistsUserMiddleware(BaseMiddleware):
    def __init__(self):
        self.prefix = "key_prefix"
        super(ExistsUserMiddleware, self).__init__()

    async def on_process_update(self, update: Update, data: dict):
        if "message" in update:
            this_user = update.message.from_user
        elif "callback_query" in update:
            this_user = update.callback_query.from_user
        else:
            this_user = None

        if this_user is not None:
            settings = get_settings()

            if settings['status_work'] == 1 or this_user.id in get_admins():
                if not this_user.is_bot:
                    user = get_user(userid=this_user.id)

                    userid = this_user.id
                    username = this_user.username
                    fullname = this_user.full_name

                    if username is None: username = ""

                    if user is None:
                        add_user(userid, username, fullname)
                    elif username != user['username'] or fullname != user['fullname']:
                        update_user(user['userid'], username=username, fullname=fullname)
