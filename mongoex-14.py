"""import pymongo


myclient = pymongo.MongoClient('mongodb://localhost:27017/')

#mydb = myclient['mydatabase']
#print(myclient.list_database_names())
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")"""

"""import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']

mycol = mydb["customers"]



print(mydb.list_collection_names())"""

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)
print(x)