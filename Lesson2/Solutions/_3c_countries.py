"""
A program that takes a continent and prints
all of the countries on that continent
"""

# Read data/continents.csv and save all countries by continent
import csv

countries = {}
with open('../data/continents.csv', 'r') as file:
    reader = csv.DictReader(file)
    for line in reader:
        continent = line['Continent']
        if continent not in countries:
            countries[continent] = []
        countries[continent].append(line['Country'])

continents = {
    1: 'Africa',
    2: 'Asia',
    3: 'Europe',
    4: 'North America',
    5: 'Oceania',
    6: 'South America'
}

# Get user to provide a continent by inputting a number
print('Choose a continent:')
print('1: Africa, 2: Asia, 3: Europe, 4: North America, 5: Oceania, 6: South America')
number = int(input())
continent = continents.get(number)

# Print the number of countries on that continent
continent_countries = countries.get(continent, [])
print(f'There are {len(continent_countries)} countries in {continent}')

# Print each of the countries on that continent to the console
for country in continent_countries:
    print('  ' + country)
