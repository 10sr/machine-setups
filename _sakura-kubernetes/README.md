sakura-kubernetes
=================

Kubernetes manifest files for sakura.


    make <manifest_name>


Notes
-----

- ローカルから NodePort にアクセスしようとしたときに localhost でなく 127.0.0.1 を使う必要があるように見える
  - できる `curl 127.0.0.1:30009`
  - できない `curl localhost:30009`
