#!/usr/bin/python3

import mysql.connector

# print(mysql.connector)

#establishing the connection
conn = mysql.connector.connect(user='remoteuser', password='testerific', host='0.1.2.3.4', database='tester')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()


cursor.execute("SELECT * FROM employees")

data = cursor.fetchall()

print(data)

for record in data:
    print(f'His name is... {record[2]}')

#Closing the connection
conn.close()
