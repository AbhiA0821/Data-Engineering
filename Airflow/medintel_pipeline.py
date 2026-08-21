from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


def validate_data():
    print("Validating processed healthcare data...")


with DAG(
    dag_id="medintel_end_to_end_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["medintel", "production-pipeline"],
) as dag:

    generate_data = BashOperator(
        task_id="generate_data",
        bash_command="echo 'Generating patient vital-sign data'",
    )

    process_with_pyspark = BashOperator(
        task_id="process_with_pyspark",
        bash_command="python /opt/airflow/spark/process_vitals.py",
    )

    validate = PythonOperator(
        task_id="validate_data",
        python_callable=validate_data,
    )

    load_to_duckdb = BashOperator(
        task_id="load_to_duckdb",
        bash_command="echo 'Loading processed data into DuckDB'",
    )

    generate_data >> process_with_pyspark >> validate >> load_to_duckdb