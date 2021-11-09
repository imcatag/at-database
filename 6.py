import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="pw12",
	database="bonk"
	)

mycursor = mydb.cursor(buffered=True)

mycursor.execute("SELECT price FROM stock WHERE deadstock=0")

sum=0

for x in mycursor:
	for i in x:
		sum = sum + int(i)

print('Sum =', sum/mycursor.rowcount)