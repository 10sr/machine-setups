#!/bin/sh
set -eux

user=prom
group=prom

# https://github.com/go-gitea/gitea/blob/master/Dockerfile
grep ^${group} /etc/group || addgroup -S -g 1000 ${group}
id ${user} || adduser -S -H -D -u 1000 -G ${group} ${user}
echo "${user}:$(dd if=/dev/urandom bs=24 count=1 status=none | base64)" | chpasswd
mkdir -p /home/${user}; chown -R ${user}:${group} /home/${user}

chown -R ${user}:${group} /prometheus

# apt-get update
# apt-get install --yes sudo

command="/bin/prometheus $@"
exec su ${user} -c "$command"
