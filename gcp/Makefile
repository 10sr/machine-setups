gcp_project := praxis-practice-289116

pipenv_run := pipenv run

list-inventory:
	$(pipenv_run) ansible-inventory --list

setup:
	$(pipenv_run) ansible all -m setup

ping:
	$(pipenv_run) ansible all -m ping

play:
	$(pipenv_run) ansible-playbook -vv ansible.yaml
