opti
====

Ansible playbook for my opti machine.


Pre configurations
------------------

* Add normal user: `adduser NAME`
  * Add `.ssh/authorized_keys` file for the user
  * Add the user to `sudo` group: `gpasswd -a NAME sudo`


Usage
-----


Add `vault_pass.secret` with the vault password in it and issue:

```
make play

```
