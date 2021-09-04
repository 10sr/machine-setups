LDAP initialie role
===================

LDPA サーバのインストールと初期設定を行う。


- /etc/ldap/slap.d は、 /etc/ldap/slap.conf から生成を行う
- パッケージインストール直後は /etc/ldap/slap.d は存在するがこれは削除する必要がある。しかし一度 slap.conf から生成してデータを入れた後は削除しないほうが良いような気がする。どうすればよいか？
- 冪等性は諦めたほうがよい？


行った手順
----------

1. systemctl stop slapd
2. mv /etc/ldap/slapd.d{,.bak}
3. mv /var/lib/ldap{,.bak}
4. Playbook 実行
5. cd /etc/ldap && sudo -u openldap slaptest -f slapd.conf -F slapd.d

最後の slaptest において以下の出力が出るが問題ない

```
root@tk2-407-44672:/etc/ldap# sudo -u openldap slaptest -f ./slapd.conf -F slapd.d
5eb677a2 mdb_db_open: database "dc=3ends,dc=info" cannot be opened: No such file or directory (2). Restore from backup!
5eb677a2 backend_startup_one (type=mdb, suffix="dc=3ends,dc=info"): bi_db_open failed! (2)
slap_startup failed (test would succeed using the -u switch)
```
