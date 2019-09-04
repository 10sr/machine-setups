target := sakura

scp: manifest.yaml
	scp $^ "$(target):"

apply: scp
	ssh -t $(target) kubectl apply -f manifest.yaml
