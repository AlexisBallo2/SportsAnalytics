import numpy
import csv

newlist = []
names = {}
y = -1
#print(newdata)
#print(newdata[1])
#equ = (hitts - homeruns)/(atbats - strikeouts - homeruns + sacrificefiles)


#start by opening the file and reading the data
with open('sa.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        y = y+1
        newlist.append(row)
        names[row[0]] = y

#make sure list is generating correctly      
print("list: ", newlist)
def calculate(name):
  x = names[name]
#create dictionary from list [0] and [1]
  dict1 = {}
  dict1 = dict(zip(newlist[0],newlist[x]))
  for a,b in dict1.items():
      try:
          dict1[a] = float(b)
      except:
          try:
              dict1[a] = int(b)
          except:
              continue
  #calcualte the thing from the keys
  equ1 = (dict1['Hits'] - dict1['Homeruns']) / (dict1['Atbats'] - dict1['Strikeouts'] - dict1['Homeruns'] + dict1['Sacrificeflies'])
  return dict1['player'], "'s BIBIP for the" , str(int(dict1['year'])), " season is: " , str(equ1)

#need to convert the return value into a string to make it pretty
def tupletostring(tup): 
    str =  ''.join(tup) 
    return str

print(tupletostring(calculate('David Peralta')))
print(tupletostring(calculate('steve yaegar')))
print(tupletostring(calculate('Mark Grudzielanek')))
print(tupletostring(calculate('Victor Martinez')))


  
