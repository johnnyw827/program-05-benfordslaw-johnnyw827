import pandas as pd
from bs4 import BeautifulSoup
import requests

nbawebsite = 'https://basketballnoise.com/nba-players-height-2019-2020/'

height_list = []

data = requests.get(nbawebsite)
soup = BeautifulSoup(data.text,'html.parser')

#height_tables = soup.findAll('td')
#print(height_tables[14].get_text())

tables = soup.find(class_='wp-block-table is-style-stripes')
for tr in tables.findAll('tr'):
    place = tr.findAll('td')[1].text
    print(place[0])
