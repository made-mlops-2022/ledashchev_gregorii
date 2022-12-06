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
        "predict",
        default_args=default_args,
        schedule_interval="50 23 * * *",  # every day at 23:50. Model might be fitted at 23:30 + t_0
        start_date=datetime.fromisoformat('2022-11-29T00:00:00'),
) as dag:
    process = DockerOperator(
        image="airflow-process-data",
        command="--input-dir /data/raw/{{ ds }} --output-dir /data/daily_processed/{{ ds }} --process-target false",
        network_mode="bridge",
        task_id="docker-airflow-process-data",
        do_xcom_push=False,
        mount_tmp_dir=False,
        auto_remove=True,
        mounts=[Mount(source=Variable.get("path_to_data"), target="/data", type='bind')]
    )

    predict = DockerOperator(
        image="airflow-predict",
        command="--input-data-dir /data/daily_processed/{{ ds }} "
                f"--input-model-dir {Variable.get('path_to_model_loading')} "
                "--output-dir /data/predictions/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-predict",
        do_xcom_push=False,
        mount_tmp_dir=False,
        auto_remove=True,
        mounts=[Mount(source=Variable.get("path_to_data"), target="/data", type='bind')]
    )
    process >> predict
