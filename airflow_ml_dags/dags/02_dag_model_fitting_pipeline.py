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
        "model_fitting",
        default_args=default_args,
        schedule_interval="30 23 * * 0",  # every Sunday at 23:30:00. Data are loaded 30 minutes ago.
        start_date=datetime.fromisoformat('2022-11-29T12:00:00'),
) as dag:
    process = DockerOperator(
        image="airflow-process-data",
        command="--input-dir /data/raw/{{ ds }} --output-dir /data/processed/{{ ds }} --process-target true",
        network_mode="bridge",
        task_id="docker-airflow-process-data",
        do_xcom_push=False,
        mount_tmp_dir=False,
        auto_remove=True,
        mounts=[Mount(source=Variable.get("path_to_data"), target="/data", type='bind')]
    )

    train_test_split = DockerOperator(
        image="airflow-split-data",
        command="--input-dir /data/processed/{{ ds }} --output-dir /data/split/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-split-data",
        do_xcom_push=False,
        mount_tmp_dir=False,
        auto_remove=True,
        mounts=[Mount(source=Variable.get("path_to_data"), target="/data", type='bind')]
    )

    fit_model = DockerOperator(
        image="airflow-fit",
        command="--input-dir /data/split/{{ ds }} --output-dir /data/model/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-fit-data",
        do_xcom_push=False,
        mount_tmp_dir=False,
        auto_remove=True,
        mounts=[Mount(source=Variable.get("path_to_data"), target="/data", type='bind')]
    )

    validate_model = DockerOperator(
        image="airflow-validate",
        command="--input-data-dir /data/split/{{ ds }} "
                f"--input-model-dir {Variable.get('path_to_model_saving')} "
                "--output-dir /data/validation/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-validate",
        do_xcom_push=False,
        mount_tmp_dir=False,
        auto_remove=True,
        mounts=[Mount(source=Variable.get("path_to_data"), target="/data", type='bind')]
    )
    process >> train_test_split >> fit_model >> validate_model
