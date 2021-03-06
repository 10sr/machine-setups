target := k8s-master02

kustomize_targets := exposed.webtools

manifests_yaml := $(wildcard *.yaml)
manifests := $(manifests_yaml:%.yaml=%)

remote_dir := kubernetes_manifests

ssh := gcloud --project "praxis-practice-289116" beta compute ssh --zone "asia-northeast1-b" $(target) --
scp := gcloud --project "praxis-practice-289116" beta compute scp --zone "asia-northeast1-b"
kubectl := sudo kubectl

scp:
	$(ssh) mkdir -p $(remote_dir)/
	$(scp) --recurse "$(CURDIR)"/* "$(target):$(remote_dir)/"

decrypt-remote: scp
	$(ssh) -t make -C $(remote_dir) decrypt-secrets

$(manifests): scp
	$(ssh) -t $(kubectl) apply -f $(remote_dir)/$@.yaml

$(kustomize_targets): scp decrypt-remote
	$(ssh) -t $(kubectl) apply --kustomize $(remote_dir)/$@


uname := $(shell uname)

installdeps: .kubeval/kubeval

.kubeval/kubeval:
	mkdir -p .kubeval
	wget https://github.com/instrumenta/kubeval/releases/download/0.9.2/kubeval-$(uname)-amd64.tar.gz -O .kubeval/kubeval.tgz
	cd .kubeval && tar -vxf kubeval.tgz


check: # check-kubeval

check-kubeval: .kubeval/kubeval
	./.kubeval/kubeval $(manifests_yaml)


GPG_KEYS := 62AC0DD763376B69D3D2C2A6F9E23285A57E4750
#   B88675283D2C1119B42ABA9E19C1680735DE33FB \
#   EE30A1A1AF0E0A44B07D5346E6CF633A3945E1B0 \
#   192EAF31F20AC91E846CD712FAA457DB43F334D6

gpg_recipient_args := $(GPG_KEYS:%=--recipient %)

encrypt_targets := $(shell find */secrets -type f '!' -name '*.asc')
encrypt_dest := $(encrypt_targets:%=%.asc)

encrypt-secrets: $(encrypt_dest)

$(encrypt_dest): %.asc: %
	gpg2 $(gpg_recipient_args) --armor --encrypt $^



decrypt_targets := $(shell find */secrets -type f -name '*.asc')
decrypt_dest := $(decrypt_targets:%.asc=%)

decrypt-secrets: $(decrypt_dest)

$(decrypt_dest):
	gpg2 --output $@ --decrypt $@.asc


mk-hostpath-dir:
	$(ssh) sudo mkdir -p /var/lib/data/kubernetes-hostpath/exposed.webtools/minio/export
	$(ssh) sudo mkdir -p /var/lib/data/kubernetes-hostpath/exposed.webtools/minio/config


# ###########
# # Dashboard

# dashboard: scp
# 	ssh -t $(target) make -C $(remote_dir)/dashboard
