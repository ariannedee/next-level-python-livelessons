from package.package_module import module_func
from package.subpackage import sub_module_func


def func():
    print('example 1 modules: ' + __name__)


if __name__ == '__main__':
    func()
    module_func()
    sub_module_func()
