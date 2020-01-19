#!/usr/bin/env python3

from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://www.soccerstats.com/latest.asp?league=england' #URL
response = requests.get(url) #RESPONSE

if response.status_code in [200]:
    print('It worked!')
    
bs = BeautifulSoup(response.text, 'html.parser') #CONTENT

teams  = []
pos = []
team_pos = []

pos_list = bs.findAll('td', {'height':'22', 'align':'center'})
team_list = bs.findAll('td', {'width':'110'})
    
for idx in pos_list:
    p = idx.get_text().strip()
    pos.append(p)
    
for idx in pos:
   if idx != '':
      try:
         if int(idx):
            team_pos.append(idx)
      except:
         pass
        
for idx in team_list:
   t = idx.get_text().strip()
   teams.append(t)
   
epl_table_pos = dict(zip(team_pos, teams)) #Data put in a dictionary.
print(epl_table_pos)

#Storing data in a CSV file.
df = pd.DataFrame({'Position':team_pos, 'Team':teams})
df.to_csv('table.csv', index=False, encoding='utf-8')