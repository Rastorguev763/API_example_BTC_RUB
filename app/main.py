from config import *
from db_handler import *

print('Starting')

# Создаем подключение к базе данных PostgreSQL
connection = connect_to_db(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)

print('Connect to database')

# Создаем курсор для выполнения SQL-запросов
cursor = connection.cursor()

# Создаем таблицу, если ее еще нет
create_table(cursor, NAME_TABLE)
create_summary_table(cursor)

print('Getting information in source')

# Полученин информации о курсе за заданный период(период задаем в конфиге)
# get_currency_rate(connection, cursor, LAST_DAY, YEAR, MONTH, ACCESS_KEY, SOURCE, TARGET, NAME_TABLE )

# print('Converting data from the database')

# max_date = get_day_max_currency_exchange_rate(cursor, NAME_TABLE)
# min_date = get_day_min_currency_exchange_rate(cursor, NAME_TABLE)
# max_rate = get_max_rate(cursor, NAME_TABLE)
# min_rate = get_min_rate(cursor, NAME_TABLE)
# average_rate = get_avg_rate(cursor, NAME_TABLE)
# last_day_rate = get_rate_last_day(cursor, NAME_TABLE)

# print('Writing data to summary table')

# insert_data_summary_table(connection, cursor, SOURCE+TARGET, MONTH, max_date, min_date, max_rate, min_rate, average_rate, last_day_rate)

# Получение информации о курсе в лайф
get_currency_rate_live(connection, cursor, ACCESS_KEY, SOURCE, TARGET, NAME_TABLE)

# Закрываем соединение с базой данных
cursor.close()
connection.close()

print('Connection closed, working ended')