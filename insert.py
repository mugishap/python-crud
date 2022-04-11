import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python'
)

myCursor = mydb.cursor()

sql = "INSERT INTO users(name,age) VALUES(%s,%s)"
values = [('Mahoro Ange', 13), ('Lyamukuru Irene', 26), ('Dusabe Aimee', 10), ('Faith Deborah', 7),
          ('Hirwa Gad', 4)]

myCursor.executemany(sql, values)
mydb.commit()
print("1 row inserted, ID is: {}".format(myCursor.lastrowid))
