# - *- coding: utf- 8 - *-
from datetime import datetime
import asyncio
from utils.logging import bot_logger


def get_date(format_date="%d.%m.%Y %H:%M:%S", timestamp=0):
    if timestamp:
        date = datetime.fromtimestamp(timestamp)
    else:
        date = datetime.today().replace(microsecond=0)

    return date.strftime(format_date)


async def restart_bot(user_id):
    import sys
    import os
    await asyncio.sleep(1)

    bot_logger.critical(f'BOT WAS RESTARTED BY ADMIN {user_id}')
    os.execv(sys.executable, ['python'] + sys.argv)
