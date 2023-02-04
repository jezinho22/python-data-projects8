# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import requests
from user_agent import generate_user_agent
import pandas as pd
#import random
#import time
#import re
from datetime import date

lst = []

for intmonth in (8,9,10,11,12,1):
    strpage_link = "https://www.soccerstats.com/results.asp?league=england&pmtype=month" + str(intmonth)
    
    #generate a user agent
    user_headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
    
    #get the page code
    page_response = requests.get(strpage_link, timeout=5, headers = user_headers)
    print (page_response)

    page_content = BeautifulSoup(page_response.content, "html.parser")

    table1 = page_content.find_all('a', class_="tooltip2")

    
    for x in range(len(table1)):
        score = table1[x].find('div', style="text-align:center;").get_text()
        #replace unwanted items
        for r in (('\xa0\xa0', "-"), ('\r', ''), ('\n','')):
            score = score.replace(*r)
        score = score.split('-')
    
        halftime = table1[x].find('div', style="text-align:left;").get_text().replace('-',' ')
        ht = halftime.find('HT:')
        halftime = halftime[ht+3:ht+12]
        halftime2 = [int(s) for s in halftime.split() if s.isdigit()]
        lst.append([score, halftime2])
    
print (lst[1][1])
print (lst[1][0:])
print (len(lst))
listall = []
for x in range(len(lst)):
    listall.append(lst[x][0] + lst[x][1])





#s += 1


df= pd.DataFrame(listall, columns = ['home','homeresult','awayresult','away','homehalftime','awayhalftime'])
filename = 'eplscores plus halftimes' + '.csv'
df.to_csv(filename)