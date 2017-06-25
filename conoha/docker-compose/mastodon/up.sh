#!/bin/sh
set -eux

set 2>&1

docker-compose down
nice ionice docker build  -t local/st.3ends.info \
     "https://github.com/10sr/mastodon.git#st.3ends.info"
#nice docker-compose --verbose build --pull
nice ionice docker-compose --verbose run --rm web rails db:migrate
nice ionice docker-compose --verbose run --rm web rails assets:precompile
exec nice ionice docker-compose --verbose up
