import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="pw12",
	database="bonk"
	)

mycursor = mydb.cursor(buffered=True)

size=str(input("size: "))
brand=str(input("brand: "))

#print("SELECT stock.price FROM stock JOIN sneakers WHERE stock.deadstock=1, stock.size=" +  size  +", sneakers.brand=" + '\'' + brand + '\'')

mycursor.execute("SELECT stock.price FROM stock JOIN sneakers ON stock.snkr_id=sneakers.snkr_id WHERE sneakers.brand=" + '\'' + brand + '\'' + "AND stock.deadstock=1 AND stock.size=" + str(size))

minim = 1000000000

for x in mycursor:
	for i in x:
		minim = min(minim, int(i))

if(minim != 1000000000):
	print('Minim =', minim)

else:
	print("Sneaker not found!")