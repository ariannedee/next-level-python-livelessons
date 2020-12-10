from package.package_module import module_func
from package.subpackage.sub_module import sub_module_func


def func():
    print('_2_init: ' + __name__)


if __name__ == '__main__':
    func()
    module_func()
    sub_module_func()
