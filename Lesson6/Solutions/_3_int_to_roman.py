def assert_equals(actual, expected):
    assert actual == expected, f'Expected {expected}, got {actual}'


def int_to_roman(i):
    int_to_roman_list = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    roman = ''
    while i > 0:
        for num, letter in int_to_roman_list:
            if i == 0:
                break
            if i >= num:
                roman += letter
                i -= num
                break
    return roman


assert_equals(int_to_roman(1), 'I')
assert_equals(int_to_roman(2), 'II')
assert_equals(int_to_roman(4), 'IV')
assert_equals(int_to_roman(9), 'IX')
assert_equals(int_to_roman(14), 'XIV')
assert_equals(int_to_roman(58), 'LVIII')
assert_equals(int_to_roman(1994), 'MCMXCIV')
