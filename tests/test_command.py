
from doitsys import command
from doit.tools import Interactive


class TestBaseCommand_OptStr(object):
    def test_no_value(self):
        assert '' == command.BaseCommand.opt_str()

    def test_single_value(self):
        assert '--name test' == command.BaseCommand.opt_str({'name':'test'})
        assert '-n test' == command.BaseCommand.opt_str({'n':'test'})
        assert '--flag' == command.BaseCommand.opt_str({'flag': None})

    def test_many_values(self):
        opt1 = {'n':'test'}
        opt2 = {'val2':'lala', 'o':None}
        got = command.BaseCommand.opt_str(opt1, opt2)
        assert '-n test' in got
        assert '--val2 lala' in got
        assert '-o' in got


class TestBaseCommand_Init(object):

    class MyCmd(command.BaseCommand):
        sudo = True
        interactive = True
        base_options = {'p1': 'ha'}

    def test_defaults(self):
        cmd = command.BaseCommand()
        assert False == cmd.sudo
        assert False == cmd.interactive
        assert {} == cmd.options

    def test_cvar_defaults(self):
        cmd = self.MyCmd()
        assert True == cmd.sudo
        assert True == cmd.interactive
        assert {'p1': 'ha'} == cmd.options

    def test_set_init(self):
        cmd = self.MyCmd(sudo=False, interactive=True, options={'p2': 'bar'})
        assert False == cmd.sudo
        assert True == cmd.interactive
        assert {'p1': 'ha', 'p2':'bar'} == cmd.options


class TestBaseCommand_Action(object):

    class MyCmd(command.BaseCommand):
        cmd_template = 'foo {options} {target}'
        def __call__(self, target):
            action = self.action(self.cmd_template.format(
                    target=target,
                    options=self.opt_str(self.options),
                    ))
            return {
                'name': target,
                'actions': [action],
                }

    def test_normal(self):
        cmd = self.MyCmd(options={'bar': 'baz'})
        assert 'foo --bar baz tx' == cmd('tx')['actions'][0]

    def test_sudo(self):
        cmd = self.MyCmd(sudo=True, options={'bar': 'baz'})
        assert 'sudo foo --bar baz tx' == cmd('tx')['actions'][0]

    def test_interactive(self):
        cmd = self.MyCmd(interactive=True, options={'bar': 'baz'})
        action = cmd('tx')['actions'][0]
        assert isinstance(action, Interactive)
        assert 'foo --bar baz tx' == action.action


class TestCmd(object):
    def test_cmd(self):
        task = command.cmd('foo -p bar', file_dep=['xxx'])
        assert ['xxx'] == task['file_dep']
        assert ['foo -p bar'] == task['actions']


    def test_interactive(self):
        task = command.interactive('foo -p bar', file_dep=['xxx'])
        assert ['xxx'] == task['file_dep']
        action = task['actions'][0]
        assert 'foo -p bar' == action.action
        assert isinstance(action, Interactive)
