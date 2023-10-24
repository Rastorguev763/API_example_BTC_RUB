from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'your_username',
    'start_date': datetime(2023, 10, 24),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_docker_dag',
    default_args=default_args,
    description='Run app_container every 10 minutes',
    schedule_interval=timedelta(minutes=10),
    catchup=False,  # Если вы хотите избежать наведения с накоплением данных
)

run_docker_task = DockerOperator(
    task_id='run_app_container',
    image='app_container',  # Имя вашего контейнера
    command='python /path/to/your/main.py',  # Команда, которую нужно выполнить в контейнере
    network_mode='bridge',  # Возможно, вам понадобится настроить сеть
    dag=dag,
)

run_docker_task

if __name__ == "__main__":
    dag.cli()
