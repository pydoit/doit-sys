from doit.tools import Interactive

class BaseCommand(object):
    """base class to create tasks that execute a shell command"""
    base_options = {}
    cmd_template = None
    sudo = False
    interactive = False


    def __init__(self, sudo=None, interactive=None, options=None):
        if sudo is not None:
            self.sudo = sudo
        if interactive is not None:
            self.interactive = interactive
        self.options = {}
        self.options.update(self.base_options)
        if options:
            self.options.update(options)


    @staticmethod
    def opt_str(*opt_list):
        """return string with formatted options
        @param opt_list: list of dict with paramenter options
        If value is None it is an option flag
        """
        options = opt_list[0] if opt_list else {}
        for opt_dict in opt_list[1:]:
            options.update(opt_dict)

        parts = []
        for name, val in options.items():
            dashes = '-' if len(name) == 1 else '--'
            opt_val = ' {}'.format(val) if val is not None else ''
            parts.append(dashes + name + opt_val)
        return ' '.join(parts)


    def _action(self, cmd_str):
        """modify action adding sudo / Interactive"""
        if self.sudo:
            cmd_str = 'sudo ' + cmd_str
        if self.interactive:
            return Interactive(cmd_str)
        else:
            return cmd_str


    def __call__(self):
        raise NotImplementedError()


def cmd(cmd_str, **task_params):
    """short-cut to execute a simple command"""
    _cmd = BaseCommand()
    task = {
        'name': cmd_str,
        'actions': [_cmd._action(cmd_str)],
        }
    task.update(task_params)
    return task


def interactive(cmd_str, **task_params):
    """short-cut to execute a simple command interactively"""
    _cmd = BaseCommand(interactive=True)
    task = {
        'name': cmd_str,
        'actions': [_cmd._action(cmd_str)],
        }
    task.update(task_params)
    return task
