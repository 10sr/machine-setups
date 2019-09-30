#!/bin/sh
set -eux

export WEBTOOLS_SETTINGS_TOML=/settings.toml

envsubst \
    <$WEBTOOLS_SETTINGS_TOML_ENVSUBST \
    >$WEBTOOLS_SETTINGS_TOML

env

cat $WEBTOOLS_SETTINGS_TOML

# while true; do sleep 1000; done

exec make migrate collectstatic gunicorn
