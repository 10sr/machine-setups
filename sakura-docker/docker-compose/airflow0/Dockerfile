FROM python:3.6
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install docker
# https://docs.docker.com/engine/install/debian/
RUN apt update
RUN apt install -y \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
RUN apt update
RUN apt install -y docker-ce-cli



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
RUN pip install apache-airflow[mysql,password,crypto]==${AIRFLOW_VERSION} werkzeug==0.15.2

# docker.Client has been renamed in 2.0.0
RUN pip install docker-py[tls]==1.10.6
