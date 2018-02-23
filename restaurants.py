import pymongo

connection = pymongo.MongoClient('homer.stuy.edu')
db = connection.test
collection = db.restaurants

def findByBorough(borough):
    for entry in collection.find({'borough': borough}):
        print entry

def findByZip(zipcode):
    for entry in collection.find({'address.zipcode' : zipcode }):
        print entry

def findByZipandGrade(zipcode,grade):
    for entry in collection.find({'address.zipcode' : zipcode, "grades.grade" : grade}):
        print entry                        

def findByZipandScore(zipcode,score):
    for entry in collection.find({'address.zipcode' : zipcode, "grades.score": {"$lt": score }}):
        print entry                        

def findByZipandCuisine(zipcode,cuisine):
    for entry in collection.find({'address.zipcode' : zipcode, "cuisine": cuisine }):
        print entry
        
findByBorough('Brooklyn')
findByZip('10282')
findByZipandGrade('10282','A')
findByZipandScore('10282',10)
findByZipandCuisine('10282','American')
