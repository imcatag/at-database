import mysql.connector
 
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="pw12",
	database="bonk"
	)

mycursor = mydb.cursor()

nrt = int(input("Number of tables to delete: "))

while nrt>0:
	nrt-=1
	tablename = str(input("Table name: "))
	mycursor.execute("DROP TABLE "+ tablename)
