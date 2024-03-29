tags ?= all

pipenv := env PIPENV_VENV_IN_PROJECT=1 pipenv

default: help

.PHONY: help check play facts hosts install check-ansible-version

help:
	@echo sakura ansible | (figlet || cat) | (lolcat || cat)
	@awk 'BEGIN {FS = ":.*?## "}; /^[a-zA-Z_-]+:.*?##/{printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)


THIS_REVISION_ID := $(shell git describe --all --always --long --dirty)
THIS_REVISION_TIMESTAMP := $(shell git log --pretty=tformat:%ct -n1)
THIS_REVISION_SUBJECT := $(shell git log --pretty=tformat:%s -n1)
env_this_revision := \
	THIS_REVISION_ID=$(THIS_REVISION_ID) \
	THIS_REVISION_TIMESTAMP=$(THIS_REVISION_TIMESTAMP) \
	THIS_REVISION_SUBJECT='$(THIS_REVISION_SUBJECT)'  # FIXME: This will fail if SUBJECT has quotes


check: ansible-lint  ## Run check

.venv:
	${pipenv} install

install:  ## Install depending packages
	${pipenv} install

install-dev:
	${pipenv} install --dev

play: .venv check-ansible-version  ## Invoke ansible-playbook
	${pipenv} run env $(env_this_revision) ansible-playbook -vv ansible.yaml --tags $(tags)

facts: .venv  ## Show fact
	${pipenv} run ansible -m setup sakura

hosts:
	${pipenv} run ansible all --list-hosts


encrypt-all: .venv  ## Encrypt all files in vault/
	find vault/ -type f | xargs grep -L 'ANSIBLE_VAULT;' | xargs -n 1 ${pipenv} run ansible-vault encrypt


decrypt-all: .venv  ## Decrypt all files in vault/
	find vault/ -type f | xargs grep -l 'ANSIBLE_VAULT;' | xargs -n 1 ${pipenv} run ansible-vault decrypt


ansible-lint: .venv  ## Run ansible-lint
	${pipenv} run ansible-lint ansible.yaml --nocolor -p

check-ansible-version:
	PIP_USER= ${pipenv} run python3 ./check_ansible_version.py


# Molecule

molecule_role_targets := locale sosreport

molecule-test:  ## Run molecule role tests
	set -eux; for role in $(molecule_role_targets); do (cd roles/$$role && ${pipenv} run molecule test); done
