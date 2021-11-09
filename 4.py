import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="pw12",
	database="bonk"
	)

mycursor = mydb.cursor()

mycursor.execute("""
	SELECT * FROM suppliers ORDER BY cut4 ASC, sup_name DESC;
    """)


results = mycursor.fetchall()

print(tabulate(results, headers=['sup_id','sup_name','cut2','cut3','cut4','sup_sup'], tablefmt='psql'))