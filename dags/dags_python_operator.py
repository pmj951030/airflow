from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
import random


with DAG(
    dag_id="dags_python_operator", ## airflow에들어왔을때 보이는 dag이름
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False, ## 날짜 누락된 구간은 코드 실행x(start_date부터 어제까지의 구간은 코드실행X)
    # dagrun_timeout=datetime.timedelta(minutes=60),
    # params={"example_key": "example_value"}, ## 덱 밑에 테스크에 공통적으로 줄 파라미터들
) as dag:
    def select_fruit():
        fruit=['apple','banana','orange']
        rand_int=random.randint(0,3)
        print(fruit[rand_int])
    
    py_t1=PythonOperator(
        task_id='py_t1',
        python_callable=select_fruit
    )
    
    py_t1
    