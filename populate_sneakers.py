import mysql.connector
 
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="pw12",
	database="bonk"
	)

mycursor = mydb.cursor()

lssnk =[
(1001,"Adidas","UltraBOOST 20","Black"),
(1002,"Adidas","Yeezy Boost 350 V2","Black"),
(1003,"Adidas","Yeezy Boost 350 V2","Zebra"),
(1004,"Adidas","NMD HU Pharrell Human Race","Scarlet"),
(1005,"Adidas","Yeezy Boost 700 V3","Arzareth"),
(1006,"Adidas","Yeezy Boost 500","Black"),
(1007,"Adidas","Superstar Sean Wotherspoon","Superearth"),
(1008,"Adidas","ZX 2K 4D","Cloud White"),
(1009,"Adidas","Ultra4D","Core Black"),
(2001,"Balenciaga","Triple S","Blue with clear sole"),
(2002,"Balenciaga","Track ","Black with neon green"),
(3001,"Nike","Air Force 1 Low","White"),
(3002,"Nike","Air Force 1 High","Black"),
(3003,"Nike","Air Max 90","White"),
(3004,"Nike","Air Max 2090","White"),
(3005,"Nike","MX-720-818","Black"),
(3006,"Nike","SB Dunk Low Supreme Jewel Swoosh","Silver"),
(4001,"Air Jordan","1 Low","Black Toe"),
(4002,"Air Jordan","1 Retro High","Mocha"),
(4003,"Air Jordan","4 Retro","Fire Red"),
(4004,"Air Jordan","5 Retro Off-White","Black"),
(4005,"Air Jordan","1 Retro High","Travis Scott"),
(5001,"Versace","Chain Reaction","Green"),
(6001,"Vans","Old Skool David Bowie Aladdin Sane","Red"),
(6002,"Vans","Old Skool Yacht Club","Blue"),
(6003,"Vans","Authentic Supreme Blue Checker Logo","Blue")
]

cod = "INSERT INTO sneakers(snkr_id, brand, name, colortype) VALUES(%s, %s, %s, %s)"

mycursor.executemany(cod, lssnk)

mydb.commit()

print(mycursor.rowcount, "inserted!")