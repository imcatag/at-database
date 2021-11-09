import mysql.connector
from tabulate import tabulate
import sys

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pw12",
    database="bonk"
    )

arglist = str(sys.argv)

for i in range(1, len(sys.argv)):
    
    table = sys.argv[i]

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM  "+ table)

    results = mycursor.fetchall()

    if table.upper() == 'STOCK':
        head = ['snkr_id', 'price', 'deadstock', 'size', 'sup_id', 'unique_id']
        
    if table.upper() == 'SUPPLIERS':
        head = ['sup_id', 'sup_name', 'cut2', 'cut3', 'cut4', 'sup_sup']
        
    if table.upper() == 'BRANDS':
        head = ['brand', 'brand_id', 'site']
        
    if table.upper() == 'SNEAKERS':
        head = ['snkr_id', 'brand' , 'name', 'colortype']

    print('\n' + table +'\n')
    print(tabulate(results, headers=head, tablefmt='psql'))


if len(sys.argv) == 1:

    table = str(input("table name: "))

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM  "+ table)

    results = mycursor.fetchall()

    if table.upper() == 'STOCK':
        head = ['snkr_id', 'price', 'deadstock', 'size', 'sup_id', 'unique_id']
        
    if table.upper() == 'SUPPLIERS':
        head = ['sup_id', 'sup_name', 'cut2', 'cut3', 'cut4', 'sup_sup']
        
    if table.upper() == 'BRANDS':
        head = ['brand', 'brand_id', 'site']
        
    if table.upper() == 'SNEAKERS':
        head = ['snkr_id', 'brand' , 'name', 'colortype']

    print('\n' + table +'\n')
    print(tabulate(results, headers=head, tablefmt='psql'))
    print('\nNext time write table name(s) in the box ')