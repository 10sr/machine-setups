#!/bin/sh
set -eux

set 2>&1

docker-compose down
docker build  -t local/st.3ends.info \
     "https://github.com/10sr/mastodon.git#st.3ends.info"
#docker-compose --verbose build --pull
while true
do
  timeout --preserve-status --signal=SIGTERM 30h docker-compose --verbose up
  echo "up.sh: Periodical restart"
  date
done
