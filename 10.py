import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="pw12",
	database="bonk"
	)

mycursor = mydb.cursor(buffered=True)

sup_id=int(input("Id supplier: "))

mycursor.execute("SELECT sup_sup FROM suppliers WHERE sup_id = " + str(sup_id))

curs = mycursor.fetchall()


for x in curs:
	for i in x:
		id2 = i

if id2 != None:
	mycursor = mydb.cursor(buffered=True)

	mycursor.execute("SELECT sup_name FROM suppliers WHERE sup_id = " + str(id2))

	curs = mycursor.fetchall()

	for x in curs:
		for i in x:
			name = i

	print('\n' + name)
else:
	print("Nu exista!")