import pymongo, json
from bson import json_util

"""
Our database is the United States Population Table (Ages 0-100) for 2010
It has the total population, the number of males and the number of females for each age from 0 to 100 in the US in 2010

Download link: http://api.population.io/1.0/population/2010/United%20States/?format=json

To import our data we first downloaded it from the link
We then read the file and removed the [ at the beginning and 
the ] at the end of the string
Since the string had multiple commas everywhere, we used find
to find the opening and closing braces in the string for each
entry and converted the substring into a dictionary, then added
each document individually to the collection
"""

connection = pymongo.MongoClient('homer.stuy.edu')
db = connection.leksanovD_parabS
collection = db.pop

def addData():
    f = open('pop.json','rU')
    r = f.read()
    data = r[1:len(r)-2]
    f.close()
    i = data.find('{')
    j = data.find('}')
    while(i != -1):
        doc = eval(data[i:j+1]) #j+1 to include the closing }
        collection.insert_one(doc)
        data = data[j+2:]
        i = data.find('{')
        j = data.find('}')

def findByTotalPopulation(total):
    for entry in collection.find({'total':total}):
        print entry

def findByAge(age):
    for entry in collection.find({'age': age}):
        print entry

def findByNumFemales(females):
    for entry in collection.find({'females': females }):
        print entry

def findByNumMales(males):
    for entry in collection.find({'males': males}):
        print entry                        

def findByNumMalesAndFemales(males, females):
    for entry in collection.find({'males' : males, "females": females }):
        print entry                        

addData()
print "Find By Population: 4057000"
findByTotalPopulation(4057000)
print "Find By Age: 45"
findByAge(45)
print "Find By Female Population: 1977000"
findByNumFemales(1977000)
print "Find By Male Population: 2296000"
findByNumMales(2296000)
print "Find By Male and Female Population: 108000,247000"
findByNumMalesAndFemales(108000, 247000)

