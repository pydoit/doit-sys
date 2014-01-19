

class Command(object):
    """abstract base class to create tasks that execute a shell command"""
    base_options = {}
    cmd_template = None

    def __init__(self, sudo=False, options=None):
        self.sudo = sudo
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


