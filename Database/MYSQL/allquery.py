import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)


# creating the databases with the help of mydb
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists test2")
mydb.close()
# creating the table with the help of mydb
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists  test2.test_table(c1 INT , c2 VARCHAR(50) , c3 FLOAT , c4 INT , c5 VARCHAR(30))")
mydb.close()

# query on the database 
mycursor = mydb.cursor()
#mycursor.execute("select * from test2.test_table")
mycursor.execute("select c1 , c5 from test2.test_table")
for i in mycursor.fetchall() : 
    print(i)

mydb.close()
