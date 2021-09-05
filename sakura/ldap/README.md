ldap/
=====

LDAP の学習を目的に slapd を立てたりするやつ


Terminology
-----------

- **DN** Distinguished Name 。`cn=Manager,dc=3ends,dc=info` みたいなやつ。絶対パス。
- **RDN** Relative Distinguished Name 。 DN の中の `cn=Manager` の部分。ファイル名。
  エントリのうちどれか一つの属性値を RDN として使用する。どの属性値を RDN として使用するかは自由に決定することができる。
  持ってない値を RDN にしようとしたらどうなるんだろう？
- **Bind DN** LDAP へのアクセス時に認証に使用する DN 。
  Bind DN とその `userPassword` を使用して認証を行う。
  このパスワードは **Bind Password** と呼ぶ。
- **rootdn**  LDAP ディレクトリ管理者。
  データのブートストラップに必要で、特に初期構築時はこの DN を Bind DN として使用する。
  `cn=Manager,dc=3ends,dc=info` のように `cn=Manager` という名前を使うのが一般的。


Command
-------

例えば、 ldap にエントリを追加するには以下のコマンドを実行する。

    ldapadd -x -W -D "cn=Manager,dc=3ends,dc=info" -f people-service.ldif

ここで、それぞれ以下の意味がある。

- `ldapadd` エントリを追加する
- `-x` SASL ではなく単純な認証を使用する（？）
- `-W` パスワードを引数で与えるのではなくプロンプトから入力させる
- `-D "cn=Manager,dc=3ends,dc=info"` 与えた DN を binddn として使用する（LDAP にアクセスする DN として使用する）
- `-f people-service.ldif` 追加するエントリが記述されたファイルを与える


以下のコマンドで検索できる。

    ldapsearch -x -W -D "cn=Manager,dc=3ends,dc=info" -b 'dc=3ends,dc=info' '(objectClass=*)' dn

- `-b 'dc=3ends,dc=info'` 検索を行うディレクトリ
- `'(objectClass=*)'` 検索条件
- `dn` 表示する属性


設定ディレクトリを検索するには以下。

- ここで上と同様の `-D "cn=Manager,dc=3ends,dc=info"` が使用できないのは権限がないため？

    ldapsearch -Y EXTERNAL -H ldapi:/// -b 'cn=config' '(objectclass=*)' dn

- `-Y EXTERNAL` SASL 認証として EXTERNAL を使用する
- `-H ldapi:///` ローカルの LDAP にアクセスする
