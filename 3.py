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

mycursor.execute("SELECT name, colortype FROM sneakers JOIN stock ON stock.snkr_id=sneakers.snkr_id WHERE sneakers.brand=" + '\'' + brand + '\'' + "AND stock.size=" + str(size))

results = mycursor.fetchall()

print(tabulate(results, headers=['name', 'colortype'], tablefmt='psql'))
