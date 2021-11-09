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
        
        labelBrand = QLabel()
        labelBrand.setText("Brand")
        gridLayout.addWidget(labelBrand, 1,0)
        
        labelName = QLabel()
        labelName.setText("Name")
        gridLayout.addWidget(labelName, 2,0)
        
        labelColortype = QLabel()
        labelColortype.setText("Colorway")
        gridLayout.addWidget(labelColortype, 3,0)
        
        brandbox = QLineEdit("",self)
        namebox = QLineEdit("",self)
        colortypebox = QLineEdit("",self)
        
        gridLayout.addWidget(brandbox, 1,1)
        gridLayout.addWidget(namebox, 2,1)
        gridLayout.addWidget(colortypebox, 3,1)
        
        buttonST1 = QPushButton("ADD IT", self)
        buttonST1.clicked.connect(lambda: do_thing())
        gridLayout.addWidget(buttonST1, 4,0)
        
        self.groupBox.setLayout(gridLayout)
        
        def do_thing():
            brand1 = brandbox.text()
            name1 = namebox.text()
            colortype1 = colortypebox.text()
            
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pw12",
            database="bonk"
            )
            
            mycursor = mydb.cursor(buffered=True)
            
            mycursor.execute("SELECT brand_id FROM brands WHERE brand=" + '\'' + brand1 + '\'')
            
            results = mycursor.fetchall()
            
            brand_id = results[0][0]
            
            mycursor = mydb.cursor(buffered=True)
            
            mycursor.execute("SELECT * FROM sneakers WHERE brand=\"" + brand1 + "\"")
            
            snkr_id = int(1000*brand_id) + int(mycursor.rowcount) + 1
            
            ins = (snkr_id, brand1, name1, colortype1)

            cod = "INSERT INTO sneakers(snkr_id, brand, name, colortype) VALUES(%s, %s, %s, %s)"

            mycursor.execute(cod, ins)
            
            mydb.commit()
            
            print ("Entry inserted: ", ins)

 
myapp = QApplication(sys.argv)
window = Window()
 
 
myapp.exec_()
sys.exit()

app = QApplication(sys.argv)                                                                        

app.exec_()