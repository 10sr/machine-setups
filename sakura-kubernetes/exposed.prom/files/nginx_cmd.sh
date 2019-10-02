#!/bin/sh
set -eux

in=$1
out=/etc/nginx/nginx.conf

envsubst \
    '$PROM_SERVICE_NAME $AM_SERVICE_NAME' \
    <$in \
    >$out

exec nginx -g 'daemon off;'
