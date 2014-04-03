
from doitsys import command


class TestBaseCommandOptStr(object):
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
