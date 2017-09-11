default: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


play: play-opti play-lxc  ## Run play-opti and play-lxc

play-opti:  ## Set up opti (lxc host)
	ansible-playbook -vv --diff opti.yml

play-lxc-bootstrap: transfer-repository  ## Set up lxc containers (requires sudo password)
	# Any way other than to use sudo ?
	ssh -t opti "cd .machine-setups-opti/ && sudo ansible-playbook -vv lxc-bootstrap.yml --diff"

transfer-repository:  ## Transfer this repository to opti
	ansible -vv --diff opti -m synchronize -a "src=./ dest=./.machine-setups-opti/ delete=yes"


facts:
	ansible -m setup conoha

encrypt-all:
	-find vault/ -type f | xargs -n 1 ansible-vault encrypt

decrypt-all:
	-find vault/ -type f | xargs -n 1 ansible-vault decrypt
