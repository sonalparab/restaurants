import pymongo

connection = pymongo.MongoClient('homer.stuy.edu')
db = connection.leksanovD_parabS
collection = db.pop

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

findByAge(45)
findByNumFemales(1977000)
findByNumMales(2296000)
findByNumMalesAndFemales(108000, 247000)

