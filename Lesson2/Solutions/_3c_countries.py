"""
A program that takes a continent and prints
all of the countries on that continent
"""
import csv

continent_dict = {}

# Read data/continents.csv and save all countries by continent
with open("../data/continents.csv") as file:
    reader = csv.DictReader(file)
    for country in reader:
        continent = country["Continent"]
        if continent not in continent_dict:
            continent_dict[continent] = []

        continent_dict[continent].append(country["Country"])

continents = [
    'Africa',
    'Asia',
    'Europe',
    'North America',
    'Oceania',
    'South America'
]

# Get user to provide a continent by inputting a number
print('Choose a continent:')
print('1: Africa, 2: Asia, 3: Europe, 4: North America, 5: Oceania, 6: South America')
user_number = int(input())

continent = continents[user_number - 1]
continent_countries = continent_dict[continent]

# Print the number of countries on that continent
print(f"There are {len(continent_countries)} countries in {continent}")

# Print each of the countries on that continent to the console
print(continent_countries)
