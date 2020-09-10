GCP Ansible
===========


Setup Connection
----------------

よくわかってないが、以下を参照すれば良さそう？

- https://cloud.google.com/compute/docs/instances/connecting-advanced?hl=ja

手順としては、以下の２つを行った気がする。

-  Compute Engine > metadata で `enable-oslogin`: `TRUE` を設定する
- `gcloud compute os-login ssh-keys add --key-file .ssh/id_rsa.pub --ttl 0 --project spheric-tea-232305` を実行する
