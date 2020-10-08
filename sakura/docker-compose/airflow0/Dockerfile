# Python3.7 cannot run airflow 1.9.0 because of async symbol
# FROM python:3.7
FROM python:3.6

# Airflow 1.10 系は initdb 時に explicit_defaults_for_timestamp = 1 を設定しようとするが、
# 現在の MariaDB Ver 10.0.38-MariaDB-0ubuntu0.16.04.1 はこれをサポートしていない。
# MariaDB 10.1.8 以降が提供されるか、 sqlalchemy で mariadb dialiect がサポートされれば
# 1.10 系を使うことができそうだが、現在はどちらも利用できない。
# MariaDB explicit_defaults_for_timestamp
# https://mariadb.com/kb/en/server-system-variables/#explicit_defaults_for_timestamp
# mariadb dialect
# https://github.com/sqlalchemy/sqlalchemy/commit/cd03b8f0cecbf72ecd6c99c4d3a6338c8278b40d
ARG AIRFLOW_VERSION=1.9.0

# werkzeug==0.15.2 is required to avoid ImportError: cannot import name 'import_string' from 'werkzeug' error
# https://blog.csdn.net/weixin_41759152/article/details/105990535
# pasword subpackage is required for password login
RUN pip install apache-airflow[mysql,password]==${AIRFLOW_VERSION} werkzeug==0.15.2 cryptography
