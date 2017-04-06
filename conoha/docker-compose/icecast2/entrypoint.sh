#!/bin/sh

set -eux

cat <<__EOC__ >/home/liquidsoap/liquidsoap.liq
output.icecast (
    %mp3,
    host = "133.130.91.27",
    port = ${ICECAST2_SERVER_PORT},
    password = "${ICECAST2_SOURCE_PASSWORD}",
    mount = "/${LIQUIDSOAP_MOUNTPOINT}",
    name = "/${LIQUIDSOAP_MOUNTPOINT}",
    encoding = "UTF-8",
    mksafe(playlist("${LIQUIDSOAP_PLAYLIST}"))
)
__EOC__

exec liquidsoap -d /home/liquidsoap/liquidsoap.liq
