# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 23:55:15 2019

@author: Jeremy
"""

import requests
import lxml.html as lh
import pandas as pd

#decades = ['1950s','1960s','1970s','1980s','1990s','2000s','2010s']
decades = ['Reading']
for decs in decades:
    url='http://www.transfermarkt.co.uk/reading-fc/kader/verein/1032/saison_id/2018/plus/1'
    
    #Create a handle, page, to handle the contents of the website
    page = requests.get(url)
    print page.text
    #Store the contents of the website under doc
    doc = lh.fromstring(page.content)
    print doc
    #Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')   
    print tr_elements
    #Check the length of the first 12 rows
    print [len(T) for T in tr_elements[:50]]
    
    #Create empty list
    
    col=[]
#    col.append(('No.',[]))
#    col.append(('Artist',[]))
#    col.append(('Album',[]))
#    col.append(('Record label',[]))
#    col.append(('When number 1',[]))
#    col.append(('No of weeks',[]))
#    if decs > '1970s':
#        col.append(('Certification',[]))
    
#    i=0
#    #For each row, store each first element (header) and an empty list
#    #for t in tr_elements[0]:
#    #    i+=1
#    #    name=t.text_content()
#    #    print '%d:"%s"'%(i,name)
#    #    col.append((name,[]))
#    
#    #Since out first row is the header, data is stored on the second row onwards
#    for j in range(1,len(tr_elements)):
#        #T is our j'th row
#        T=tr_elements[j]
#        #check on T
#        print len (T)
#        if decs > '1970s':
#            target_rows = 7
#        else:
#            target_rows = 6
#        #If row is not of size 6, the //tr data is not from our table 
#        #but there may be other tables, so just process rows of 6 items
#        if len(T) == target_rows:  
#            #i is the index of our column
#            i=0        
#            #Iterate through each element of the row
#            for t in T.iterchildren():
#                data=t.text_content() 
#                #Check if row is empty
#                if i>-1:
#                #Convert any numerical value to integers
#                    try:
#                        data=int(data)
#                    except:
#                        pass
#                #Append the data to the empty list of the i'th column
#                col[i][1].append(data)
#                #Increment i for the next column
#                i+=1
#    #check all columns are the same length
#    #print [len(C) for (title,C) in col]
#    
#    Dict={title:column for (title,column) in col}
#    df=pd.DataFrame(Dict)
#    
#    #add to excel
#    from openpyxl import load_workbook
#    path = r"C:\Users\Jeremy\Documents\Data science\Python work in Spyder\no one albums.xlsx"
#    
#    
#    book = load_workbook(path)
#    writer = pd.ExcelWriter(path, engine='openpyxl')
#    writer.book = book
#    
#    df.to_excel(writer, decs , index=True)
#    writer.save()
#    
#        #be a conscientious scraper and pause between scrapes
#    time.sleep(1)
