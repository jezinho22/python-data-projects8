# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup
import requests
from user_agent import generate_user_agent
import pandas as pd
import re

pl_seasons = pd.read_csv('prem_season_pages.csv')

seasons_list = []
season_row = []

for page in pl_seasons.webpage:

    page_link = page
    #generate a user agent
    user_headers = {'User-Agent': generate_user_agent(
            device_type="desktop", os=('mac', 'linux'))}
    #get the page code
    page_response = requests.get(page_link, timeout=5,headers = user_headers)
    print (page_response)
    
    page_content = BeautifulSoup(page_response.content, "html.parser")
    
    #print (len(page_content.find_all('tr')))
    #26 rows
    #
    rows = page_content.find_all('tr')
    print ([len(rows[x].find_all('td')) for x in range(len(rows))])
    #19 columns
    col_count = ([len(rows[x].find_all('td')) for x in range(len(rows))])
    
    #capture max cells in row - just collect rows wih max
    max_col_count = max(col_count)  

    for row in range(len(rows)):
        #collect up season headings to separate seasons in final dataframe
        if len(rows[row].find_all('td')) == 3:
#            table.append([td.get_text() for td in (rows[row].find_all('td'))][1])
            season_row.append([td.get_text() for td in (rows[row].find_all('td'))][1])
        #collect data from other wanted rows)
        if len(rows[row].find_all('td')) == max_col_count: 
            #dodge the 'Team' heading from earlier tables
            if [td.get_text() for td in (rows[row].find_all('td'))][2] != 'Team':
                season_row.append([td.get_text() for td in (rows[row].find_all('td'))][2])
        
    seasons_list.append(season_row)  #add row to table of season positions
    season_row = []  #reset season_row
#print (seasons_list)
max_cols =  (max([len(x) for x in seasons_list]))
cols = [x for x in range(-1,(max([len(x) for x in seasons_list]))-1)]
seasons_in_rows = pd.DataFrame(seasons_list, columns = cols)
seasons_in_rows.to_csv('another prem sheet - delete.csv')

##################################################################

#DATA CLEANING

#ditch a blank column
seasons_in_rows.drop(columns = -1, inplace = True)

#use regex sub on all cells to remove anything in brackets
for f in range(0, len(seasons_in_rows)):
    for g in range (1, len(seasons_in_rows.loc[f])):
        try:
            seasons_in_rows.loc[f].at[g] = re.sub(r'\(.*\)', '', seasons_in_rows.loc[f].at[g])
        except TypeError:
            pass
        try:
            seasons_in_rows.loc[f].at[g] = seasons_in_rows.loc[f].at[g].strip()
        except:
            pass
       
#clean up decoding errors
seasons_in_rows.replace({'''\n''': ' ',
              '''\r''': ' ',
              '\xa0': '',
              '−' : '-',
              'Total goals scored':'',
              '  ':' ',
              '   ': ' ',
              '    ': ' '
              }, regex = True, inplace = True)
seasons_in_rows.replace({'  ':' ',
              '   ': ' ',
              '    ': ' '}, regex = True, inplace = True)
seasons_in_rows.replace({'West Bromwich Alb':'West Bromwich Albion',
              'West Bromwich A': 'West Bromwich Albion',
              'Middlesbrough*': 'Middlesbrough',
              'Wolverhampton Wndrs' : 'Wolverhampton Wanderers',
              'Wolverhampton W' : 'Wolverhampton Wanderers',
              '''Queen's Park Rangers''': 'Queens Park Rangers',
              '''Cardiff City [notes 1]''':'Cardiff City'},inplace = True)
    
#change row headers/index
seasons_in_rows.insert(loc = 0, column = 'Season', value = [x for x in range(2017, 1991, -1)])
#drop unwanted columns
seasons_in_rows = seasons_in_rows.drop([0, 23, 24, 25], axis = 1)

seasons_in_rows.to_csv('Prem seasons in rows.csv')