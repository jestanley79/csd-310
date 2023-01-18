from pymongo import MongoClient
url = "mongodb+srv://admin:admin@classcluster1.zltsdhr.mongodb.net/test"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})

print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")  
for doc in docs:
    print("Student ID: " + doc["student_id"])
    print("First Name: " + doc["first_name"])
    print("Last Name: " + doc["last_name"])
    print("")

doc = db.students.find_one({"student_id": "1007"})

print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")

print("Student ID: " + doc["student_id"])
print("First Name: " + doc["first_name"])
print("Last Name: " + doc["last_name"])

input("\nEnd of program, press any key to exit... ")
