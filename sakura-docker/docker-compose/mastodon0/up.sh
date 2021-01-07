#!/bin/sh
set -eux

set 2>&1

docker-compose down
make build-image
#docker-compose --verbose build --pull
while true
do
  timeout --preserve-status --signal=SIGTERM 30h docker-compose --verbose up
  echo "up.sh: Periodical restart"
  date
done
