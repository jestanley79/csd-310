# Title: pytech_delete.py
# Author: Jennifer Stanley
# Date: January 19, 2023
# Description: Module 6.3 

# Step 2: Add the required Python code to connect to the students collection.

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@classcluster1.zltsdhr.mongodb.net/test"

client = MongoClient(url)

db = client.pytech

# Step 3: Call the find() method and display the results to the terminal window.

docs = db.students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")  
for doc in docs:
    print("  Student ID: " + doc["student_id"])
    print("  First Name: " + doc["first_name"])
    print("  Last Name: " + doc["last_name"])
    print("")

#Step 4: Call the insert_one() method and Insert a new document into the pytech collection with student_id 1010.

bob = {
    "student_id": "1010",
    "first_name": "bob",
    "last_name": "marley"
}

students = db.students

print("\n  -- INSERT STATEMENTS --")

bob_student_id = students.insert_one(bob).inserted_id

print("  Inserted student record into the students collection with document_id " + str(bob_student_id))

#Step 5: Call the find_one() method and display the results to the terminal window.

print("\n\n  -- DISPLAYING STUDENT TEST DOC -- ")

bob = db.students.find_one({"student_id": "1010"})

print("  Student ID: " + bob["student_id"])
print("  First Name: " + bob["first_name"])
print("  Last Name: " + bob["last_name"])
print("")

#Step 6: Call the delete_one() method by student_id 1010.

bob = db.students.delete_one({"student_id": "1010"})

#Step 7: Call the find() method and display the results to the terminal window.

docs = db.students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")  
for doc in docs:
    print("  Student ID: " + doc["student_id"])
    print("  First Name: " + doc["first_name"])
    print("  Last Name: " + doc["last_name"])
    print("")

input("\n\n  End of program, press any key to exit... ")