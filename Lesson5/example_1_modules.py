from package.package_module import package_module_func
from package.subpackage import sub_module_func


def func():
    print('example 1 modules: ' + __name__)


if __name__ == '__main__':
    import sys
    print(sys.path)  # Python searches for modules here (in-order)

    func()
    package_module_func()
    sub_module_func()
