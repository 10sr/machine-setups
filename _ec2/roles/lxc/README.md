Role - lxc
===========

Role to setup LXC with unprivileged container configurations.


Example
-------

```
- hosts: all
  roles:
    - role: lxc
      lxc_user: "{{ansible_user_id}}"
      lxc_user_dir: "{{ansible_user_dir}}"
      lxc_virbr_name: lxcbr0
      lxc_nic_num: 10
      lxc_subuid_start: 100000
      lxc_subuid_range: 65536
      lxc_subgid_start: 100000
      lxc_subgid_range: 65536
```
