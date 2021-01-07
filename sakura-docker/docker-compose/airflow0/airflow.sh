#!/bin/sh

docker-compose run --rm webserver airflow "$@"
