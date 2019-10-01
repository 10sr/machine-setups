#!/bin/sh
set -eux

. ../prometheus0.env
#export NODE_EXPORTER_PASSWORD

# prometheus image does not have envsubst command, so do this outside of container


exec docker-compose up --build
