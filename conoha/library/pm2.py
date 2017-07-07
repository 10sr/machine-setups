#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, 10sr <8.slashes () gmail.com>
#
# This file is not part of Ansible
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

import os
from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.0'}


class _TaskFailedException(Exception):
    def __init__(self, rc, msg):
        self.rc = rc
        self.msg = msg
        return


class _Pm2(object):
    def __init__(self, module, name, pm2_executable):
        self.module = module
        self.name = name
        if pm2_executable is None:
            self.pm2_executable = module.get_bin_path("pm2", required=True)
        else:
            self.pm2_executable = pm2_executable

        rc, out, err = self._run_pm2(["-v"])
        if rc != 0:
            # raise _TaskFailedException(rc=rc, msg=err.strip())
            raise _TaskFailedException(rc=rc, msg=out.strip())

        return

    def start(self, target, chdir=None):
        if chdir is None:
            target = os.path.abspath(target)
            chdir = os.path.dirname(target)
        rc, out, err = self._run_pm2(["start", target, "--name", self.name],
                                     check_rc=True, cwd=chdir)
        return {
            "stdout": out,
            "stderr": err
        }

    def stop(self):
        rc, out, err = self._run_pm2(["stop", self.name],
                                     check_rc=True)
        return {
            "stdout": out,
            "stderr": err
        }

    def delete(self):
        rc, out, err = self._run_pm2(["delete", self.name],
                                     check_rc=True)
        return {
            "stdout": out,
            "stderr": err
        }

    def restart(self, target=None, chdir=None):
        if target is None:
            rc, out, err = self._run_pm2(["restart", self.name],
                                         check_rc=True)
            return {
                "stdout": out,
                "stderr": err
            }
        if chdir is None:
            target = os.path.abspath(target)
            chdir = os.path.dirname(target)
        rc, out, err = self._run_pm2(["restart", target, "--name", self.name],
                                     check_rc=True, cwd=chdir)
        return {
            "stdout": out,
            "stderr": err
        }

    def reload(self, config=None, chdir=None):
        if config is None:
            raise _TaskFailedException(
                rc=1,
                msg="config args is given for reload command"
            )
        if chdir is None:
            config = os.path.abspath(config)
            chdir = os.path.dirname(config)
        rc, out, err = self._run_pm2(["startOrReload", config, "--name", self.name],
                                     check_rc=True, cwd=chdir)
        return {
            "stdout": out,
            "stderr": err
        }

    def is_started(self):
        status = self.get_status()
        return status is not None and status == "online"

    def exists(self):
        return self.get_status() is not None

    def get_status(self):
        rc, out, err = self._run_pm2(["jlist"], check_rc=True)
        try:
            apps = self.module.from_json(out)
        except ValueError as e:
            raise _TaskFailedException(rc=1, msg=e.args[0])
        try:
            for app in apps:
                if app["name"] == self.name:
                    return app["pm2_env"]["status"]
        except KeyError as e:
            raise _TaskFailedException(
                rc=1,
                msg="Unexpected pm2 jlist output: {}".format(out)
            )
        return None

    def _run_pm2(self, args, check_rc=False, cwd=None):
        return self.module.run_command(args=([self.pm2_executable] + args),
                                       check_rc=check_rc, cwd=cwd)


def do_pm2(module, name, config, script, state, chdir, executable):
    pm2 = _Pm2(module, name, executable)
    if state == "running" or state == "started":
        if pm2.is_started():
            return {
                "changed": False,
                "msg": "{} already started".format(name)
            }
        target = config or script
        if target is None:
            raise _TaskFailedException(
                rc=1,
                msg="Neigher config nor script args is given for start command"
            )
        result = pm2.start(target=target, chdir=chdir)
        return dict(result,
                    changed=True,
                    msg="Started {}".format(name))
    elif state == "stopped":
        if pm2.is_started():
            result = pm2.stop()
            return dict(result,
                        changed=True,
                        msg="Stopped {}".format(name))
        return {
            "changed": False,
            "msg": "{} already stopped/absent".format(name)
        }
    elif state == "restarted":
        target = config or script
        result = pm2.restart(target=target, chdir=chdir)
        return dict(result,
                    changed=True,
                    msg="Restarted {}".format(name))
    elif state == "reloaded":
        result = pm2.reload(config=config, chdir=chdir)
        return dict(result,
                    changed=True,
                    msg="Reloaded {}".format(name))
    elif state == "absent" or state == "deleted":
        if pm2.exists():
            result = pm2.delete()
            return dict(result,
                        changed=True,
                        msg="Deleted {}".format(name))
        return {
            "changed": False,
            "msg": "{} not exists".format(name)
        }
    raise _TaskFailedException(msg="Unknown state: {]".format(state), rc=1)


def main():
    module = AnsibleModule(
        argument_spec=dict(
            config=dict(type='path'),
            script=dict(type='path'),
            executable=dict(type='path'),
            chdir=dict(type='path'),
            state=dict(choices=['running', 'started',
                                'stopped',
                                'restarted', 'reloaded',
                                'absent', 'deleted']),
            name=dict(required=True)
        ),
        supports_check_mode=True,
        mutually_exclusive=[['config', 'script']],
    )

    try:
        result = do_pm2(
            module=module,
            config=module.params['config'],
            script=module.params['script'],
            executable=module.params['executable'],
            chdir=module.params['chdir'],
            state=module.params['state'],
            name=module.params['name']
        )

    except _TaskFailedException as e:
        module.fail_json(
            rc=e.rc,
            msg=e.msg
        )
        return

    module.exit_json(
        rc=0,
        failed=False,
        **result
    )
    return


if __name__ == '__main__':
    main()
