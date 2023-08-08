from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
from common.common_func import regist



with DAG(
    dag_id="dags_python_with_args", ## airflow에들어왔을때 보이는 dag이름
    schedule="* * * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False, ## 날짜 누락된 구간은 코드 실행x(start_date부터 어제까지의 구간은 코드실행X)

) as dag:
    
    regist_t1=PythonOperator(
        task_id='regist_t1',
        python_callable=regist,
        op_args=['mjpark','man','kr','seoul']
    )

    regist_t1
    