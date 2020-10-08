#!/usr/bin/env python3

from getpass import getpass

import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

user = PasswordUser(models.User())

user.username = input("Username: ")
user.email = input("Email: ")
user.password = getpass()

session = settings.Session()
session.add(user)
session.commit()
session.close()
exit()
