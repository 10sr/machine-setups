#!/usr/bin/env python3

# https://mawatari.jp/archives/notify-the-result-of-ansible
# https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html#callback-plugins

from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    def playbook_on_stats(self, stats):
        print(stats)
        return
