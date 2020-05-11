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
