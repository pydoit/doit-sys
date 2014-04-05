from doitsys import ssh


class TestSSH(object):
    def test_call(self):
        conn = ssh.SSH('s1.example.com', 'john')
        task = conn('uname')
        assert ['ssh  john@s1.example.com uname'] == task['actions']
