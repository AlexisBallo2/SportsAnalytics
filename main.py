import pandas as pd
import numpy
import csv
import json


newlist = []
#print(newdata)
#print(newdata[1])
#equ = (hitts - homeruns)/(atbats - strikeouts - homeruns + sacrificefiles)


#start by opening the file and reading the data
with open('sa.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        newlist.append(row)

#make sure list is generating correctly      
print("list: ", newlist)

#create dictionary from list [0] and [1]
dict1 = {}
dict1 = dict(zip(newlist[0],newlist[1]))
for a,b in dict1.items():
    try:
        dict1[a] = float(b)
    except:
        try:
            dict1[a] = int(b)
        except:
            print()
#calcualte the thing from the keys
equ1 = (dict1['Hits'] - dict1['Homeruns']) / (dict1['Atbats'] - dict1['Strikeouts'] - dict1['Homeruns'] + dict1['Sacrificeflies'])
print(dict1['player'], "'s BIBIP for the" , int(dict1['year']), " season is:" , equ1)


dict2 = {}

#print("list: ", newlist)
dict2 = {}
dict2 = dict(zip(newlist[0],newlist[2]))
for a,b in dict2.items():
    try:
        dict2[a] = float(b)
    except:
        try:
            dict2[a] = int(b)
        except:
            print()
#print(dict1)
equ2 = (dict2['Hits'] - dict2['Homeruns']) / (dict2['Atbats'] - dict2['Strikeouts'] - dict2['Homeruns'] + dict2['Sacrificeflies'])
print(dict2['player'], "'s BIBIP is:" , equ2)
