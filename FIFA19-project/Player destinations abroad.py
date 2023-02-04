# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:17:47 2019

@author: Jeremy
"""

import pandas as pd
import numpy as np

players = pd.read_csv('FIFA 19 Player DB.csv', low_memory = False)
clubs = pd.read_csv('world clubs.csv')
countries = players['League location'].unique().tolist()


#where in the world are all the English players?
#
#English_players = players[players.Nationality == 'England']
#
#Locs = English_players.groupby('League location').ID.count().reset_index()
#
#woah = (Locs['ID'] / float(Locs['ID'].sum())).reset_index()
#Locs['percent'] = woah['ID']

#  extract locations for all countries in countries list
# and add to excel as a sheet per country
with pd.ExcelWriter('player locations project.xlsx') as writer:  # doctest: +SKIP
    for x in countries:
        x_players = players[players.Nationality == x]
        x_locations = x_players.groupby('League location').ID.count().reset_index()
        #make percents column
        percent_series = (x_locations['ID'] / float(x_locations['ID'].sum())).reset_index()
        x_locations['percent'] = percent_series['ID']
        x_locations.sort_values(['percent'],ascending=[False], inplace = True)
        x_locations.to_excel(writer, sheet_name = x)

#less than half of the players listed as Irish in FIFA19 actually play in Ireland

#only 51% of Portuguese players play in Portugal
#but there is at least one more pro league in Portugal
        
#only 56% of Argetninian players play in Argentina, yet most of the players
#in the Argentine league are Argentinian - a staggering 277 players play abroad!

#93% of English players and 99% of Chinese players play in their own country
#also 99% of Saudi players
        

