import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python'
)

myCursor = mydb.cursor()
# myCursor.execute('CREATE TABLE users(name varchar(200),age int)')
myCursor.execute('SHOW TABLES')
for x in myCursor:
    print(x)
