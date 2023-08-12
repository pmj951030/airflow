from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator



with DAG(
    dag_id="dags_bash_with_macro_eg1", ## airflow에들어왔을때 보이는 dag이름
    schedule="10 0 L * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False, ## 날짜 누락된 구간은 코드 실행x(start_date부터 어제까지의 구간은 코드실행X)

) as dag:
    # START_DATE : 전원 말일, END_DATE: 1일전
    bash_task_1=BashOperator(
        task_id='bash_task_1',
        env={'START_DATE':'{{data_interval_start.in_timezone("Asia/Seoul") | ds}}',## 기본적으로 UTC로 되어있어서 한국보다 9시간느림 따라서 한국타임존으로 맞춰야함
             'END_DATE':'{{(data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=1))|ds }}'}, ## -연산자 같은거 할꺼면 days해야함
    bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
    )

    