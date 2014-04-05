from doitsys.command import BaseCommand

class Package(BaseCommand):
    cmd_template = 'apt-get {sub_cmd} {opts} {pkg}'
    sudo = True

    def install(self, pkg_name, **cmd_opts):
        opts = self.opt_str(self.options, cmd_opts)

        cmd = self.cmd_template.format(sub_cmd='install', opts=opts,
                                       pkg=pkg_name)
        check_installed = 'dpkg-query -s {} | grep "^Status: install ok installed"'
        return {
            'basename': 'pkg',
            'name': pkg_name,
            'actions': [self.action(cmd)],
            'uptodate': [check_installed.format(pkg_name)]
            }
