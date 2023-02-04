# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 11:22:57 2019

@author: Jeremy
"""

import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000) 


stadia = pd.read_csv('Eng stadia utf.csv')
stadia.to_csv('Eng stadia utf2.csv')
print (stadia.head())
print ('''
''')
print (stadia.info())
biggest_stadia = stadia[stadia.Capacity > 20000]
print (biggest_stadia[['Stadium','Capacity']])
print (stadia['League_Tier'].unique())
champ = stadia[stadia.League_Tier == 'Championship']
print ('''
''')
print (champ[['Stadium', 'Capacity', 'Club', 'League_Pos']].sort_values('Capacity', ascending = False))
print ('''
''')
#champ.to_csv('Championship grounds.csv')