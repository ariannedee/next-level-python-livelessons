"""
A program that takes a letter and outputs a text file of
all of the countries that start with that letter
"""
from collections import defaultdict


# Read data/countries.txt and save all countries by starting letter
countries = defaultdict(list)
with open('../data/countries.txt', 'r') as file:  # Remove the ../ if the data folder is a sibling of this file
    for line in file.readlines():
        starting_letter = line[0]
        country = line.strip()
        countries[starting_letter].append(country)

# Get user to provide a letter
letter = input('Number of countries that start with letter: ')
letter = letter.capitalize()

# Print the number of countries that start with the letter
letter_countries = countries[letter]
print(f'{len(letter_countries)} countries start with an {letter}')

# Create text file that lists the countries starting with the letter
with open(f'../data/{letter}_countries.txt', 'w') as file:  # Remove the ../ if the data folder is a sibling of this file
    for country in letter_countries:
        file.write(country)
        file.write('\n')
