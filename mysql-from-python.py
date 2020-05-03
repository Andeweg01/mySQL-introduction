# Standard DELETE:

import os
import pymysql

# Get username from workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE Name = 'Bob';")
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
