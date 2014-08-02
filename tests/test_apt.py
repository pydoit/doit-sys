from doitsys import apt


class TestPackage(object):
    def test_install(self):
        pkg = apt.Package(options={'yes':True})
        task = pkg.install('foo')
        assert ['sudo apt-get install --yes foo'] == task['actions']
