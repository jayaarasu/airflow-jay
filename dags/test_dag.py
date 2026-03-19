from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("new DAG")

with DAG(
    dag_id="Test_jay_dag",
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="hello_task",
        python_callable=hello
    )