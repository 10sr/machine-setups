#!/bin/sh
set -eux

# echo 'config.force_ssl = true' \
    #      >>./config/environments/production.rb
patch -p1 </secure_cookie.patch

exec "$@"
