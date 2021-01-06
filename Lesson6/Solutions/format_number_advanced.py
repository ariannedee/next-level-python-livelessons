"""
Extra practice: handle negative numbers and numbers with decimal places
"""


def format_number(num):
    return _handle_negatives(num)


def _handle_negatives(num):  # Note: function names that start with an underscore make it "semi-private"
    negative = num != abs(num)
    as_string = _handle_decimals(abs(num))
    if negative:
        return '-' + as_string
    return as_string


def _handle_decimals(num):
    number_parts = str(num).split('.')

    as_string = _handle_positive_integer(number_parts[0])

    if len(number_parts) == 2:
        return as_string + '.' + number_parts[1]
    return as_string


def _handle_positive_integer(num):
    as_string = ""
    for i, char in enumerate(str(num)[::-1]):
        if i >= 3 and i % 3 == 0:
            as_string += ','
        as_string += char
    return as_string[::-1]


if __name__ == "__main__":
    def assert_equals(actual, expected):
        assert actual == expected, f"Expected {expected} but got {actual}"

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

    print("All tests passed")
