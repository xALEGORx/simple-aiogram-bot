# - *- coding: utf- 8 - *-
import configparser

read_config = configparser.ConfigParser()
read_config.read('settings.ini')

BOT_TOKEN = read_config['settings']['token'].strip()  # Токен бота
RATE_LIMIT = float(read_config['settings']['rate_limit'].strip())  # Антифлуд
PATH_DATABASE = 'data/database.db'  # Путь к БД
PATH_LOGS = 'data/logs.log'  # Путь к Логам

def get_admins():
    read_admins = configparser.ConfigParser()
    read_admins.read('settings.ini')

    admins = read_admins['settings']['admin_id'].strip()
    admins = admins.replace(' ', '')

    admins = admins.split(',')
    admins = list(map(int, admins))

    return admins
