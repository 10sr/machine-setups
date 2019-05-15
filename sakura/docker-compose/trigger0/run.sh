#!/bin/sh
set -eux

export TRIGGER_SETTINGS_TOML=/settings.toml

envsubst \
    </settings.toml.envsubst \
    >$TRIGGER_SETTINGS_TOML

exec make migrate create_superuser runserver
