#!/usr/bin/env

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
print(bs.h1)