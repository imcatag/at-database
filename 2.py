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
	SELECT * FROM sneakers WHERE brand IN ('Nike', 'Air Jordan');
    """)


results = mycursor.fetchall()

print(tabulate(results, headers=['snkr_id','brand','name','type'], tablefmt='psql'))