# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:09:27 2019

@author: Jeremy
"""

import pandas as pd
import numpy as np

players = pd.read_csv('FIFA 19 Player DB.csv', low_memory = False)
clubs = pd.read_csv('world clubs.csv')
countries = players['League location'].unique().tolist()

#insert a column into the players dataframe to say where league is
#make the column
#players.insert(loc=4, column = 'League location', value = '')
#
##loop through all the records and add a value to 'League location'
#   there must be a more memory efficient way to do this
#player2 = players
#for player in range (len(players)):
#    for league in range (len(clubs)):
#        if players.iloc[player,3] == clubs.iloc[league,0]:
#            players.iloc[player,4] = clubs.iloc[league,1]
#            continue
#players.to_csv('FIFA 19 Player DB.csv')


players_abroad = []
players_nation_total = []
nation = []
percent = []

for x in countries:
    players_abroad.append (len(players[(players['Nationality'] == x) &\
                                 (players['League location'] != x)]))
    players_nation_total.append (len(players[players['Nationality'] == x]))
    nation.append (x)
    percent.append((len(players[(players['Nationality'] == x) &\
                  (players['League location'] != x)]))/(\
                  float(len(players[players['Nationality'] == x]))))
    
dict1 = {'Nation': nation,\
         'Players abroad': players_abroad,\
         'All players': players_nation_total,\
         'percent' : percent}

players_abroad_data = pd.DataFrame(dict1)

players_abroad_data.to_clipboard()