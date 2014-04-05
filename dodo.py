from doitpy.pyflakes import Pyflakes
from doitpy.coverage import PythonPackage, Coverage


DOIT_CONFIG = {'default_tasks': ['pyflakes']}


def task_pyflakes():
    yield Pyflakes().tasks('**/*.py')

def task_coverage():
    cov = Coverage([PythonPackage('doitsys', test_path='tests')])
    yield cov.all()
    yield cov.src()
    yield cov.by_module()
