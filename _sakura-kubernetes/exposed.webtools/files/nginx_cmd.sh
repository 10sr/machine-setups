#!/bin/sh
set -eux
cp -pf $VOLUME_MOUNT_PATH/nginx_index.html /usr/share/nginx/html/index.html
echo `hostname` >>/usr/share/nginx/html/index.html
exec nginx -g "daemon off;"
