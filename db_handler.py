import psycopg2

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
