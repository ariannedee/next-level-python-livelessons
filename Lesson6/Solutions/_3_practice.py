"""
This program takes a number and returns it as a string with commas as the
thousands separators

Basic practice: add tests and fix the code to handle positive whole numbers
Extra practice: extend it to handle negative numbers and numbers with decimal places
"""
from format_number import format_number


user_num = input("Enter a number: ")
print(format_number(user_num))
