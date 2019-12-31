#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

url = 'https://www.soccerstats.com/latest.asp?league=england' #URL
response = requests.get(url) #RESPONSE

if response.status_code in [200]:
    print('It worked!')
else:
   print('Failed.')
    
bs = BeautifulSoup(response.text, 'html.parser') #CONTENT

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