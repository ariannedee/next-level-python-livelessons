"""
This program takes a number and returns it as a string with commas as the
thousands separators

Basic practice: add tests and fix the code to handle positive whole numbers
Extra practice: extend it to handle negative numbers and numbers with decimal places
"""

num = input("Enter a number: ")


as_string = ""
i = 0
for char in str(num):
    if i % 3 == 1:
        as_string += ','
    as_string += char
    i += 1

print(as_string)
