#!/bin/sh
set -eux

set 2>&1

docker-compose down
nice ionice docker-compose run --rm web rails db:migrate
nice ionice docker-compose run --rm web rails assets:precompile
exec nice ionice docker-compose up --build
