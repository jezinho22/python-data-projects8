# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 08:43:47 2019

@author: Jeremy
"""

from bs4 import BeautifulSoup
import requests
from user_agent import generate_user_agent
import pandas as pd

page_link = 'https://www.transfermarkt.com/championship/startseite/wettbewerb/GB2/saison_id/2018'
user_headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
#page_response = requests.get(page_link, timeout=5, headers=user_headers)
print page_response
page_content = BeautifulSoup(page_response.content, "html.parser")

table = page_content.find(class_="responsive-table")
table_body = table.find('tbody')
link = table_body.find_all('a', class_="vereinprofil_tooltip")
links = []
for i in range(0, len(link),3 ):
    links.append(link[i]['href'])
clubs = []
for club in links:
    clubs.append("https://www.transfermarkt.com" + str(club))
    

df2 = pd.DataFrame (clubs)

#make csv
df2.to_csv("transfermarkt page list.csv")


