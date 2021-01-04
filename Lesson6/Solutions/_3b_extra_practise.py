"""
Write a function that takes a number and returns it as a string with commas as
the thousands separators

Extra practise: handle negative numbers and numbers with decimal places
"""


def assert_equals(actual, expected):
    assert actual == expected, f'Expected {expected}, got {actual}'


def format_number(num):
    return handle_negatives(num)


def handle_negatives(num):
    negative = num != abs(num)
    as_string = handle_decimals(abs(num))
    if negative:
        return '-' + as_string
    return as_string


def handle_decimals(num):
    number_parts = str(num).split('.')

    as_string = handle_positive_integer(number_parts[0])

    if len(number_parts) == 2:
        return as_string + '.' + number_parts[1]
    return as_string


def handle_positive_integer(num):
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

assert_equals(format_number(-100), '-100')
assert_equals(format_number(-1000000), '-1,000,000')

assert_equals(format_number(1000.123), '1,000.123')
assert_equals(format_number(-100.0), '-100.0')
assert_equals(format_number(-1000000.0001), '-1,000,000.0001')

print('all passed')
