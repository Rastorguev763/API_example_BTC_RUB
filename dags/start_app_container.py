from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Настройте аргументы для вашего DAG
default_args = {
    'owner': 'your_username',
    'start_date': datetime.now(),
    'retries': 1,  # Количество попыток в случае неудачи
    'retry_delay': timedelta(minutes=2), # Интервал между попытками 2 минуты
    'is_paused_upon_creation': False,  # Устанавливаем, чтобы DAG не был на паузе при создании
}

# Создайте объект DAG
dag = DAG(
    'run_main_py',
    default_args=default_args,
    schedule_interval="* /10 * * *",  # Можете настроить расписание
    catchup=False,
    max_active_runs=1,  # Количество одновременных запусков DAG
)

# Создайте оператор BashOperator для выполнения main.py
run_main_task = BashOperator(
    task_id='execute_main_py',
    bash_command='python /app/main.py',  # Укажите путь к вашему main.py
    dag=dag,
)

# Определите порядок выполнения задач
run_main_task
