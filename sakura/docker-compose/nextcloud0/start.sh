#!/bin/sh

set -eux

cp -pf /local.config.php /var/www/html/config/local.config.php

exec php-fpm
