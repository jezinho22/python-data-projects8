# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 12:52:49 2019

@author: Jeremy
"""

from bs4 import BeautifulSoup
import requests
from user_agent import generate_user_agent
import pandas as pd

page_link = "https://en.wikipedia.org/wiki/List_of_football_clubs_in_England"
    
#generate a user agent
user_headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
#get the page code
page_response = requests.get(page_link, timeout=5, headers = user_headers)
print page_response

page_content = BeautifulSoup(page_response.content, "html.parser")

table = page_content.find_all('table', class_='wikitable sortable')

#print len(table.find_all

headings = [x.get_text() for x in table[0].find_all('th')]

tablelist = []
club = []

#page is made up of a series of tables, so
#table level
for tab in table:
    #skip the last table which has 6 columns
    if len(tab.find_all('th'))>5:
        print len(tab.find_all('th'))
        break
    #row level    
    for row in tab.find_all('tr'):
        club = []
        #cell level - 5 cells to a row        
        for cell in row.find_all('td'):
            club.append(cell.get_text())        
        tablelist.append(club)
        
clublist = pd.DataFrame(tablelist, columns = ['Club', 'League', 'Lvl', 'Nickname','Change from 2017-18'])


filename = 'Eng clubs list.csv'
clublist.to_csv(filename, encoding = 'utf-8')