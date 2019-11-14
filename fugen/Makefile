pipenv := env PIPENV_VENV_IN_PROJECT=1 pipenv

default: help

.PHONY: help check play facts hosts install check-ansible-version

help:
	@echo fugen ansible | (figlet || cat) | (lolcat || cat)
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


THIS_REVISION_ID := $(shell git describe --all --always --long --dirty)
THIS_REVISION_TIMESTAMP := $(shell git log --pretty=tformat:%ct -n1)
THIS_REVISION_SUBJECT := $(shell git log --pretty=tformat:%s -n1)
env_this_revision := \
	THIS_REVISION_ID=$(THIS_REVISION_ID) \
	THIS_REVISION_TIMESTAMP=$(THIS_REVISION_TIMESTAMP) \
	THIS_REVISION_SUBJECT='$(THIS_REVISION_SUBJECT)'  # FIXME: This will fail if SUBJECT has quotes


ANSIBLE_INSTALLED_VERSION := $(shell $(pipenv) run ansible --version | awk '/^ansible/ {print $$2 }')


check: ansible-lint  ## Run check

.venv:
	${pipenv} install

install:  ## Install depending packages
	${pipenv} install

play: .venv check-ansible-version  ## Invoke ansible-playbook
	${pipenv} run env $(env_this_revision) ansible-playbook -vv ansible.yaml

facts: .venv  ## Show fact
	${pipenv} run ansible -m setup default

hosts:
	${pipenv} run ansible all --list-hosts


encrypt-all: .venv  ## Encrypt all files in vault/
	find vault/ -type f | xargs grep -L 'ANSIBLE_VAULT;' | xargs -n 1 ${pipenv} run ansible-vault encrypt


decrypt-all: .venv  ## Decrypt all files in vault/
	find vault/ -type f | xargs grep -l 'ANSIBLE_VAULT;' | xargs -n 1 ${pipenv} run ansible-vault decrypt


ansible-lint: .venv  ## Run ansible-lint
	${pipenv} run ansible-lint ansible.yaml --nocolor -p

check-ansible-version:
	grep '^ansible = "==$(ANSIBLE_INSTALLED_VERSION)"$$' Pipfile
