import os
import calendar

# Загрузка переменных окружения из файла .env
from dotenv import load_dotenv
load_dotenv()

ACCESS_KEY = os.getenv('API_KEY')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Исходная валюта и валюта, для которой получаем данные
SOURCE = 'BTC'
TARGET = 'RUB'
YEAR = 2023
MONTH = 2
LAST_DAY = calendar.monthrange(YEAR, MONTH)[1]
NAME_TABLE = 'bitcoin_rates_to_rub'
