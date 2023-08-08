from airflow import DAG
import datetime
import pendulum
from airflow.operators.email import EmailOperator


with DAG(
    dag_id="dags_email_operator", ## airflow에들어왔을때 보이는 dag이름
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False, ## 날짜 누락된 구간은 코드 실행x(start_date부터 어제까지의 구간은 코드실행X)
    # dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "example2"], ## airflow에 들어왔을때 태그
    # params={"example_key": "example_value"}, ## 덱 밑에 테스크에 공통적으로 줄 파라미터들
) as dag:
    send_email_task=EmailOperator(
        task_id='send_email_task',
        to='audwls7857@naver.com', ## 네이버로 보내기
        html_content='Airflow작업 완료'
    )