# - *- coding: utf- 8 - *-
import logging
import sys

import colorlog

from data.config import PATH_LOGS

bot_logger = logging.getLogger(__name__)

file_log = logging.FileHandler(PATH_LOGS)
console_out = logging.StreamHandler()

format_message = colorlog.ColoredFormatter(
    "%(log_color)s[%(asctime)s | %(levelname)s]%(reset)s%(blue)s: %(name)s.%(funcName)s:%(lineno)d - %(white)s%(message)s",
    datefmt="%d.%m.%Y %H:%M:%S",
    reset=True,
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'red,bg_white'
    }
)

console_out.setFormatter(format_message)

logging.basicConfig(handlers=(file_log, console_out),
                    format='[%(asctime)s | %(levelname)s]: %(message)s',
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.NOTSET)

def error_handler(type, value, tb):
    print(tb.tb_lasti)
    print(tb.tb_frame)
    bot_logger.critical(f"Exception '{type.__name__}': {value}. File: '{tb.tb_frame.f_code.co_filename}'. Line: {tb.tb_lineno}")

sys.excepthook = error_handler

logging.getLogger('aiogram').setLevel(logging.CRITICAL)
logging.getLogger('asyncio').setLevel(logging.CRITICAL)