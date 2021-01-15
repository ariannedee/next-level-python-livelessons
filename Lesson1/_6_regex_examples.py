"""
General regex tutorial: https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285
Python: https://www.w3schools.com/python/python_regex.asp
PyCharm: https://www.jetbrains.com/help/pycharm/regular-expression-syntax-reference.html
"""
import re


assert re.search(r"world", "Hello world")  # Search looks anywhere inside the string
assert not re.match(r"world", "Hello world")  # Match looks at the start of the string
assert re.match(r"Hello", "Hello world")  # Match looks at the start of the string


valid_zip_code = r'[0-9]{5}'
assert re.fullmatch(valid_zip_code, '90210')
assert not re.fullmatch(valid_zip_code, '9021')
assert not re.fullmatch(valid_zip_code, '902100')  # Full match checks that the entire string matches (e.g. no extra characters)
assert not re.fullmatch(valid_zip_code, '9021a')


# Note: \w+ finds all of the words (set of 1 or more alpha characters)
list_of_matches = re.findall(r'\w+', "The quick brown fox jumped over the lazy dog")
print(list_of_matches)


assert not re.search('hello', 'Hello world')
assert re.search('hello', 'Hello world', re.IGNORECASE)


print(re.sub(r'[aeiou]', '_', 'Hello world'))  # Replace with a static string
print(re.sub(r'(\w+)', '~*\\1*~', 'Hello world'))  # Replace with the matched pattern; \\1 refers to what was matched in the ()
