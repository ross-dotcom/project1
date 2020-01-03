#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

url = 'https://www.soccerstats.com/latest.asp?league=england' #URL
response = requests.get(url) #RESPONSE

if response.status_code in [200]:
    print('It worked!')
    
bs = BeautifulSoup(response.text, 'html.parser') #CONTENT

teams  = []
pts = []
rank = []
rank_2 = []

teamList = bs.findAll('td', {'width':'110'})
rankList = bs.findAll('td', {'height':'22', 'align':'center'})
    
for ranks in rankList:
    r = ranks.get_text().strip()
    rank.append(r)
    
for r in rank:
    if r != '':
        try:
            if int(r):
                rank_2.append(r)
        except:
            pass
        
for team in teamList:
   t = team.get_text().strip()
   teams.append(t)

epl_dict = dict(zip(rank_2, teams))

print(epl_dict)