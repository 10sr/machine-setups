from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.docker_operator import DockerOperator
from airflow.utils.dates import days_ago

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
task_default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(
    'test2',
    default_args=task_default_args,
    description='Test2 DAG',
    schedule_interval=timedelta(days=1),
)

t_bash_test = BashOperator(
    task_id='t_bash_test',
    bash_command='set -eux -o pipefail; env; date; hostname; whoami',
    dag=dag,
)

t_docker_test = DockerOperator(
    task_id='t_docker_test',
    image="debian",
    command='set -eux -o pipefail; env; date; hostname; whoami',
    dag=dag,
)

t_post_cmd = BashOperator(
    task_id='t_post_cmd',
    bash_command='echo "SUCCESS!"',
    dag=dag,
)

[t_bash_test, t_docker_test] >> t_post_cmd
