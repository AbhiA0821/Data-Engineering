from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="medintel_pyspark_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["medintel", "pyspark"],
) as dag:

    run_pyspark = BashOperator(
        task_id="run_pyspark_processing",
        bash_command="python /opt/airflow/spark/process_vitals.py",
    )

    finish = BashOperator(
        task_id="pipeline_complete",
        bash_command="echo 'PySpark processing completed'",
    )

    run_pyspark >> finish