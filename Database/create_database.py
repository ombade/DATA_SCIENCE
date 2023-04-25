import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists test2")
mydb.close()