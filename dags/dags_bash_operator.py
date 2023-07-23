from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="dags_bash_operator", ## airflow에들어왔을때 보이는 dag이름
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False, ## 날짜 누락된 구간은 코드 실행x(start_date부터 어제까지의 구간은 코드실행X)
    # dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "example2"], ## airflow에 들어왔을때 태그
    # params={"example_key": "example_value"}, ## 덱 밑에 테스크에 공통적으로 줄 파라미터들
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1", ## graph들어갔을때 보이는 이름
        bash_command="echo whoami",
    )
    
    bash_t2 = BashOperator(
        task_id="bash_t2", ## graph들어갔을때 보이는 이름
        bash_command="echo $HOSTNAME",
    )
    
    bash_t1 >> bash_t2
    