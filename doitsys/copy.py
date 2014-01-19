
from doit.tools import title_with_actions

from .command import Command

class Copy(Command):
    cmd_template = 'install {opts} {source} {dest}'
    base_options = {'D': None} # -D / create all leading folders

    def __call__(self, source, dest, **kwargs):
        """return task dict"""
        opts = self.opt_str(self.options, kwargs)

        cmd = self.cmd_template.format(opts=opts, source=source, dest=dest)
        if self.sudo:
            cmd = 'sudo ' + cmd
        return {
            'name': 'copy-{}'.format(dest),
            'actions': [cmd],
            'file_dep': [source],
            'targets': [dest],
            'title': title_with_actions,
            }

