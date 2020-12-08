import csv
import re
import time

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://ariannedee.pythonanywhere.com"
URL = BASE_URL + "/Member_states_of_the_United_Nations"

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

        links = tds[0].find_all('a')
        country_name = links[1].string
        url = BASE_URL + links[1]['href']

        date_joined = tds[1].span.string

        country_dict = {
            'Name': country_name,
            'Date Joined': date_joined,
            'URL': url
        }

        countries.append(country_dict)

for country_dict in countries[:3]:
    url = country_dict['URL']
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        continue

    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    table = soup.find('table', class_='geography')

    tr_header = table.find('tr', string=re.compile("Area"))
    area_text = tr_header.next_sibling.td.text
    area = area_text.split()[0].split('[')[0]
    country_dict["Area"] = area

    tr_header = table.find('tr', string=re.compile("Population"))
    population_text = tr_header.next_sibling.td.text
    population = population_text.split()[0].split('[')[0]
    country_dict["Population"] = population

    time.sleep(1)

with open("countries.csv", "w") as file:
    # extrasaction=ignore ignores the URL field
    writer = csv.DictWriter(file, ('Name', 'Date Joined', 'Area', 'Population'), extrasaction="ignore")
    writer.writeheader()
    writer.writerows(countries)
