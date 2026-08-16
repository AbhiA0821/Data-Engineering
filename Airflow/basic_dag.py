from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def extract_data():
    print("Extracting healthcare data...")


def transform_data():
    print("Transforming healthcare data...")


def load_data():
    print("Loading processed data...")


with DAG(
    dag_id="medintel_basic_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["medintel", "data-engineering"],
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