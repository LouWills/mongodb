import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

#new_doc = {'first': 'douglas', 'last': 'wilton', 'dob': '17/04/1958', 'hair_colour': 'grey', 'occupation': 'retired', 'nationality': 'scottish'}

coll.remove({'first': 'douglas'})

documents = coll.find()

for doc in documents:
    print(doc)