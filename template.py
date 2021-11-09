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

    """)