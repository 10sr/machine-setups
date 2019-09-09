#!/bin/sh
set -eux
cp -pf /configmap_volume/nginx_index_html /usr/share/nginx/html/index.html
echo `hostname` >>/usr/share/nginx/html/index.html
exec nginx -g "daemon off;"
