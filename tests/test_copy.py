from doitsys import copy


class TestCopy(object):
    def test_call(self):
        cp = copy.Copy(sudo=True, options={'p':None})
        task = cp('foo', 'bar')
        assert ['sudo install -p -D foo bar'] == task['actions']
