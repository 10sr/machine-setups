#!/bin/sh
set -eux

set 2>&1

docker-compose down
docker build  -t local/st.3ends.info \
     "https://github.com/10sr/mastodon.git#st.3ends.info"
#docker-compose --verbose build --pull
docker-compose --verbose run --rm web rails db:migrate
docker-compose --verbose run --rm web rails assets:precompile
exec docker-compose --verbose up
