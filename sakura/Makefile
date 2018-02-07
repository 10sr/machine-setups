pipenv := env PIPENV_VENV_IN_PROJECT=1 pipenv

default:

.venv:
	${pipenv} install --ignore-pipfile

play: .venv
	${pipenv} run ansible-playbook -vv ansible.yml --diff

facts: .venv
	${pipenv} run ansible -m setup sakura


encrypt_all: .venv
	-find vault/ -type f | xargs -n 1 ${pipenv} run ansible-vault encrypt


decrypt_all: .venv
	-find vault/ -type f | xargs -n 1 ${pipenv} run ansible-vault decrypt
