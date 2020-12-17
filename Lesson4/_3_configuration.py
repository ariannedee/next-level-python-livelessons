"""
This file requires an argument.

In the terminal:
$ python3 _3_configuration.py <your_name>

In PyCharm:
Edit run configurations to include <your_name> in the parameters
"""
import sys

name = sys.argv[1]

print(f'Hello {name}')
