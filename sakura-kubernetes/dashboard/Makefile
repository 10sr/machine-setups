manifests_yaml := $(wildcard *.yaml)
manifests := $(manifests_yaml:%.yaml=%)

all: $(manifests) metrics-server # dashboard
.PHONY: $(manifests) metrics-server dashboard

$(manifests):
	kubectl apply -f $@.yaml


metrics-server: metrics-server/deploy/1.8+
	kubectl apply -f $^

dashboard: dashboard/aio/deploy/alternative.yaml
	kubectl apply -f $^
