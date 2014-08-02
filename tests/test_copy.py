from doitsys import copy


class TestCopy(object):
    def test_call(self):
        cp = copy.Copy(sudo=True, options={'p':True})
        task = cp('foo', 'bar')
        assert ['sudo install -D -p foo bar'] == task['actions']
