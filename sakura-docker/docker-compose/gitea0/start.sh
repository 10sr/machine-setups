#!/bin/sh
set -eux

conf_envsubst=/app.ini.envsubst
conf=/data/gitea/conf/app.ini
test -f $conf_envsubst

# Is there a way to assert variables are defined?
envsubst \
    '$SERVER_LFS_JWT_SECRET $SECURITY_SECRET_KEY $SECURITY_INTERNAL_TOKEN $OAUTH2_JWT_SECRET' \
    <$conf_envsubst >$conf


exec /bin/s6-svscan /etc/s6/
