#!/bin/sh

set -eux

ionice -c 2 -n 7 nice -n 19 rails db:migrate
ionice -c 2 -n 7 nice -n 19 rails assets:precompile
exec ionice -c 2 -n 7 nice -n 19 rails s -p 3000 -b 0.0.0.0
