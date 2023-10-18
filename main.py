from config import *
from api_handler import fetch_exchange_rate
from db_handler import connect_to_db, create_table, insert_data

def get_exchange_rate():
    try:
        # Создаем подключение к базе данных PostgreSQL
        connection = connect_to_db(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)

        # Создаем курсор для выполнения SQL-запросов
        cursor = connection.cursor()

        # Создаем таблицу, если ее еще нет
        create_table(cursor, NAME_TABLE)

        # Цикл для запроса данных для каждой даты
        for day in range(1, LAST_DAY + 1):
            date = f"{YEAR}-{MONTH:02d}-{day:02d}"
            rate = fetch_exchange_rate(ACCESS_KEY, SOURCE, TARGET, date)

            if rate is not None:
                insert_data(cursor, date, SOURCE, TARGET, rate, NAME_TABLE)
                connection.commit()
            else:
                print(f'Ошибка при выполнении запроса для даты {date}')

        # Закрываем соединение с базой данных
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        print(f'Ошибка: {str(e)}')
        return False

if get_exchange_rate():
    print('Данные успешно обновлены.')
else:
    print('Ошибка при обновлении данных.')

if __name__ == "__main__":
    get_exchange_rate()