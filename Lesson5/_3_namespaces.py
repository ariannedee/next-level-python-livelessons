"""
There are 4 types of namespaces:
- built-in
- global
- enclosing
- local
"""
import math
from random import *

a = 1

print(f'Built-ins\n{dir(__builtins__)}\n')
print(f'Globals\n{globals()}\n')


def outer_function(b, c):
    def inner_function(d):
        global a
        a = 10
        b = 100  # Creates a new local variable (b) that is destroyed once out of inner_function
        print(f'Inner function locals\n{locals()}\n')

    inner_function(4)
    print(f'a = {a}')
    print(f'Outer function locals\n{locals()}\n')


outer_function(2, 3)
print(f'Main locals\n{locals()}\n')
