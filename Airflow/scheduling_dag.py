from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


def extract_data():
    print("Extracting patient data...")


def transform_data():
    print("Transforming patient data...")


def load_data():
    print("Loading data into analytical storage...")


default_args = {
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="medintel_scheduled_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
    tags=["medintel", "airflow"],
) as dag:

    extract = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data,
    )

    transform = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data,
    )

    load = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
    )

    extract >> transform >> load