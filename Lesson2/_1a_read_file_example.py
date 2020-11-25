"""
Read a file with a number on each line. Print the sum of those numbers.
"""

# Open file
file = open('data/read_example.txt', 'r')

sum = 0
# Read each line
for line in file.readlines():
    num = int(line)
    sum += num

print(f'Sum is {sum}')

# Close the file
file.close()
