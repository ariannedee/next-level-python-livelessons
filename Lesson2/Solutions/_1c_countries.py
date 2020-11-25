"""
A program that takes a letter and prints
all of the countries that start with that letter
"""

countries = []

# Read data/countries.txt and save all countries by starting letter
with open("data/countries.txt") as file:
    for line in file.readlines():
        countries.append(line.strip())

# Get user to provide a letter
letter = input('Number of countries that start with letter: ')
letter = letter.capitalize()

# Print the number of countries that start with the letter
letter_countries = []
for country in countries:
    if country[0].upper() == letter:
        letter_countries.append(country)

# Print the number of countries that start with the letter
print(f"There are {len(letter_countries)} countries that start with the letter {letter}")

# Print the countries that start with the letter
print(letter_countries)
