import pymongo
client = pymongo.MongoClient("mongodb+srv://Bhavya:Ammulu1906@bhavya.fuzii4m.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "bhavya",
    "email" : "bhavya137@gmail.com",
    "surname" : "cheruku"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
