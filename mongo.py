import pymongo

connection = pymongo.MongoClient('homer.stuy.edu')
db = connection.test
collection = db.restaurants

def findByBorough(bor):
        for entry in collection.find({'borough': bor}):
                print entry

def findByZip(zipp):
        for entry in collection.find({'address': {'zipcode': zipp}}):
                print entry


#findByBorough('Brooklyn')
findByZip('10282')
