from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator



with DAG(
    dag_id="dags_bash_with_macro_eg2", ## airflow에들어왔을때 보이는 dag이름
    schedule="10 0 * * 6#2",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False, ## 날짜 누락된 구간은 코드 실행x(start_date부터 어제까지의 구간은 코드실행X)

) as dag:
    # START_DATE : 2주전 월요일, END_DATE : 2주전 토요일
    bash_task_1=BashOperator(
        task_id='bash_task_2',
        env={'START_DATE':'{{(data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=19))|ds}}',
             'END_DATE':'{{(data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=14))|ds}}'},
    bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
    )

    