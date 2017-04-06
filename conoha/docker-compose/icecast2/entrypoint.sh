#!/bin/sh

set -eux

find "$LIQUIDSOAP_DIRECTORY" -type f -name '*.mp3' \
     >/usr/share/liquidsoap/playlist.m3u

cat <<__EOC__ | exec liquidsoap -
output.icecast (
    %mp3,
    host = "133.130.91.27",
    port = ${ICECAST2_SERVER_PORT},
    password = "${ICECAST2_SOURCE_PASSWORD}",
    mount = "/${LIQUIDSOAP_MOUNTPOINT}",
    name = "/${LIQUIDSOAP_MOUNTPOINT}",
    encoding = "UTF-8",
    mksafe(playlist("/usr/share/liquidsoap/playlist.m3u"))
)
__EOC__
