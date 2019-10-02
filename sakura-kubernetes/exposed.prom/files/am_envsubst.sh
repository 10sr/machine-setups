#!/bin/sh
set -eux

in=$1
out=$2

env -i - \
    "AM_EMAIL_TO=$AM_EMAIL_TO" \
    "AM_EMAIL_FROM=$AM_EMAIL_FROM" \
    "AM_SMTP_SMARTHOST=$AM_SMTP_SMARTHOST" \
    "AM_SMTP_USERNAME=$AM_SMTP_USERNAME" \
    "AM_SMTP_PASSWORD=$AM_SMTP_PASSWORD" \
    envsubst \
    <$in \
    >$out
