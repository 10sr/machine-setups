# user ?= $(shell whoami)
user ?= 10sr

gcp_project := praxis-practice-289116

pipenv_run := pipenv run

list-inventory:
	$(pipenv_run) ansible-inventory --list

update-config:
	# gcloud compute config-ssh --remove
	# gcloud compute config-ssh --project $(gcp_project)

setup: update-config
	$(pipenv_run) ansible all -m setup

ping: update-config
	$(pipenv_run) ansible all -m ping

play:
	$(pipenv_run) ansible-playbook ansible.yaml
