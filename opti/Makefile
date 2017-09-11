default:

play: play-opti play-lxc

play-opti:
	ansible-playbook -vv --diff opti.yml

play-lxc-bootstrap: transfer-repository
	# Any way other than to use sudo ?
	ssh -t opti "cd .machine-setups-opti/ && sudo ansible-playbook -vv lxc-bootstrap.yml --diff"

transfer-repository:
	ansible -vv --diff opti -m synchronize -a "src=./ dest=./.machine-setups-opti/ delete=yes"


facts:
	ansible -m setup conoha

encrypt-all:
	-find vault/ -type f | xargs -n 1 ansible-vault encrypt

decrypt-all:
	-find vault/ -type f | xargs -n 1 ansible-vault decrypt
