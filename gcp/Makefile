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

encrypt-all:
	find vault/ -type f | xargs grep -L 'ANSIBLE_VAULT;' | xargs -n 1 ${pipenv_run} ansible-vault encrypt


decrypt-all:
	find vault/ -type f | xargs grep -l 'ANSIBLE_VAULT;' | xargs -n 1 ${pipenv_run} ansible-vault decrypt
