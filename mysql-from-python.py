import os
import pymysql

#Get username from workspace
#(modify)
username = os.getenv('C9_USER')

#connect to database
connection = pymysql.connect(host='localhost', user=username, password='', db='Chinook')

try:
    #run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #always close connection to sql
    connection.close()

