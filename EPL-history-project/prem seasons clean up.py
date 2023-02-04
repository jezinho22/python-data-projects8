# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 20:22:47 2019

@author: Jeremy
"""

from bs4 import BeautifulSoup
import requests
from user_agent import generate_user_agent
import pandas as pd
import re

prem = pd.read_csv('All prem seasons - Copy.csv', encoding = 'utf-8')

for f in range(len(prem.Club)):
    #replace anything in brackets
    try:
        prem.at[f, 'Club'] = re.sub(r'\(.*\)', '', prem.Club[f])
    except:
        prem.at[f, 'Club'] = prem.Club[f]
       
#clean up decoding errors
prem.replace({'''\n''': ' ',
              '''\r''': ' ',
              '\xa0': '',
              '−' : '-',
              '  ':' ',
              '   ':' ',
              '    ': ' ',
              'Total goals scored':'',
              }, regex = True, inplace = True)
t = len(prem)
print (t)
#remove empty rows
prem.drop(prem [prem.Club != prem.Club].index, inplace = True)
prem.drop(prem [prem.Club == ''].index, inplace = True)
prem.drop(prem [prem.Club == 'Team'].index, inplace = True)

prem.to_csv('Clean prem data - no season labels.csv')

