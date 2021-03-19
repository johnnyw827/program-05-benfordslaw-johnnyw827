import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
def scrape():
    nbawebsite = 'https://basketballnoise.com/nba-players-height-2019-2020/'

    tes = []
    data = requests.get(nbawebsite)
    soup = BeautifulSoup(data.text,'html.parser')


    add_period = ['’']

    remove = [',',"\\","'",'"','[',']','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',"-"]
    for height in soup.find_all(class_='wp-block-table is-style-stripes'):
        tes.append(height.tr.td.text)
        table1 = str(tes[0:])

    for i in remove:
        table1 = table1.replace(i,'')
    for i in add_period:
        table1 = table1.replace(i,'.')

    ls = table1.split()
    ls2 = [s.strip('.')for s in ls]

    with open('./nbafile.txt','w') as writing:
        for i in ls2:
            writing.writelines('%s\n'%i)
