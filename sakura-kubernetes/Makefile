target := sakura

manifests_yaml := $(shell find * -name '*.yaml')
manifests := $(manifests_yaml:%.yaml=%)

remote_dir := kubernetes_manifests

scp:
	ssh $(target) mkdir -p $(remote_dir)/
	rsync -av --delete ./ "$(target):$(remote_dir)/"

decrypt_remote: scp
	ssh -t $(target) make -C $(remote_dir) decrypt_secrets

$(manifests): scp
	ssh -t $(target) kubectl apply -f $(remote_dir)/$@.yaml

kexample: scp
	ssh -t $(target) kubectl apply -k $(remote_dir)/$@

exposed.webtools: scp decrypt_remote
	ssh -t $(target) kubectl apply -k $(remote_dir)/$@


uname := $(shell uname)

installdeps: .kubeval/kubeval

.kubeval/kubeval:
	mkdir -p .kubeval
	wget https://github.com/instrumenta/kubeval/releases/download/0.9.2/kubeval-$(uname)-amd64.tar.gz -O .kubeval/kubeval.tgz
	cd .kubeval && tar -vxf kubeval.tgz


check: # check-kubeval

check-kubeval: .kubeval/kubeval
	./.kubeval/kubeval $(manifests_yaml)


GPG_KEYID := AD4550BFA479ED8068A4E7BD3A20F06288D2DD34

encrypt_targets := $(shell find */secrets -type f '!' -name '*.asc')
encrypt_dest := $(encrypt_targets:%=%.asc)

encrypt_secrets: $(encrypt_dest)

$(encrypt_dest): %.asc: %
	gpg2 --recipient $(GPG_KEYID) --armor --encrypt $^



decrypt_targets := $(shell find */secrets -type f -name '*.asc')
decrypt_dest := $(decrypt_targets:%.asc=%)

decrypt_secrets:
	echo $(decrypt_dest)

decrypt_secrets: $(decrypt_dest)

$(decrypt_dest):
	gpg2 --output $@ --decrypt $@.asc
