import os

os.system("python dropdb.py")
os.system("python createdb.py")
os.system("python createtables.py")

os.system("python populate_brands.py")
os.system("python populate_suppliers.py")
os.system("python populate_sneakers.py")
os.system("python populate_stock.py") 

print('\nDone!')