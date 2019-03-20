#!/bin/sh
set -eu

# Run original CMD
exec /bin/s6-svscan /app/gogs/docker/s6/
