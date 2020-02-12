manifests_yaml := $(wildcard additionals/*.yaml)
manifests := $(manifests_yaml:%.yaml=%)

all: $(manifests) metrics-server dashboard
.PHONY: $(manifests) metrics-server dashboard

$(manifests):
	kubectl apply -f $@.yaml


metrics-server: metrics-server/deploy/kubernetes/
	kubectl apply -f $^

dashboard: dashboard/aio/deploy/alternative.yaml
	kubectl apply -f $^
	kubectl patch -n kubernetes-dashboard \
		deployment kubernetes-dashboard \
		--patch "$$(cat dashboard-alternative-patch-v2.0.0-rc5.yaml)"
