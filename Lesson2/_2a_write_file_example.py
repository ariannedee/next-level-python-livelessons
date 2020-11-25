"""
Write a poem to a file
"""

poem = """I have eaten
the plums
that were in
the icebox

and which
you were probably
saving
for breakfast

Forgive me
they were delicious
so sweet
and so cold
"""

author = 'William Carlos Williams'

with open('data/write_example.txt', 'w') as file:
    file.write(poem)   # Multi-line strings include newlines
    file.write('\n')   # Manually insert a new line
    file.write(f'- ')  # Writes without newlines will be on the same line
    file.write(author)
