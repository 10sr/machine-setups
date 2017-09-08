default:

play: play-opti play-lxc

play-opti:
	ansible-playbook -vv opti.yml --diff

play-lxc:
	ssh opti "cd .machine-setups-opti/ && ansible-playbook --help"


facts:
	ansible -m setup conoha


encrypt_all:
	-find vault/ -type f | xargs -n 1 ansible-vault encrypt


decrypt_all:
	-find vault/ -type f | xargs -n 1 ansible-vault decrypt
