gcp-k8s
=======


GPG Key
=======

Generate key:

    [k8s-master02] $ gpg --gen-key


Import key:

    gcloud compute ssh k8s-master02 -- gpg --export --armor 62AC0DD763376B69D3D2C2A6F9E23285A57E4750 \
        | gpg --import
