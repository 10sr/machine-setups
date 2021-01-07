#!/bin/sh
set -eux

# envsubst \
    #   '$NGINX_SERVER_NAME' \
    #   </etc/nginx/nginx.conf.envsubst \
    #   >/etc/nginx/nginx.conf

# Currently there are no substitution
cp -v /etc/nginx/nginx.conf.envsubst /etc/nginx/nginx.conf

exec nginx -g 'daemon off;'
