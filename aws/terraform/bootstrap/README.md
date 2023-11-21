aws-bootstrap
=============

AWS 環境で Terraform を使用するためのブートストラップを行う。


以下を行う。

- Terraform の backend に使用するリソースの作成
- Terraform の実行に使用する IAM role の作成

```shell
terraform init
terraform plan
terraform apply
```




初回設定
--------

初回のみ、 backend に使用する s3 などを作成するために override を使用し local に state を作成する。
その後 migrate-state オプションを使用し state を s3 に移動させる。


```shell
cp -pvf override.tf{_,}
terraform init
terraform plan
terraform apply
rm -f override.tf
# Migrate state file from local to s3
terraform init -migrate-state -force-copy
# Check current state with new backend
terraform plan
# Remove local tfstate file
rm -f terraform.tfstate
```
