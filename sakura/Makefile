pipenv := env PIPENV_VENV_IN_PROJECT=1 pipenv

default: help

.PHONY: help check play facts hosts

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

check: ansible-lint  # Run check

.venv:
	${pipenv} install

play: .venv  ## Invoke ansible-playbook
	${pipenv} run ansible-playbook -vv ansible.yml

facts: .venv  ## Show fact
	${pipenv} run ansible -m setup sakura

hosts:
	${pipenv} run ansible all --list-hosts


encrypt_all: .venv  ## Encrypt all files in vault/
	-find vault/ -type f | xargs -n 1 ${pipenv} run ansible-vault encrypt


decrypt_all: .venv  ## Decrypt all files in vault/
	-find vault/ -type f | xargs -n 1 ${pipenv} run ansible-vault decrypt


ansible-lint: .venv  ## Run ansible-lint
	${pipenv} run ansible-lint ansible.yml --nocolor -p
