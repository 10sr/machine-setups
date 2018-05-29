Amazon EC2 provisioning
======================


Vagrant (Virtualbox)
-----------------

Setup vboxdrv (`sudo /etc/init.d/vboxdrv setup`) fails with error
`(Running VirtualBox in a Xen environment is not supported)`.

It seems that VirtualBox wont run insice Amazon EC2 (google `ec2 virtualbox`).


LXC
----

* To create container, `lxc-create -n c0 -t centos`.
* To destroy (stopped) container, `lxc-destroy -n c0`.
