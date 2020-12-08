import csv
import re
import time

import requests
from bs4 import BeautifulSoup

SLEEP_SECONDS = 1

# Todo: Update with your info
NAME = None
EMAIL = None
assert NAME and EMAIL

HEADERS = {'User-Agent': f'{NAME} ({EMAIL})'}

BASE_URL = "http://ariannedee.pythonanywhere.com"
URL = BASE_URL + "/Member_states_of_the_United_Nations"


def run_scraper():
    soup = get_soup_from_url(URL)
    countries = get_country_dicts(soup)

    for country_dict in countries[:3]:
        get_country_detail_data(country_dict)
        time.sleep(SLEEP_SECONDS)

    write_to_csv(countries)


def get_soup_from_url(url):
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 200, f"Response was {response.status_code} for url {url}"
    html_doc = response.text
    return BeautifulSoup(html_doc, 'html.parser')


def get_country_dicts(soup):
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
    return countries


def get_country_detail_data(country_dict):
    soup = get_soup_from_url(country_dict['URL'])
    table = soup.find('table', class_='geography')

    def get_detail_data(name):
        tr_header = table.find('tr', string=re.compile(name))
        data_text = tr_header.next_sibling.td.text
        return data_text.split()[0].split('[')[0]

    country_dict["Area"] = get_detail_data("Area")
    country_dict["Population"] = get_detail_data("Population")


def write_to_csv(country_dicts):
    with open("countries.csv", "w") as file:
        writer = csv.DictWriter(file, ('Name', 'Date Joined', 'Area', 'Population'), extrasaction="ignore")
        writer.writeheader()
        writer.writerows(country_dicts)


if __name__ == "__main__":
    run_scraper()
