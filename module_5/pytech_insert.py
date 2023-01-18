from pymongo import MongoClient

url = "mongodb+srv://admin:admin@classcluster1.zltsdhr.mongodb.net/test"

client = MongoClient(url)

db = client.pytech


john = {
    "student_id": "1007",
    "first_name": "john",
    "last_name": "doe",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor lawrence",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor lawrence",
                    "grade": "A+"
                }
            ]
        }
    ]

}

jane = {
    "student_id": "1008",
    "first_name": "jane",
    "last_name": "smith",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.52",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor lawrence",
                    "grade": "B+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor lawrence",
                    "grade": "A-"
                }
            ]
        }
    ]
}

alexander = {
    "student_id": "1009",
    "first_name": "alexander",
    "last_name": "jones",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "1.5",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor lawrence",
                    "grade": "C"
                },
                {
                    "course_id": "CSD 320",
                    "description": "Programming with Java",
                    "instructor": "Professor lawrence",
                    "grade": "B"
                }
            ]
        }
    ]
}


students = db.students

print("\n  -- INSERT STATEMENTS --")
john_student_id = students.insert_one(john).inserted_id
print("  Inserted student record john doe into the students collection with document_id " + str(john_student_id))

jane_student_id = students.insert_one(jane).inserted_id
print("  Inserted student record jane smith into the students collection with document_id " + str(jane_student_id))

alexander_student_id = students.insert_one(alexander).inserted_id
print("  Inserted student record alexander jones into the students collection with document_id " + str(alexander_student_id))

input("\n\n  End of program, press any key to exit... ")
