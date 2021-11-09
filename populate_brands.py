import mysql.connector
 
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="pw12",
	database="bonk"
	)

mycursor = mydb.cursor()

lsbrands = [
("Adidas",1,"adidas.com"),
("Balenciaga",2,"balenciaga.com"),
("Nike",3,"nike.com"),
("Air Jordan",4,"nike.com/jordan"),
("Versace",5,"versace.com"),
("Vans",6,"vans.eu")
]


cod = "INSERT INTO brands(brand, brand_id, site) VALUES(%s, %s, %s)"

mycursor.executemany(cod, lsbrands)

mydb.commit()

print(mycursor.rowcount, "inserted!")