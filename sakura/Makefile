default:

play:
	ansible-playbook -vv ansible.yml --diff

facts:
	ansible -m setup sakura


encrypt_all:
	-find vault/ -type f | xargs -n 1 ansible-vault encrypt


decrypt_all:
	-find vault/ -type f | xargs -n 1 ansible-vault decrypt
