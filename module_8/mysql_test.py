# Title: mysql_test.py
# Author: Jennifer Stanley
# Date: February 5, 2023
# Description: Module 8.2

config = {
    "user": "root",
    "password": "ChunkyMunkey79!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

import mysql.connector
from mysql.connector import errorcode

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password is invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
        
    else:
        print(err)

finally:
    db.close()