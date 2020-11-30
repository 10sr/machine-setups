ROOT_DIR := $(CURDIR)

installdeps:
	PIP_USER= pipenv run pip install -r kubespray/requirements.txt
	PIP_USER= pipenv run pip install -r kubespray/contrib/inventory_builder/requirements.txt

inventory/hosts.ini:
	./gen_inventory.sh

cluster: inventory/hosts.ini ssh-config
	cd kubespray/ && pipenv run ansible-playbook -i $(ROOT_DIR)/inventory/hosts.ini --ssh-common-args "-F $(ROOT_DIR)/ssh-config" --become cluster.yml

ssh-config:
	gcloud compute config-ssh --ssh-config-file=$@ --project praxis-practice-289116
