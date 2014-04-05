from .command import BaseCommand

class SSH(BaseCommand):
    cmd_template = 'ssh {opts} {user}@{host} {cmd}'

    def __init__(self, host, user, sudo=False, interactive=None, options=None):
        super(SSH, self).__init__(sudo=sudo, options=options,
                                  interactive=interactive)
        self.host = host
        self.user = user

    def __call__(self, remote_cmd, **kwargs):
        """return task dict"""
        opts = self.opt_str(self.options, kwargs)
        cmd = self.cmd_template.format(opts=opts, host=self.host,
                                       user=self.user, cmd=remote_cmd)
        task = {
            'name': cmd,
            'actions': [self.action(cmd)]
            }
        return task

