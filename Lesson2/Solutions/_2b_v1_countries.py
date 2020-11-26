"""
A program that takes a letter and outputs a text file of
all of the countries that start with that letter
"""

countries = []

# Read data/countries.txt and save all countries by starting letter
with open("../data/countries.txt") as file:  # Remove the ../ if the data folder is a sibling of this file
    for line in file.readlines():
        countries.append(line.strip())

# Get user to provide a letter
letter = input('Number of countries that start with letter: ')
letter = letter.capitalize()

letter_countries = []
for country in countries:
    if country[0].upper() == letter:
        letter_countries.append(country)

# Print the number of countries that start with the letter
print(f'{len(letter_countries)} countries start with an {letter}')

# Create text file that lists the countries starting with the letter
with open(f'data/{letter}_countries.txt', 'w') as file:
    for country in letter_countries:
        file.write(country)
        file.write('\n')
