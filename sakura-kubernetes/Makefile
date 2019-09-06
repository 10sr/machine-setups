target := sakura

manifests_yaml := $(shell find * -name '*.yaml')
manifests := $(manifests_yaml:%.yaml=%)

remote_dir := kubernetes_manifests

scp:
	ssh $(target) mkdir -p $(remote_dir)/
	rsync -av --delete ./ "$(target):$(remote_dir)/"

$(manifests): scp
	ssh -t $(target) kubectl apply -f $(remote_dir)/$@.yaml


uname := $(shell uname)

installdeps: kubeval/kubeval:

kubeval/kubeval:
	mkdir -p kubeval
	wget https://github.com/instrumenta/kubeval/releases/download/0.9.2/kubeval-$(uname)-amd64.tar.gz -O kubeval/kubeval.tgz
	cd kubeval && tar -vxf kubeval.tgz


check: kubeval/kubeval
	./kubeval/kubeval $(manifests_yaml)
