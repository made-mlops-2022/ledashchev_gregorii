from datetime import timedelta
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from docker.types import Mount
from airflow.models import Variable

default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "generate_data",
        default_args=default_args,
        schedule_interval="0 23 * * *",  # every day at 23:00
        start_date=datetime.fromisoformat('2022-11-29T00:00:00'),
) as dag:
    download = DockerOperator(
        image="airflow-generate-data",
        command="--output-dir /data/raw/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-generate-data",
        do_xcom_push=False,
        mount_tmp_dir=False,
        auto_remove=True,
        mounts=[Mount(source=Variable.get("path_to_data"), target="/data", type='bind')]
    )
