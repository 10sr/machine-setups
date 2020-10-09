from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
task_default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['8.slashes@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(
    'mailtest',
    default_args=task_default_args,
    description='Mail Test',
    schedule_interval=None,
)

t1 = BashOperator(
    task_id='task_failures',
    bash_command=("set -eux -o pipefail; " +
                  "date; " +
                  "hostname; " +
                  "whoami; " +
                  "echo 'run_id={{ run_id }} dag_run={{ dag_run }}'; " +
                  "false; "),
    dag=dag,
)
