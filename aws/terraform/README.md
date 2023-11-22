aws/terraform
=============

事前準備
--------


`bootstrap/` を通すために、まず AdministratorAccess のついたユーザを用意する。
今回は IAM Identity Center を使用して用意した。

- https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html

設定した認証方法を `8-admin` という名前のプロファイルで保存する。
