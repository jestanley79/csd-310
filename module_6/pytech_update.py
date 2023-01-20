# Title: pytech_update.py
# Author: Jennifer Stanley
# Date: January 18, 2023
# Description: Module 6.2 

# Step 3: Add the required Python code to connect to the students collection.

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@classcluster1.zltsdhr.mongodb.net/test"

client = MongoClient(url)

db = client.pytech

# Step 4: Call the find() method and output the documents to the terminal window.

docs = db.students.find({})

print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")  
for doc in docs:
    print("Student ID: " + doc["student_id"])
    print("First Name: " + doc["first_name"])
    print("Last Name: " + doc["last_name"])
    print("")

# Step 5: Call the update_one method by student_id 1007 and update the last name to something different than the originally saved name.

print("\n-- DISPLAYING STUDENT DOCUMENT 1007 --") 

# Do I need to have an $unset somewhere to take out the old last name? I had update= at first, but my classmate has update=... neither one works.
update = db.students.update_one({"student_id" : "1007" }, {"$set": {"last_name": "Depp"}})

# Step 6: Call the find_one method by student_id 1007 and output the document to the terminal window.

john = db.students.find_one({"student_id": "1007"})

print("  Student ID: " + john["student_id"])
print("  First Name: " + john["first_name"])
print("  Last Name: " + john["last_name"])

input("\n\n  End of program, press any key to continue...")