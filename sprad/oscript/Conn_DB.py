#import json
#import datetime
#from time import gmtime, strftime

#from jpro.models import Tournaments

# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3 as db

from .set_tournaments import RealizTournaments

def get_connection (db_name):
    # Создаем соединение с нашей базой данных
    # В нашем примере у нас это просто файл базы
    conn = db.connect(db_name)
    return conn

def addMatches(tbl, jdata): # f_conn_BD
    conn = get_connection ('db.sqlite3')
    # Создаем курсор - это специальный объект который делает запросы и получает их результаты
    cursor = conn.cursor()
# ТУТ БУДЕТ НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ
    RealizTournaments(cursor,conn, jdata)


# КОД ДАЛЬНЕЙШИХ ПРИМЕРОВ ВСТАВЛЯТЬ В ЭТО МЕСТО

#    results = cursor.fetchall()
#    print(results)

# Не забываем закрыть соединение с базой данных
    conn.close()
