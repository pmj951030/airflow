from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator



with DAG(
    dag_id="dags_bash_with_tamplate", ## airflow에들어왔을때 보이는 dag이름
    schedule="10 * * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False, ## 날짜 누락된 구간은 코드 실행x(start_date부터 어제까지의 구간은 코드실행X)

) as dag:
    bash_t1=BashOperator(
        task_id='bash_t1',
        bash_command='echo "data_interval_end : {{data_interval_end}}"'
    )
    

    bash_t2=BashOperator(
        task_id='bash_t2',
        env={
            'START_DATE' : '{{data_interval_start | ds}}', ## yyyy-mm-dd 형태로 출력을 위해 |ds 넣음
            'END_DATE' : '{{data_interval_end | ds}}'
            bash_command='echo $START_DATE && echo $END_DATE'
        }
    )
    bash_t1 >> bash_t2