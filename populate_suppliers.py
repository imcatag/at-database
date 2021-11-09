import mysql.connector
 
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="pw12",
	database="bonk"
	)

mycursor = mydb.cursor()

lssup = [
(1,"Juan",0,0,10,0),
(2,"Matty",0,0,25,0),
(3,"Saboss",0,10,30,1),
(4,"Catag",10,15,20,0),
(5,"Banel",10,10,10,2),
(6,"Botez",0,10,15,2)
]

cod = "INSERT INTO suppliers(sup_id, sup_name, cut2, cut3, cut4, sup_sup) VALUES(%s, %s, %s, %s, %s, %s)"

#try:
mycursor.executemany(cod, lssup)
#except mysql.connector.IntegrityError as err:
#	print("Error: {}".format(err))

#mycursor.execute(
#	"INSERT INTO suppliers(sup_id, sup_name, cut2, cut3, cut4) VALUES(0, 'No Supplier',0,0,0);"
#	)

mycursor.execute("""

	UPDATE suppliers SET sup_sup = Null WHERE sup_sup=0;

""")

mydb.commit()

mycursor.execute("""
	ALTER TABLE suppliers ADD FOREIGN KEY(sup_sup) REFERENCES suppliers(sup_id) ON DELETE SET NULL;
""")

print(mycursor.rowcount, "inserted!")