#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Ansible by Red Hat, inc
#
# This file is part of Ansible by Red Hat
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.0'}

DOCUMENTATION = '''
'''

EXAMPLES = '''
'''

RETURN = '''
'''

import os
from ansible.module_utils.basic import AnsibleModule


class _TaskFailedException(Exception):
    def __init__(self, msg, **kargs):
        self.msg = msg
        self.kargs = kargs
        return


class _Pm2(object):
    # application info
    info_raw = None
    pm_id = -1
    pid = -1
    # None if app is not registered to pm2
    pm2_status = None

    def __init__(self, module, name, pm2_executable):
        self.module = module
        self.name = name
        if pm2_executable is None:
            self.pm2_executable = module.get_bin_path("pm2", required=True)
        else:
            self.pm2_executable = pm2_executable

        self._run_pm2(["--version"], check_rc=True)
        self._update_info()
        return

    def start(self, target, chdir=None):
        assert target is not None
        if chdir is None:
            target = os.path.abspath(target)
            chdir = os.path.dirname(target)
        rc, out, err = self._run_pm2(["start", target, "--name", self.name],
                                     check_rc=True, cwd=chdir)
        self._update_info()
        return {
            "rc": rc,
            "stdout": out,
            "stderr": err
        }

    def stop(self):
        rc, out, err = self._run_pm2(["stop", self.name],
                                     check_rc=True)
        self._update_info()
        return {
            "rc": rc,
            "stdout": out,
            "stderr": err
        }

    def delete(self):
        rc, out, err = self._run_pm2(["delete", self.name],
                                     check_rc=True)
        self._update_info()
        return {
            "rc": rc,
            "stdout": out,
            "stderr": err
        }

    def restart(self, target=None, chdir=None):
        if target is None:
            rc, out, err = self._run_pm2(["restart", self.name],
                                         check_rc=True)
            self._update_info()
            return {
                "rc": rc,
                "stdout": out,
                "stderr": err
            }
        if chdir is None:
            target = os.path.abspath(target)
            chdir = os.path.dirname(target)
        rc, out, err = self._run_pm2(["restart", target, "--name", self.name],
                                     check_rc=True, cwd=chdir)
        self._update_info()
        return {
            "rc": rc,
            "stdout": out,
            "stderr": err
        }

    def reload(self, config, chdir=None):
        assert config is not None
        if chdir is None:
            config = os.path.abspath(config)
            chdir = os.path.dirname(config)
        rc, out, err = self._run_pm2(["startOrReload", config,
                                      "--name", self.name],
                                     check_rc=True, cwd=chdir)
        self._update_info()
        return {
            "rc": rc,
            "stdout": out,
            "stderr": err
        }

    def is_started(self):
        return self.pm2_status == "online"

    def exists(self):
        return self.pm2_status is not None

    def _run_pm2(self, args, check_rc=False, cwd=None):
        return self.module.run_command(args=([self.pm2_executable] + args),
                                       check_rc=check_rc, cwd=cwd)

    def _update_info(self):
        self.info_raw = None
        self.pm_id = -1
        self.pid = -1
        self.pm2_status = None

        rc, out, err = self._run_pm2(["jlist"], check_rc=True)
        try:
            apps = self.module.from_json(out)
        except ValueError as e:
            raise _TaskFailedException(rc=1, msg=e.args[0])
        try:
            for app in apps:
                if app["name"] == self.name:
                    self.info_raw = app
                    break
        except KeyError:
            raise _TaskFailedException(
                msg="Unexpected pm2 jlist output format: {}".format(out)
            )

        if self.info_raw is None:
            # app is not registered
            return

        try:
            self.pm_id = self.info_raw["pm_id"]
            self.pid = self.info_raw["pid"]
            self.pm2_status = self.info_raw["pm2_env"]["status"]
        except KeyError:
            raise _TaskFailedException(
                msg="Unexpected pm2 jlist output: {}".format(self.info_raw)
            )
        return


def do_pm2(module, name, config, script, state, chdir, executable):
    result = {}
    pm2 = _Pm2(module, name, executable)

    if state == "started":
        target = config or script
        if target is None:
            raise _TaskFailedException(
                msg="Neigher CONFIG nor SCRIPT is given for start command"
            )
        if pm2.is_started():
            result.update(
                chagned=False,
                msg="{} already started".format(name)
            )
        else:
            if not module.check_mode:
                cmd_result = pm2.start(target=target, chdir=chdir)
                result.update(cmd_result)
            result.update(
                changed=True,
                msg="Started {}".format(name)
            )

    elif state == "stopped":
        if not pm2.is_started():
            result.update(
                changed=False,
                msg="{} already stopped/absent".format(name)
            )
        else:
            if not module.check_mode:
                cmd_result = pm2.stop()
                result.update(cmd_result)
            result.update(
                changed=True,
                msg="Stopped {}".format(name)
            )

    elif state == "restarted":
        target = config or script
        if not module.check_mode:
            cmd_result = pm2.restart(target=target, chdir=chdir)
            result.update(cmd_result)
        result.update(
            chagned=True,
            msg="Restarted {}".format(name)
        )

    elif state == "reloaded":
        if config is None:
            raise _TaskFailedException(
                msg="CONFIG is not given for reload command"
            )
        if not module.check_mode:
            cmd_result = pm2.reload(config=config, chdir=chdir)
            result.update(cmd_result)
        result.update(
            chagned=True,
            msg="Reloaded {}".format(name)
        )

    elif state == "absent" or state == "deleted":
        if not pm2.exists():
            result.update(
                changed=False,
                msg="{} not exists".format(name)
            )
        else:
            if not module.check_mode:
                cmd_result = pm2.delete()
                result.update(cmd_result)
            result.update(
                changed=True,
                msg="Deleted {}".format(name)
            )

    else:
        raise _TaskFailedException(msg="Unknown state: {]".format(state))

    result.update(
        pm_id=pm2.pm_id,
        pid=pm2.pid,
        pm2_status=pm2.pm2_status
    )

    return result


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            state=dict(choices=['started',
                                'stopped',
                                'restarted',
                                'reloaded',
                                'absent', 'deleted'],
                       default='started'),
            config=dict(type='path'),
            script=dict(type='path'),
            executable=dict(type='path'),
            chdir=dict(type='path')
        ),
        supports_check_mode=True,
        mutually_exclusive=[['config', 'script']],
    )

    try:
        result = do_pm2(
            name=module.params['name'],
            state=module.params['state'],
            module=module,
            config=module.params['config'],
            script=module.params['script'],
            executable=module.params['executable'],
            chdir=module.params['chdir']
        )

    except _TaskFailedException as e:
        module.fail_json(
            failed=True,
            msg=e.msg,
            **e.kargs
        )
        return

    module.exit_json(
        failed=False,
        **result
    )
    return


if __name__ == '__main__':
    main()
