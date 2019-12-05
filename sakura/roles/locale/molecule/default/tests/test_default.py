import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_locale(host):
    ansible_vars = host.ansible.get_variables()
    locale_default = ansible_vars["locale_default"]

    f = host.file('/etc/default/locale')
    lines = f.content_string.split("\n")

    assert 'LANG={}'.format(locale_default) in lines
    return
