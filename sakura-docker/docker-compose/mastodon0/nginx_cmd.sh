#!/bin/sh
set -eux

envsubst \
  '$NGINX_SERVER_NAME $NGINX_S3_SERVER_NAME $NGINX_SERVER_PORT $NGINX_S3_SERVER_PORT' \
  </etc/nginx/nginx.conf.envsubst \
  >/etc/nginx/nginx.conf

exec nginx -g 'daemon off;'
