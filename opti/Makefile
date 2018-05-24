ssh_config ?= ssh_config
SSH_ARGS := -F ${ssh_config}

pipenv := env PIPENV_VENV_IN_PROJECT=1 pipenv


default: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


check:  ## Run check

.venv:
	${pipenv} install --ignore-pipfile

play: .venv play-opti play-lxc  ## Run play-opti and play-lxc

play-opti: .venv  ## Set up opti (lxc host)
	${pipenv} run ansible-playbook -vv --ssh-common-args='${SSH_ARGS}' --diff opti.yml

play-lxc: transfer-repository  ## Set up lxc containers
	# Any way other than to use sudo ?
	ssh ${SSH_ARGS} -t opti "cd .machine-setups-opti/ && ansible-playbook -vv lxc.yml --diff"

play-lxc-bootstrap: transfer-repository  ## Set up lxc containers (requires sudo password)
	# Any way other than to use sudo ?
	ssh ${SSH_ARGS} -t opti "cd .machine-setups-opti/ && sudo ansible-playbook -vv lxc-bootstrap.yml --diff"

transfer-repository: .venv  ## Transfer this repository to opti
	${pipenv} run ansible -vv --ssh-common-args='${SSH_ARGS}' --diff opti -m synchronize -a "src=./ dest=./.machine-setups-opti/ delete=yes use_ssh_args=yes"


ssh:
	exec ssh ${SSH_ARGS} opti

ssh-l:
	exec ssh ${SSH_ARGS} -L 7180:cm01:7180 opti

facts:
	ansible -m setup conoha

encrypt-all:
	-find vault/ -type f | xargs -n 1 ansible-vault encrypt

decrypt-all:
	-find vault/ -type f | xargs -n 1 ansible-vault decrypt
