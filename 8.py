import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="pw12",
	database="bonk"
	)

mycursor = mydb.cursor(buffered=True)

sup_name=str(input("Supplier name: "))

mycursor.execute("SELECT sup_id, cut2 FROM suppliers WHERE sup_name = " + '\'' + sup_name + '\';')


curs = mycursor.fetchall()

for x in curs:
	sup_id = x[0]
	cut2 = x[1]

mycursor = mydb.cursor(buffered=True)

maxim = 0
minim = 1000000000

mycursor.execute("SELECT price, snkr_id FROM stock WHERE sup_id=" + str(sup_id) )

curs = mycursor.fetchall()

for x in curs:
		if x[0] > maxim:
			maxim = x[0]
			pmax = x[1]
		if x[0] < minim:
			minim = x[0]
			pmin = x[1]

mycursor = mydb.cursor(buffered=True)

mycursor.execute("SELECT * FROM sneakers WHERE snkr_id=" + str(pmax) )
	
#print('Maxim = ', maxim)

results = mycursor.fetchall()

print(tabulate(results, headers=['snkr_id','brand','name','colortype'], tablefmt='psql'))



mycursor = mydb.cursor(buffered=True)

mycursor.execute("SELECT * FROM sneakers WHERE snkr_id=" + str(pmin) )
	
#print('Minim = ', minim)

results = mycursor.fetchall()

print(tabulate(results, headers=['snkr_id','brand','name','colortype'], tablefmt='psql'))

print("\nTotal: ", (minim+maxim) * (100-cut2) / 100)