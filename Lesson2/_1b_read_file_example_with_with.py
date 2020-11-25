"""
Read a file with a number on each line. Print the sum of those numbers.
"""

# Open the file and save it to variable "file"
with open('data/read_example.txt', 'r') as file:
    sum = 0
    # Read each line
    for line in file.readlines():
        num = int(line)
        sum += num
    print(f'Sum is {sum}')


# File is automatically closed when exiting the with block

