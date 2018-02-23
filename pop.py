import pymongo

"""
Our database is the United States Population Table (Ages 0-100) for 2010
It has the total population, the number of males and the number of females for each age from 0 to 100 in the US in 2010
Download link: http://api.population.io/1.0/population/2010/United%20States/?format=json
"""

connection = pymongo.MongoClient('homer.stuy.edu')
db = connection.leksanovD_parabS
collection = db.pop

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

findByTotalPopulation(4057000)
findByAge(45)
findByNumFemales(1977000)
findByNumMales(2296000)
findByNumMalesAndFemales(108000, 247000)

