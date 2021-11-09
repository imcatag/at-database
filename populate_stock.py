import mysql.connector
 
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="pw12",
	database="bonk"
	)

mycursor = mydb.cursor()

lsstk=[
(1001,200,True,8.5,3),
(1002,565,True,8,1),
(1003,480,True,9,2),
(1003,510,True,10,6),
(1004,800,True,9.5,3),
(1005,340,True,8.5,5),
(1006,125,False,9,5),
(1007,140,True,10,4),
(1008,140,True,8.5,1),
(1009,220,True,9.5,3),
(2001,895,True,9,3),
(2002,500,False,10,2),
(3001,110,True,8.5,5),
(3001,110,True,7.5,4),
(3001,120,True,9.5,4),
(3002,140,True,9,1),
(3003,150,True,8,5),
(3004,150,True,9,1),
(3005,175,True,10,6),
(3005,170,True,9.5,6),
(3006,320,True,9.5,2),
(4001,300,True,8.5,4),
(4002,350,True,9,3),
(4003,120,False,9.5,5),
(4004,925,True,9.5,5),
(4005,1600,True,9.5,3),
(5001,1000,True,9,4),
(6001,75,False,8.5,6),
(6002,70,True,9.5,2),
(6003,2600,True,10,2)
]

cod = "INSERT INTO stock(snkr_id, price, deadstock, size, sup_id) VALUES(%s, %s, %s, %s, %s)"

mycursor.executemany(cod, lsstk)

mydb.commit()

print(mycursor.rowcount, "inserted!")