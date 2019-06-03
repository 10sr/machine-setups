#!/bin/sh
set -eux
docker-compose exec --user 1000 app /usr/local/bin/gitea "$@"

