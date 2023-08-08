from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
from common.common_func import get_sftp



with DAG(
    dag_id="dags_python_import_func", ## airflow에들어왔을때 보이는 dag이름
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False, ## 날짜 누락된 구간은 코드 실행x(start_date부터 어제까지의 구간은 코드실행X)

) as dag:
    task_get_sftp=PythonOperator(
        task_id='task_get_sftp',
        python_callable=get_sftp
    )
    
    task_get_sftp