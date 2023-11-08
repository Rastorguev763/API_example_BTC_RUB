from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

def my_variable():
    return Variable.get('bash_command_var_con')

# Настройте аргументы для вашего DAG
default_args = {
    'owner': 'your_username',
    'start_date': datetime.now(),  # Укажите конкретную дату начала выполнения DAG
    'retries': 1,  # Количество попыток в случае неудачи
    'retry_delay': timedelta(minutes=2), # Интервал между попытками 2 минуты
    'is_paused_upon_creation': False,  # Устанавливаем, чтобы DAG не был на паузе при создании
}

# Создайте объект DAG
dag = DAG(
    'run_main_var_con_py',
    default_args=default_args,
    schedule_interval="*/10 * * * *",  # Можете настроить расписание
    catchup=False,
    max_active_runs=1,  # Количество одновременных запусков DAG
)

run_main_task = BashOperator(
    task_id='execute_main_py',
    bash_command = my_variable(),  # Укажите путь к вашему main.py
    dag=dag,
)