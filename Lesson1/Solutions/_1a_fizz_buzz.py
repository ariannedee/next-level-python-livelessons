"""
FizzBuzz is a classic programming challenge.

For every number from 1 to n,
print Fizz if the number is divisible by 3,
print Buzz if the number is divisible by 5,
print FizzBuzz if the number is divisible by 3 and 5,
otherwise, print the original number otherwise
"""


# Simple test helper function
def assert_equals(actual, expected):
    assert actual == expected, f'Expected {expected}, got {actual}'


def fizz_buzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return n


assert_equals(fizz_buzz(1), 1)
assert_equals(fizz_buzz(7), 7)
assert_equals(fizz_buzz(3), "Fizz")
assert_equals(fizz_buzz(5), "Buzz")
assert_equals(fizz_buzz(6), "Fizz")
assert_equals(fizz_buzz(10), "Buzz")
assert_equals(fizz_buzz(15), "FizzBuzz")
assert_equals(fizz_buzz(30), "FizzBuzz")

number = int(input("Enter a number: "))

fizz_buzz_list = []
for i in range(number):
    fizz_buzz_list.append(fizz_buzz(i + 1))

print(fizz_buzz_list)
