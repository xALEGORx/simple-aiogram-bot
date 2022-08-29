# - *- coding: utf- 8 - *-
import logging
import colorlog

from data.config import PATH_LOGS

bot_logger = logging.getLogger(__name__)

log_formatter_file = logging.Formatter("%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s")
log_formatter_console = colorlog.ColoredFormatter(
    "%(purple)s%(levelname)s %(blue)s|%(purple)s %(asctime)s %(blue)s|%(purple)s %(filename)s:%(lineno)d %(blue)s|%(purple)s %(message)s%(red)s",
    datefmt="%d-%m-%Y %H:%M:%S",
)

log_formatter_file_user = logging.Formatter("%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(userid)s | %(message)s")

file_handler = logging.FileHandler(PATH_LOGS, "a", "utf-8")
file_handler.setFormatter(log_formatter_file)
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter_console)

bot_logger.addHandler(file_handler)
bot_logger.addHandler(console_handler)
