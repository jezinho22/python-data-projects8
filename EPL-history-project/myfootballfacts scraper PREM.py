# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup
import requests
from user_agent import generate_user_agent
import pandas as pd

all_prem_seasons = pd.DataFrame()
all_prem_seasons2 = pd.DataFrame()

pl_seasons = pd.read_csv('prem_season_pages.csv')
dicto = {}

for page in pl_seasons.webpage[0:10]:

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
#    print ([len(rows[x].find_all('td')) for x in range(len(rows))])
    #19 columns
    col_count = ([len(rows[x].find_all('td')) for x in range(len(rows))])
    
    #capture max cells in row - just collect rows wih max
    max_col_count = max(col_count)
#    if max_col_count < 19:
#        thats_it = page
#        break
#    print (max_col_count)
    
    table= []
    club_row = []
    for row in range(len(rows)):
        #collect up season headings to separate seasons in final dataframe
        if len(rows[row].find_all('td')) == 3:
#            table.append([td.get_text() for td in (rows[row].find_all('td'))][1])
            season = [td.get_text() for td in (rows[row].find_all('td'))][1]
            #add season name to dictionary
            dicto[season] = []
        #collect data from other wanted rows
        if len(rows[row].find_all('td')) == max_col_count:
            for cell in rows[row].find_all('td'):
                club_row.append(cell.get_text())
        table.append(club_row)
        club_row=[]
    #get column headings
    cols = ['Blank0', 'Pos', 'Club', 'Pld', 'H_Won', 'H_Draw',
            'H_Loss', 'H_GF', 'H_GA', 'A_Won', 'A_Draw', 'A_Loss',
            'A_GF', 'A_GA', 'TotGF', 'TotGA', 'GD', 'Pts', 'Blank2']
    #
    #    
    prem_season = pd.DataFrame (table[4:-1], columns = cols)
    prem_season.drop(columns = ['Blank0', 'TotGF', 'TotGA', 
                                'Blank2'], inplace = True)
    all_prem_seasons = pd.concat([all_prem_seasons, prem_season])
    
    #add table to dicto under title of the season name
    dicto[season] = table
print (all_prem_seasons.head(10))
################################################################    

for page in pl_seasons.webpage[11:len(pl_seasons)]:

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
#    print ([len(rows[x].find_all('td')) for x in range(len(rows))])
    #19 columns
    col_count = ([len(rows[x].find_all('td')) for x in range(len(rows))])
    
    #capture max cells in row - just collect rows wih max
    max_col_count = max(col_count)
    
    table= []
    club_row = []
    for row in range(len(rows)):
#        collect up season headings to separate seasons in final dataframe
        if len(rows[row].find_all('td')) == 3:
            #table.append([td.get_text() for td in (rows[row].find_all('td'))][1])
            season = [td.get_text() for td in (rows[row].find_all('td'))][1]
#            add season name to dictionary
            dicto[season] = []
        #collect data from other wanted rows
        if len(rows[row].find_all('td')) == max_col_count:
            for cell in rows[row].find_all('td'):
                club_row.append(cell.get_text())
        table.append(club_row)
        club_row=[]    
        
    #get column headings
    cols = ['Blank0', 'Pos', 'Club', 'Pld', 'Tot_W', 'Tot_D',
            'Tot_L', 'TotGF', 'TotGA', 'GD', 'Pts', 'Blank2']
    #    
    prem_season = pd.DataFrame (table, columns = cols)
    prem_season.drop(columns = ['Blank0', 'TotGF', 'TotGA', 
                                'Blank2'], inplace = True)
    #add each season onto a set of seasons
    all_prem_seasons2 = pd.concat([all_prem_seasons2, prem_season])
    #add table to dicto under title of the season name
    dicto[season] = table
#stick together two sets of season
all_prem_season3 = pd.concat([all_prem_seasons, all_prem_seasons2],sort = False)
#stick it all in a csv
all_prem_season3.to_csv('All prem seasons.csv')



#make a df which has column for every position, row for each season
#collect up all the seasons into rows
all_the_seasons_list = []
#first you need a list of all the seasons, to extract each list
#from the dict - becuase its not in an order
seasonlist = [season for season in dicto.keys()]
for season in seasonlist:
    #take a heading from dicto
    sublime = dicto[season]
    #make a list of the 2nd item in each item from the season
    #that would be the club name skipping the headings row
    sublime3 = [t[1] for t in sublime[1:len(sublime)]]
    #stick the season name into the list, at the start
    sublime3.insert(0,season)
    #add the season onto the others collected
    all_the_seasons_list.append(sublime3)


#create column headings as simple 1, 2, 3, etc
x = list(range(0, max([len(s) for s in all_the_seasons_list])))
#create frame - empty cells will get NaN
df_all_seasons = pd.DataFrame(all_the_seasons_list, columns = x)