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
        links = row.td.find_all('a')
        country_name = links[1].string
        countries.append(country_name)

with open("countries.txt", "w") as file:
    for country in countries:
        file.write(country)
        file.write('\n')
