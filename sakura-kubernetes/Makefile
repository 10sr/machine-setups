target := sakura

manifests_yaml := $(shell find * -name '*.yaml')
manifests := $(manifests_yaml:%.yaml=%)

remote_dir := kubernetes_manifests

scp:
	ssh $(target) mkdir -p $(remote_dir)/
	scp -rv * "$(target):$(remote_dir)/"
	echo $(manifests)

$(manifests): scp
	ssh -t $(target) kubectl apply -f $(remote_dir)/$@.yaml
