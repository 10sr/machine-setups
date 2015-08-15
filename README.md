ec2
====


What is This?
------------

自分の持ってる Amazon EC2 のインスタンスを管理するためのレポジトリです。

動かすには、 `ssh ec2` できる必要があります。
現在、 `ubuntu trusty 14.04` を使っています。


Create Machine
-----------

* https://console.aws.amazon.com/ec2 ここからマシンを追加します
* セキュリティグループの設定から、 HTTP ポートを開けます


Usage
-----

Issue

    ansible-playbook ansible.yml

Optionally, when you want to update mydns password:

    ansible-playbook ansible.yml --extra-vars=mydns_password=xxxx



saku
----

よくわかんないけど 8000 番をコンソールから開けないといけない気がします

dokku
-----

デプロイするには、

    cat .ssh/id_rsa.pub |ssh ubuntu@10sr.mydns.jp 'sudo sshcommand acl-add dokku dokkudeploy'

みたいなことをマシン毎にしなきゃいけません。どうにかして自動化したい。


TODO
----


License
-------

Files in this repository are unlicensed unless explicitly specified.
See `LICENSE` for details.
