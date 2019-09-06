roles/kubernetes
================

Prepare Kubernetes service.


Setup
-----

この role は、必要なパッケージのインストールと最低限の設定の配置のみを行う。
この role を流した後、以下のコマンドを実行してサービスを開始させた。


    # Master ノードの構築
    sudo kubeadm init --pod-network-cidr=192.168.0.0/16 --ignore-preflight-errors=Swap

    # ログインユーザに kubectl 実行のための権限を設定
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config

    # ネットワークの設定（ calico を使用）
    kubectl apply -f https://docs.projectcalico.org/v3.8/manifests/calico.yaml

    # 補完設定
    kubectl completion bash | sudo tee /etc/bash_completion.d/kubectl

    # Master ノードから Taint を削除
    # （ Master しか存在しないため行う。別途 Slave が存在するなら不要）
    kubectl taint nodes --all node-role.kubernetes.io/master-

    # Pod 作成テスト
    kubectl create deployment nginx --image=nginx
    kubectl get pod
