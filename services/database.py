# - *- coding: utf- 8 - *-
import sqlite3
from time import time
from data.config import PATH_DATABASE

########################################
#  _    _ _______ _____ _       _____  #
# | |  | |__   __|_   _| |     / ____| #
# | |  | |  | |    | | | |    | (___   #
# | |  | |  | |    | | | |     \___ \  #
# | |__| |  | |   _| |_| |____ ____) | #
#  \____/   |_|  |_____|______|_____/  #
########################################
# Спасибо Djimbo (https://lolz.guru/djimbo/)
# Форматирование запроса без аргументов


def update_format(sql, parameters: dict):
    if "XXX" not in sql:
        sql += " XXX "

    values = ", ".join([
        f"{item} = ?" for item in parameters
    ])
    sql = sql.replace("XXX", values)

    return sql, list(parameters.values())


# Форматирование запроса с аргументами
def update_format_args(sql, parameters: dict):
    sql = f"{sql} WHERE "

    sql += " AND ".join([
        f"{item} = ?" for item in parameters
    ])

    return sql, list(parameters.values())


# Преобразования sql списка в словарь
def dict_factory(cursor, row):
    save_dict = {}

    for idx, col in enumerate(cursor.description):
        save_dict[col[0]] = row[idx]

    return save_dict


##########################
#   _____  ____  _       #
#  / ____|/ __ \| |      #
# | (___ | |  | | |      #
#  \___ \| |  | | |      #
#  ____) | |__| | |____  #
# |_____/ \___\_\______| #
##########################
# Добавление пользователя
def add_user(userid, username, fullname):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        con.execute("INSERT INTO users "
                    "(userid, username, fullname, balance, created) "
                    "VALUES (?, ?, ?, ?, ?)",
                    [userid, username, fullname, 0, int(time())])
        con.commit()


# Получение пользователя
def get_user(**kwargs):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = "SELECT * FROM users"
        sql, parameters = update_format_args(sql, kwargs)
        return con.execute(sql, parameters).fetchone()


# Получение пользователей
def get_users(**kwargs):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = "SELECT * FROM users"
        sql, parameters = update_format_args(sql, kwargs)
        return con.execute(sql, parameters).fetchall()


# Получение всех пользователей
def get_all_users():
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = "SELECT * FROM users"
        return con.execute(sql).fetchall()


# Редактирование пользователя
def update_user(userid, **kwargs):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = f"UPDATE users SET"
        sql, parameters = update_format(sql, kwargs)
        parameters.append(userid)
        con.execute(sql + "WHERE userid = ?", parameters)
        con.commit()


# Удаление пользователя
def delete_user(**kwargs):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = "DELETE FROM users"
        sql, parameters = update_format_args(sql, kwargs)
        con.execute(sql, parameters)
        con.commit()


# Получение настроек
def get_settings():
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = "SELECT * FROM settings"
        return con.execute(sql).fetchone()
