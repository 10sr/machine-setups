#!/bin/sh
set -eux

. ../prometheus0.env
#export NODE_EXPORTER_PASSWORD

# prometheus image does not have envsubst command, so do this outside of container
env -i - \
    "NODE_EXPORTER_PASSWORD=$NODE_EXPORTER_PASSWORD" \
    envsubst \
    <./prometheus.yml.envsubst \
    >./prometheus.yml
env -i - \
    "AM_EMAIL_TO=$AM_EMAIL_TO" \
    "AM_EMAIL_FROM=$AM_EMAIL_FROM" \
    "AM_SMTP_SMARTHOST=$AM_SMTP_SMARTHOST" \
    "AM_SMTP_USERNAME=$AM_SMTP_USERNAME" \
    "AM_SMTP_PASSWORD=$AM_SMTP_PASSWORD" \
    envsubst \
    <./alertmanager.yml.envsubst \
    >./alertmanager.yml


exec docker-compose up --build
