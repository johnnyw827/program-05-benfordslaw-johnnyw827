import pandas as pd
from bs4 import BeautifulSoup
import requests

nbawebsite = 'https://basketballnoise.com/nba-players-height-2019-2020/'

height_list = []

data = requests.get(nbawebsite)
soup = BeautifulSoup(data.text,'html.parser')

height_tables = soup.findAll(class_='wp-block-table is-style-stripes')
height_tables.find_all('tbody')
