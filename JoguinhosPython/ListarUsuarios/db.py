import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='pythonusers'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT nome,email FROM usuarios")

for x,y in mycursor:
  print(x)
  print(y)








