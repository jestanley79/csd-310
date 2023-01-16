from pymongo import MongoClient
url = "mongodb+srv://admin:admin@classcluster1.zltsdhr.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

print("\n\n-- Pytech Collection List --")
print(db.list_collection_names())

input("\n\n  End of program, press any key to exit... ")
