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
        
        idbox = QLineEdit("",self)
        pricebox = QLineEdit("",self)
        deadstockbox = QLineEdit("",self)
        sizebox = QLineEdit("",self)
        supplierbox = QLineEdit("",self)
        
        
        gridLayout.addWidget(idbox, 1,1)
        gridLayout.addWidget(pricebox, 2,1)
        gridLayout.addWidget(deadstockbox, 3,1)
        gridLayout.addWidget(sizebox, 4,1)
        gridLayout.addWidget(supplierbox, 5,1)
        
        buttonST1 = QPushButton("ADD IT", self)
        buttonST1.clicked.connect(lambda: do_thing())
        gridLayout.addWidget(buttonST1, 8,0)
        
        self.groupBox.setLayout(gridLayout)
        
        def do_thing():
            id1 = idbox.text()
            price1 = pricebox.text()
            deadstock1 = deadstockbox.text()
            size1 = sizebox.text()
            supplier1 = supplierbox.text()
            
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pw12",
            database="bonk"
            )
            
            mycursor = mydb.cursor(buffered=True)
            
            ins = (id1, price1, deadstock1, size1, supplier1)

            cod = "INSERT INTO stock(snkr_id, price, deadstock, size, sup_id) VALUES(%s, %s, %s, %s, %s)"

            mycursor.execute(cod, ins)
            
            mydb.commit()
            
            mycursor.execute("SELECT LAST_INSERT_ID();")
            
            results = mycursor.fetchall()
            
            print ("Entry inserted: ", ins, " UNIQUE ID: ", results[0][0])
            


 
myapp = QApplication(sys.argv)
window = Window()
 
 
myapp.exec_()
sys.exit()

app = QApplication(sys.argv)                                                                        

app.exec_()