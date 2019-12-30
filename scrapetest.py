#!/usr/bin/env python3

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from lxml import etree
import requests

# try:
#     html = urlopen('https://www.soccerstats.com/latest.asp?league=england')
# except HTTPError as e:
#     print(e)
# except URLError as e:
#     print('The server could not be found.')
# else:
#     print('It worked!')

url = 'https://www.soccerstats.com/latest.asp?league=england'
response = requests.get(url)

if response.status_code in [200]:
    print('It worked!')
    
html = response.text
    
bs = BeautifulSoup(html, 'html.parser')

teams  = []
pts = []

teamList = bs.findAll('td', {'width':'110'})
pointList = bs.findAll('td', {'bgcolor':'#dedede'})
for team in teamList:
   t = team.get_text().strip()
   teams.append(t)
    
for points in pointList:
    p = points.get_text().strip()
    pts.append(p)

epl_dict = dict(zip(teams, pts))

print(epl_dict)