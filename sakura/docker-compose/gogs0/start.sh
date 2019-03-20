#!/bin/sh
set -eu

conf=/data/gogs/conf/app.ini
test -f $conf

if ! grep ^LANGS $conf
then
    cat <<'__EOC__' >>$conf

# Disable languages other than english
# https://gogs.io/docs/features/i18n
[i18n]
LANGS = en-US
NAMES = English
__EOC__
fi

# Run original CMD
exec /bin/s6-svscan /app/gogs/docker/s6/
