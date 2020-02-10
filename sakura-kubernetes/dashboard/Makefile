manifests_yaml := $(wildcard *.yaml)
manifests := $(manifests_yaml:%.yaml=%)

all: $(manifests)

$(manifests):
	kubectl apply -f $@.yaml
