import os
import pymysql

#Get username from Cloud9 workspace
username = os.getenv('c9_user')
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    #run a query
    with connection.cursor() as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #close the connection regardless of whether the above was successful
    connection.close()
