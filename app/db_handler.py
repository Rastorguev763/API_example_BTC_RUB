import psycopg2
from api_handler import fetch_exchange_rate


def connect_to_db(db_name, db_user, db_password, db_host, db_port):
    return psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )

def create_table(cursor, name_table):
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {name_table} (
        id SERIAL PRIMARY KEY,
        date DATE,
        first_currency VARCHAR,
        second_currency VARCHAR,
        rate DECIMAL
    );
    """
    cursor.execute(create_table_query)

def insert_data(cursor, date, first_currency, second_currency, rate, name_table):
    insert_query = f'INSERT INTO {name_table} (date, first_currency, second_currency, rate) VALUES (%s, %s, %s, %s, %s)'
    cursor.execute(insert_query, (date, first_currency, second_currency, rate))

def get_day_max_currency_exchange_rate(cursor, name_table):
    # Находим день с максимальным курсом
    cursor.execute(f"SELECT date FROM {name_table} WHERE rate = (SELECT MAX(rate) FROM {name_table});")
    max_date = cursor.fetchone()
    return max_date

def get_day_min_currency_exchange_rate(cursor, name_table):
    # Находим день с минимальным курсом
    cursor.execute(f"SELECT measurement_date FROM {name_table} WHERE rate = (SELECT MIN(rate) FROM {name_table});")
    min_date = cursor.fetchone()
    return min_date

def get_max_rate(cursor, name_table):
    # Находим максимальное значение курса
    cursor.execute(f"SELECT MAX(rate) FROM {name_table};")
    max_rate = cursor.fetchone()[0]
    return max_rate

def get_min_rate(cursor, name_table):
    # Находим минимальное значение курса
    cursor.execute(f"SELECT MIN(rate) FROM {name_table};")
    min_rate = cursor.fetchone()[0]
    return min_rate

def get_avg_rate(cursor, name_table):
    # Рассчитываем среднее значение курса
    cursor.execute(f"SELECT AVG(rate) FROM {name_table};")
    average_rate = cursor.fetchone()[0]
    return average_rate

def get_rate_last_day(cursor, name_table):
    # Находим значение курса на последний день месяца
    cursor.execute("SELECT rate FROM bitcoin_rates WHERE measurement_date = (SELECT MAX(measurement_date) FROM bitcoin_rates);")
    last_day_rate = cursor.fetchone()[0]
    return last_day_rate

def create_summary_table(cursor):
    create_summary_table = f"""
    CREATE TABLE IF NOT EXISTS summary_table (
        currency VARCHAR
        max_date DATE
        min_date DATE
        max_rate DECIMAL
        min_rate DECIMAL
        average_rate DECIMAL
        last_day_rate DECIMAL
    );
    """
    cursor.execute(create_summary_table)

def insert_data_summary_table(cursor, currency, max_date, min_date, max_rate, min_rate, average_rate, last_day_rate):
    insert_query = 'INSERT INTO summary_table (currency, max_date, min_date, max_rate, min_rate, average_rate, last_day_rate) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(insert_query, (currency, max_date, min_date, max_rate, min_rate, average_rate, last_day_rate))

def get_currency_rate(connection, cursor, last_day, year, month, access_key, source, target, name_table ):
    try:
        # Цикл для запроса данных для каждой даты
        for day in range(1, last_day + 1):
            date = f"{year}-{month:02d}-{day:02d}"
            rate = fetch_exchange_rate(access_key, source, target, date)

            if rate is not None:
                insert_data(cursor, date, source, target, rate, name_table)
                connection.commit()
                print('Данные успешно обновлены.')
            else:
                print(f'Ошибка при выполнении запроса для даты {date}')
    except Exception as e:
        print()
        print(f'Ошибка: {str(e)}')