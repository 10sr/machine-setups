ec2
====

Stuffs to Manage My Amazon EC2 machine


What is This?
------------

自分の持ってる Amazon EC2 のインスタンスを管理するためのレポジトリです。

鍵があれば、 `ssh ubuntu@10sr.mydns.jp` でログインできます。


Create Machine
-----------

* https://console.aws.amazon.com/ec2 ここからマシンを追加します
* セキュリティグループの設定から、 HTTP ポートを開けます


TODO
----

* mydns の IP 通知を cron で回すようにする
  * https://gist.github.com/10sr/6696565
* junks レポジトリからものを持ってきて整理する
  * https://github.com/10sr/junks/tree/master/ec2
