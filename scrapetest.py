#!/usr/bin/env python3

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('https://www.soccerstats.com/latest.asp?league=england')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found.')
else:
    print('It worked!')
    
bs = BeautifulSoup(html.read(), 'html.parser')

epl_dict = dict()

teamList = bs.findAll('td', {'width':'110'})
pointList = bs.findAll('td', {'bgcolor':'#dedede'})
for team in teamList:
    t = team.get_text().strip()
    epl_dict[t] = ''

print(epl_dict)