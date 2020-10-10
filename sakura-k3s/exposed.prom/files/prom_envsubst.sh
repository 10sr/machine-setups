#!/bin/sh
set -eux

in=$1
out=$2

env -i - \
    "NODE_EXPORTER_PASSWORD=$NODE_EXPORTER_PASSWORD" \
    "NODE_EXPORTER_HOSTNAME=$NODE_EXPORTER_HOSTNAME" \
    "AM_SERVICE_NAME=$AM_SERVICE_NAME" \
    "RULE_FILE=$RULE_FILE" \
    envsubst \
    <$in \
    >$out

# env -i - \
    #     "AM_EMAIL_TO=$AM_EMAIL_TO" \
    #     "AM_EMAIL_FROM=$AM_EMAIL_FROM" \
    #     "AM_SMTP_SMARTHOST=$AM_SMTP_SMARTHOST" \
    #     "AM_SMTP_USERNAME=$AM_SMTP_USERNAME" \
    #     "AM_SMTP_PASSWORD=$AM_SMTP_PASSWORD" \
    #     envsubst \
    #     <./alertmanager.yml.envsubst \
    #     >./alertmanager.yml
