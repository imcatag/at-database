import os
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QFont
import mysql.connector
from tabulate import tabulate


        
class Window(QWidget):

    s = 'bruh'
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("bonk")
        self.setGeometry(620,100,500,400)
 
        self.setIcon()
 
        self.createGridLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
 
        self.show()
 
 
 
    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)
 
    
    def createGridLayout(self):
        self.groupBox = QGroupBox("FILL IN THE BLANKS")
        self.groupBox.setFont(QFont("Sanserif", 13))
        gridLayout = QGridLayout()
        
        labelId = QLabel()
        labelId.setText("sneaker id")
        gridLayout.addWidget(labelId, 1,0)
        
        labelPrice = QLabel()
        labelPrice.setText("price")
        gridLayout.addWidget(labelPrice, 2,0)
        
        labelDeadstock = QLabel()
        labelDeadstock.setText("deadstock")
        gridLayout.addWidget(labelDeadstock, 3,0)
        
        labelSize = QLabel()
        labelSize.setText("size")
        gridLayout.addWidget(labelSize, 4,0)
        
        labelSupplier = QLabel()
        labelSupplier.setText("supplier id")
        gridLayout.addWidget(labelSupplier, 5,0)
        
        labelUID = QLabel()
        labelUID.setText("unique id")
        gridLayout.addWidget(labelUID, 6,0)
        
        idbox = QLineEdit("",self)
        pricebox = QLineEdit("",self)
        deadstockbox = QLineEdit("",self)
        sizebox = QLineEdit("",self)
        supplierbox = QLineEdit("",self)
        uidbox = QLineEdit("",self)
        
        gridLayout.addWidget(idbox, 1,1)
        gridLayout.addWidget(pricebox, 2,1)
        gridLayout.addWidget(deadstockbox, 3,1)
        gridLayout.addWidget(sizebox, 4,1)
        gridLayout.addWidget(supplierbox, 5,1)
        gridLayout.addWidget(uidbox, 6,1)
        
        buttonST1 = QPushButton("DELETE", self)
        buttonST1.clicked.connect(lambda: do_thing_delete())
        gridLayout.addWidget(buttonST1, 9,0)
        
        labelDEL = QLabel()
        labelDEL.setText("WARNING: Deletion cannot be undone!")
        gridLayout.addWidget(labelDEL, 9,1)
        
        buttonST2 = QPushButton("SELECT", self)
        buttonST2.clicked.connect(lambda: do_thing_select())
        gridLayout.addWidget(buttonST2, 8,0)
        
        self.groupBox.setLayout(gridLayout)
        
        def do_thing_delete():
            id1 = idbox.text()
            price1 = pricebox.text()
            deadstock1 = deadstockbox.text()
            size1 = sizebox.text()
            supplier1 = supplierbox.text()
            uid1 = uidbox.text()
            
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pw12",
            database="bonk"
            )
            
            cond = " "
            movetoand = False
            
            
            if id1.strip():
                cond += (" WHERE snkr_id = " + id1)
                movetoand = True
            
            if price1.strip():
                if not movetoand:
                    cond += (" WHERE price = " + price1)
                    movetoand = True
                else:
                    cond += (" AND price = " + price1)
            
            if deadstock1.strip():
                if not movetoand:
                    cond += (" WHERE deadstock = " + deadstock1)
                    movetoand = True
                else:
                    cond += (" AND deadstock = " + deadstock1)
                
            if size1.strip():
                if not movetoand:
                    cond += (" WHERE size = " + size1 )
                    movetoand = True
                else:
                    cond += (" AND size = " + size1)
                
            if supplier1.strip():
                if not movetoand:
                    cond += (" WHERE sup_id = " + supplier1)
                    movetoand = True
                else:
                    cond += (" AND sup_id = " + supplier1)
                
            if uid1.strip():
                if not movetoand:
                    cond += (" WHERE unique_id = " + uid1)
                    movetoand = True
                else:
                    cond += (" AND unique_id = " + uid1)
                
            mycursor = mydb.cursor(buffered=True)

            mycursor.execute("DELETE FROM stock " + cond)
            
            mydb.commit()
            
            #print("DELETE FROM stock " + cond)
            
            print("DELETED")
            

        def do_thing_select():
            id1 = idbox.text()
            price1 = pricebox.text()
            deadstock1 = deadstockbox.text()
            size1 = sizebox.text()
            supplier1 = supplierbox.text()
            uid1 = uidbox.text()
            
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pw12",
            database="bonk"
            )
            
            cond = " "
            movetoand = False
            
            
            if id1.strip():
                cond += (" WHERE snkr_id = " + id1)
                movetoand = True
            
            if price1.strip():
                if not movetoand:
                    cond += (" WHERE price = " + price1)
                    movetoand = True
                else:
                    cond += (" AND price = " + price1)
            
            if deadstock1.strip():
                if not movetoand:
                    cond += (" WHERE deadstock = " + deadstock1)
                    movetoand = True
                else:
                    cond += (" AND deadstock = " + deadstock1)
                
            if size1.strip():
                if not movetoand:
                    cond += (" WHERE size = " + size1 )
                    movetoand = True
                else:
                    cond += (" AND size = " + size1)
                
            if supplier1.strip():
                if not movetoand:
                    cond += (" WHERE sup_id = " + supplier1)
                    movetoand = True
                else:
                    cond += (" AND sup_id = " + supplier1)
                
            if uid1.strip():
                if not movetoand:
                    cond += (" WHERE unique_id = " + uid1)
                    movetoand = True
                else:
                    cond += (" AND unique_id = " + uid1)
                
            mycursor = mydb.cursor(buffered=True)

            mycursor.execute("SELECT * FROM stock " + cond)
            
            head = ['snkr_id', 'price', 'deadstock', 'size', 'sup_id', 'unique_id']
            
            results = mycursor.fetchall()
            #print("SELECT * FROM stock " + cond)
            print(tabulate(results, headers=head, tablefmt='psql'))
 
myapp = QApplication(sys.argv)
window = Window()
 
 
myapp.exec_()
sys.exit()

app = QApplication(sys.argv)                                                                        

app.exec_()