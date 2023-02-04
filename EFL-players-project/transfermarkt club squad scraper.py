# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 08:38:57 2019

@author: Jeremy
"""
from bs4 import BeautifulSoup
import requests
from user_agent import generate_user_agent
import pandas as pd
import random
import time
import re

stadia=[]

clubs = pd.read_csv("transfermarkt page list.csv")

for club in clubs.Club:
    #be a conscientious scraper and pause between scrapes
    t = (random.randint(1,21)*0.1)
    time.sleep(t)
    #choose page
    page_link = club
    # generate a user agent
    user_headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
    #get the page code
    page_response = requests.get(page_link, timeout=5, headers = user_headers)
    print page_response
    
    #sort page content into soup - unlisted list of items

    page_content = BeautifulSoup(page_response.content, "html.parser")
    
    ##make a list of page_content
    #print len(list(page_content))
    ##inspect item types
    #print [type(item) for item in list(page_content)]
    
    #extract the table
    table = page_content.find(class_="responsive-table")
    
    ##make a list of table
    #print len(list(table))
    ##inspect item types
    #print [type(item) for item in list(table)]
    
    #extract the headings from the table - each is in a th tag
    header = [item.get_text() for item in table.find_all('th')]
    #print [heading.get_text() for heading in header]
    header.append('Previous value')
    header[2] = 'Position'
    
    
    all_rows = table.find_all('tr')
    #print len(all_rows)
    #print [type(item) for item in all_rows]
    #print all_rows[1].get_text()
    
    # pick out only the rows I want - means I can use items in second part, rather
    #than a range counter
    data2 = []
    for x in range(1, len(all_rows), 3):
        row = all_rows[x].find_all('td')
        #print len(row)
        #print [type(item) for item in row]
        data2.append(row)
    
    buttcheeks = []
    for row in data2:
        #capture number, name, position, value
        cell_list = [cell.get_text() for cell in row]
        data = [cell_list[c1] for c1 in [0, 5, 4, 6, 8]]
#capture nationality from flag image
        try:
            data.append(row[7].find(class_="flaggenrahmen")['title'])        #it threw a typeerror because one player had no data
        except TypeError:
            data.append('')     

#find previous price from awkward plain td and span
        try:
            previous_price = (row[8].span)['title']
            data.append(previous_price.replace('Previous Market Value: ',''))
        #it threw a typeerror because one player had no data
        except TypeError:
            data.append('')        
       
        buttcheeks.append(data)
    
    
    df2 = pd.DataFrame (buttcheeks,columns = header)
    
    #add to excel
    from openpyxl import load_workbook
    path = r"C:\Users\Jeremy\Documents\Data science\Python work in Spyder\champ squad sheets.xlsx"
    
    
    book = load_workbook(path)
    writer = pd.ExcelWriter(path, engine='openpyxl')
    writer.book = book
    
    sheet_name = club[(club.rfind('com')+4):(club.find('start')-1)]
    df2.to_excel(writer, sheet_name, index=True)
    writer.save()
    
        
    
    #   gave up on this - realised I could make each row into a list and pick
    #the items from it, well, some of them
    ##print [type(x) for x in row1]
    #print row1[1].find('div').get_text()
    #print row1[1].find(class_= "spielprofil_tooltip").get_text()
    #img = row1[1].find(class_="zentriert rueckennummer bg_Torwart")
    #print img['title']
    #print row1[1].find(class_="zentriert").get_text()
    
    #print list(row1[1].find_all('td'))
