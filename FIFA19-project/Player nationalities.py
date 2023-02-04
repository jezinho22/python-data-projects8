# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:27:34 2019

@author: Jeremy
"""

import pandas as pd
import numpy as np

players = pd.read_csv('FIFA 19 Player DB.csv', \
                      encoding = "ISO-8859-1", \
                      low_memory = False)
clubs = pd.read_csv('world clubs.csv')
countries = players['League location'].unique().tolist()

#     to make a file of all nationalities
#pd.DataFrame(players['Nationality'].unique().\
#                    tolist()).to_csv('fifa nations.csv')

#     to make a file of all leagues - multiline code
#league_list = players.League.unique()
#league_list = league_list.tolist()
#csvlist = pd.DataFrame(league_list)


# Collecting up players in German leagues
#germany = players[(players.League == 'Bundesliga')|\
#                  (players.League == 'Bundesliga 2')|\
#                  (players.League == '3. Liga')].reset_index()
#germany.rename(columns={ 'index': 'ID'}, inplace=True)

#  Count German players
#germany_club_nation_count = germany.groupby(['Nationality', 'Club']).ID.count().reset_index()
#germany_club_nation_count_pivot = germany_club_nation_count.pivot(columns = 'Club', index = 'Nationality', values = 'ID').reset_index()

#germany_nation_count = germany.groupby('Nationality').ID.count().reset_index()
#total_germany = germany_nation_count.ID.sum()
#germany_nation_count['percent'] = germany_nation_count.ID * 100/ total_germany
#germany_nation_count.to_csv('german league nationals.csv')


#  Count up players of each nationality in each league
#   and export to one excel file
n=0
with pd.ExcelWriter('nationalities in leagues project.xlsx') as writer:  # doctest: +SKIP
    for league_name in clubs.League:
        league_players = players[players.League == league_name].reset_index()
        league_players.rename(columns={ 'index': 'Number'}, inplace=True)
        nation_count = league_players.groupby('Nationality').Number.count().reset_index()
        nation_total = nation_count.Number.sum()
        nation_count['percent'] = nation_count.Number * 100/ nation_total
        nation_count.sort_values(['percent'],ascending=[False], inplace = True)
        league_name_short = league_name[0:15] #sheet names can only be 31 long
        nation_count.to_excel(writer, sheet_name = league_name_short)


#could also go on and sort each by percentage, and put together for comparison
    