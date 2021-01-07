#!/bin/sh

set -eux

mkdir -p /var/www/html/config

# Are these required?
cp -pf /local.config.php /var/www/html/config/local.config.php
cp -pf /redis.config.php /usr/src/nextcloud/config/redis.config.php

exec php-fpm
