import csv

import requests
from bs4 import BeautifulSoup

URL = "http://ariannedee.pythonanywhere.com/Member_states_of_the_United_Nations"

# Todo: Update with your info
name = None
email = None
assert name and email

headers = {'User-Agent': f'{name} ({email})'}
response = requests.get(URL, headers=headers)

assert response.status_code == 200, f"Response was {response.status_code}"

html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

table = soup.find('table', class_='wikitable')

countries = []
for row in table.find_all('tr'):
    if row.td:
        tds = row.find_all('td')

        # Get the name
        links = tds[0].find_all('a')
        country_name = links[1].string

        # Get the date joined
        date_joined = tds[1].span.string

        country_dict = {
            'Name': country_name,
            'Date Joined': date_joined
        }

        countries.append(country_dict)

with open("countries.csv", "w") as file:
    writer = csv.DictWriter(file, ('Name', 'Date Joined'))
    writer.writeheader()
    writer.writerows(countries)
