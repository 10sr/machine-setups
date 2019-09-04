target := sakura

manifests_yaml := $(shell find * -name '*.yaml')
manifests := $(manifests_yaml:%.yaml=%)

remote_dir := kubernetes_manifests

scp:
	ssh $(target) mkdir -p $(remote_dir)/
	rsync -av --delete ./ "$(target):$(remote_dir)/"

$(manifests): scp
	ssh -t $(target) kubectl apply -f $(remote_dir)/$@.yaml
