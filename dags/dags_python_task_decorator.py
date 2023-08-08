from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
from airflow.decorators import task



with DAG(
    dag_id="dags_python_task_decorator", ## airflow에들어왔을때 보이는 dag이름
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False, ## 날짜 누락된 구간은 코드 실행x(start_date부터 어제까지의 구간은 코드실행X)

) as dag:
    @task(task_id='python_task_1')
    def print_text(input_text):
        print(input_text)
        
    python_task_1=print_text('task 데코레이터 실행')

    