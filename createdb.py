import mysql.connector
 
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="pw12"
	)

mycursor = mydb.cursor()

mycursor.execute("""
	CREATE DATABASE bonk
    """)

print("Database created succesfully!")