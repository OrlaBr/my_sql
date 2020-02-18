import os
import pymysql

# Get username from workspace
# (modify)
username = os.getenv('C9_USER')

# connect to database
connection = pymysql.connect(host='localhost', user=username, password='', db='Chinook')

try:
    # run a query
    with connection.cursor() as cursor:
        list_of_names =['Jim']
        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({})".format(format_strings), list_of_names)
        connection.commit()
finally:
    # always close connection to sql
    connection.close()
