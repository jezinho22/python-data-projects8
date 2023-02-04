# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:07:12 2019

@author: Jeremy
"""

import pandas as pd
import numpy as np



fifa = pd.read_csv('fifa 19.csv')
fifa.insert(9, 'Growth',(fifa['Potential'] - fifa['Overall']))

nos_teams = ['Os Belenenses', 'SL Benfica', 'Boavista FC', \
             'SC Braga', 'GD Chaves', 'CD Aves', 'CD Feirense',\
             'Clube Sport Marítimo', 'Moreirense FC', 'CD Nacional',\
             'Portimonense SC', 'FC Porto', 'Rio Ave FC', 'Santa Clara',\
             'Sporting CP', 'CD Tondela', 'Vitória Guimarães',\
             'Vitória de Setúbal']

fifa2 = fifa[fifa.Nationality == 'Portugal']
liga_nos = fifa[fifa.Club.isin(nos_teams)]
liga_nos = pd.merge(liga_nos, fifa2, how='outer')

#using the number of portuguese players at each club to identify
# the liga nos teams - didnt quite work
#liggg = liga_nos.groupby('Club').ID.count().reset_index()
#liggg2 = liggg[liggg.ID > 3]
#print liggg2
#exporting to send to Martin
#liggg2.to_csv('Portuguese players in world teams.csv')
#print liggg2.mean(axis=0)


#print liga_nos.count()

#  centreback
#cb1 = liga_nos[(liga_nos['Position'].str.find('CB') >-1) &\
#(liga_nos['Interceptions'] > x) & \
#(liga_nos['Acceleration'] > x + 5) &\
#(liga_nos['ShortPassing'] > x) &\
#(liga_nos['Marking'] > x) &\
#(liga_nos['Strength'] > x)]
#cb2 = cb1[['Name', 'Age', 'Overall', 'Potential','Growth', 'Club', 'Value',\
#          'Wage', 'Weak Foot','Loaned From','Contract Valid Until',\
#          'ShortPassing', 'BallControl', 'Acceleration',\
#          'SprintSpeed','Strength', 'Marking', 'Release Clause']]

#cb2 = cb1[['Name', 'Age', 'Overall', 'Potential','Growth', 'Club', 'Value',\
#          'Wage', 'Weak Foot','Loaned From','Contract Valid Until',\
#          'ShortPassing', 'BallControl', 'Acceleration',\
#          'SprintSpeed','Strength', 'Marking', 'Release Clause']]


#  centre mid
#cb1 = liga_nos[(liga_nos['Position'].str.find('CM') >-1) &\
#(liga_nos['Interceptions'] > -10) & \
#(liga_nos['Acceleration'] > x) &\
#(liga_nos['ShortPassing'] > x) &\
#(liga_nos['LongShots'] > x - 10)]# &\
##(liga_nos['Vision'] > x)]
#
#cb2 = cb1[['Name', 'Age', 'Overall', 'Potential','Growth', 'Club', 'Value',\
#          'Wage', 'Weak Foot','Loaned From','Contract Valid Until',\
#          'ShortPassing', 'BallControl', 'Acceleration',\
#          'SprintSpeed','Interceptions','Strength', 'LongShots', 'Release Clause']]
#
#cb2.to_clipboard()
x = 70
#   striker # &\
#cb1 = liga_nos[(liga_nos['ShotPower'] > x) & \
#(liga_nos['Positioning'] > x - 5 ) &\
#(liga_nos['ShortPassing'] > x - 10) &\
#(liga_nos['Acceleration'] > x) &\
#(liga_nos['Position']=='ST') | (liga_nos['Position']=='CF')]
#
#
#cb2 = cb1[['Name', 'Age', 'Overall', 'Potential','Growth', 'Club', 'Value',\
#          'Wage', 'Weak Foot','Loaned From','Contract Valid Until',\
#          'ShortPassing', 'BallControl', 'Acceleration',\
#          'SprintSpeed','Interceptions','Strength', 'LongShots', 'Release Clause']]
#
#cb2.to_clipboard()

#ncfc_germans = fifa[(fifa['Club']== 'Norwich City')\
#            & (fifa['Nationality'] == 'Germany')]
#ncfc_germans = ncfc_germans[['Name', 'Age', 'Overall', 'Potential','Growth', 'Club', 'Value',\
#          'Wage', 'Weak Foot','Loaned From','Contract Valid Until',\
#          'ShortPassing', 'BallControl', 'Acceleration',\
#          'SprintSpeed','Interceptions','Strength', 'LongShots', 'Release Clause']]
#ncfc_germans.to_clipboard()

#   Portimao only has 4 Portuguese players - where fo the others come from?
#portimao = fifa[fifa['Club'] == 'Portimonense SC']
#portimonense = portimao.groupby('Nationality').ID.count().reset_index()
#portimonense.to_clipboard()
# where do the rest of the Liga Nos players come from
liga_nos3 = fifa[fifa.Club.isin(nos_teams)]
nations = liga_nos3.groupby(['Nationality','Club']).ID. count().reset_index()
print (nations)
nations_pivot = nations.pivot(columns = 'Nationality', index = 'Club', values = 'ID')
nations_pivot.to_clipboard()


