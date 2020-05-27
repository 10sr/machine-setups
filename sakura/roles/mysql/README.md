mysql role
==========

- サービス起動後、 `mysql_secure_installation` を実行すること
- `root@localhost` には unix_socket 認証というのが設定されており、例えパスワードが合っていても root ユーザ以外はログインできない（一般ユーザが `$ mysql -u root -p` を実行してもログインできない）という **気の狂った** 状態になっていることに注意すること
  - しかもエラーメッセージを見てもそうとわからない
  - https://duckduckgo.com/?q=mariadb+root+login+unix_socket&t=ffab&ia=web
