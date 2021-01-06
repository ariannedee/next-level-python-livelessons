def format_number(num):
    as_string = ""
    i = 0
    for char in str(num):
        if i % 3 == 1:
            as_string += ','
        as_string += char
        i += 1
    return as_string


if __name__ == "__main__":
    def assert_equals(actual, expected):
        assert actual == expected, f"Expected {expected} but got {actual}"


    assert_equals(format_number(1), "1")
    assert_equals(format_number(100), "100")
    assert_equals(format_number(1000), "1,000")
    assert_equals(format_number(10000), "10,000")
    assert_equals(format_number(1000000), "1,000,000")
    assert_equals(format_number(100000000), "100,000,000")

    print("All tests passed")
