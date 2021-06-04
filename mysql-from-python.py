import os
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

    # Run a query
try:
    with connection.cursor() as cursor:  
        cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['Bob','Jim'])
        connection.commit()
finally:
    connection.close()