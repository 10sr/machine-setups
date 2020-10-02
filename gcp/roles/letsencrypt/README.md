letsencrypt
===========

TODO: 途中でコマンド実行する必要があるのでそのことについてかく


DNS レコードが追加されてるかチェックする

    nslookup -type=TXT _acme-challenge.halt2.net. 8.8.8.8
    dig @8.8.8.8 -t TXT _acme-challenge.halt2.net.
