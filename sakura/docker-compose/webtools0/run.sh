#!/bin/sh
set -eux

export WEBTOOLS_SETTINGS_TOML=/settings.toml

envsubst \
    </settings.toml.envsubst \
    >$WEBTOOLS_SETTINGS_TOML

exec make migrate gunicorn
