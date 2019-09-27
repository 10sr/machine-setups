#!/bin/sh
set -eux

envsubst \
    </settings.toml.envsubst \
    >$WEBTOOLS_SETTINGS_TOML

exec make migrate collectstatic gunicorn
