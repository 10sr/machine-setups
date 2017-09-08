default:

play: play-opti play-lxc

play-opti:
	ansible-playbook -vv --diff opti.yml

play-lxc:
	ansible -vv --diff opti -m synchronize -a "src=./ dest=./.machine-setups-opti/ delete=yes"
	# Any way other than to use sudo ?
	ssh -t opti "cd .machine-setups-opti/ && sudo ansible-playbook -vv lxc.yml --diff"


facts:
	ansible -m setup conoha


encrypt_all:
	-find vault/ -type f | xargs -n 1 ansible-vault encrypt


decrypt_all:
	-find vault/ -type f | xargs -n 1 ansible-vault decrypt
