# user ?= $(shell whoami)
user ?= usr_8_slashes_gmail_com
# # What should this be?
# # How are public keys managed in compute engine machines?
# private_key ?= $(HOME)/.ssh/google_compute_engine

gcp_project := spheric-tea-232305

pipenv_run := pipenv run

list-inventory:
	$(pipenv_run) ansible-inventory --list

update-config:
	# gcloud compute config-ssh --remove
	# gcloud compute config-ssh --project $(gcp_project)

setup: update-config
	# $(pipenv_run) ansible --user $(user) --private-key $(private_key) all -m setup
	$(pipenv_run) ansible --user $(user) all -m setup
	# $(pipenv_run) ansible all -m setup

ping: update-config
	# $(pipenv_run) ansible --user $(user) --private-key $(private_key) all -m ping
	# $(pipenv_run) ansible --private-key $(private_key) all -m ping
	$(pipenv_run) ansible --user $(user) all -m ping
	# $(pipenv_run) ansible all -m ping

play:
	$(pipenv_run) ansible-playbook --user $(user) ansible.yaml
