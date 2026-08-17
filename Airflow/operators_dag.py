from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


def extract_data():
    print("Extracting patient data...")


def transform_data():
    print("Transforming patient data...")


def validate_data():
    print("Validating patient data...")


with DAG(
    dag_id="medintel_operators_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["medintel", "airflow"],
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_data,
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transform_data,
    )

    validate = PythonOperator(
        task_id="validate",
        python_callable=validate_data,
    )

    finish = BashOperator(
        task_id="finish",
        bash_command="echo 'MedIntel pipeline completed'",
    )

    extract >> transform >> validate >> finish