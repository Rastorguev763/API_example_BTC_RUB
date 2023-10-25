from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 24),
}

dag = DAG(
    'my_docker_dag',
    default_args=default_args,
    description='Run app_container every 10 minutes',
    schedule_interval=timedelta(minutes=1),
    catchup=False,  # Если вы хотите избежать наведения с накоплением данных
)

# run_docker_task = DockerOperator(
#     task_id='run_app_container',
#     image='api_example_btc_rub-app',  # Имя вашего контейнера
#     api_version='auto',
#     docker_url='tcp://docker-proxy:2375',
#     command='python /app/main.py',  # Команда, которую нужно выполнить в контейнере
#     network_mode='bridge',  # Возможно, вам понадобится настроить сеть
#     dag=dag,
# )


# run_docker_task
# docker run -v /var/run/docker.sock:/var/run/docker.sock
# Создание BashOperator для запуска контейнера Docker
run_docker_container = BashOperator(
    task_id='run_docker_container',
    bash_command='docker run -v /var/run/docker.sock:/var/run/docker.sock api_example_btc_rub-app:latest',
    # bash_command='docker --version',
    dag=dag,
)

run_docker_container
if __name__ == "__main__":
    dag.cli()
