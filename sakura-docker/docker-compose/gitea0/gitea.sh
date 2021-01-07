#!/bin/sh
set -eux
docker-compose exec --user 1002 app /usr/local/bin/gitea "$@"

