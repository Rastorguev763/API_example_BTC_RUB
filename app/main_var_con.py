# from config import *
from db_handler import *
from airflow.models import Variable
# from airflow.hooks.base_hook import BaseHook
from airflow.hooks.base import BaseHook

def my_variable():
    # DB_NAME = Variable.get('DB_NAME')
    # DB_USER = Variable.get('DB_USER')
    # DB_PASSWORD = Variable.get('DB_PASSWORD')
    # DB_HOST = Variable.get('DB_HOST')
    # DB_PORT = Variable.get('DB_PORT')
    NAME_TABLE = Variable.get('NAME_TABLE')
    ACCESS_KEY = Variable.get('API_KEY')
    SOURCE = Variable.get('SOURCE')
    TARGET = Variable.get('TARGET')
    # return DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, NAME_TABLE, ACCESS_KEY, SOURCE, TARGET
    return NAME_TABLE, ACCESS_KEY, SOURCE, TARGET

# DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, NAME_TABLE, ACCESS_KEY, SOURCE, TARGET = my_variable()
NAME_TABLE, ACCESS_KEY, SOURCE, TARGET = my_variable()

print('Starting')

# Создаем подключение к базе данных PostgreSQL
# connection = connect_to_db(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
conn = BaseHook.get_connection('my_conn_db')

connection = connect_to_db(conn.schema,
                            conn.login,
                            conn.password,
                            conn.host,
                            conn.port)

# Создаем курсор для выполнения SQL-запросов
cursor = connection.cursor()

# Создаем таблицу, если ее еще нет
create_table(cursor, NAME_TABLE)
create_summary_table(cursor)

print('Getting information in source')

# Получение информации о курсе в лайф
get_currency_rate_live(connection, cursor, ACCESS_KEY, SOURCE, TARGET, NAME_TABLE)

# Закрываем соединение с базой данных
cursor.close()
connection.close()

print('Connection closed, working ended')

