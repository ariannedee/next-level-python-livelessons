"""
Write a function that takes a number and returns it as a string with commas as
the thousands separators

Basic practise: handle only positive whole numbers
"""


def assert_equals(actual, expected):
    assert actual == expected, f'Expected {expected}, got {actual}'


def format_number(num):
    formatted_str = ''
    for i, char in enumerate(str(num)[::-1]):
        if i >= 3 and i % 3 == 0:
            formatted_str += ','
        formatted_str += char
    return formatted_str[::-1]


assert_equals(format_number(10), '10')
assert_equals(format_number(100), '100')
assert_equals(format_number(1000), '1,000')
assert_equals(format_number(100000), '100,000')
assert_equals(format_number(1000000), '1,000,000')

print('all passed')
