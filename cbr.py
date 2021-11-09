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
        labelBrand.setText("brand")
        gridLayout.addWidget(labelBrand, 1,0)
        
        labelId = QLabel()
        labelId.setText("id")
        gridLayout.addWidget(labelId, 2,0)
        
        labelSite = QLabel()
        labelSite.setText("site")
        gridLayout.addWidget(labelSite, 3,0)
        
        brandbox = QLineEdit("",self)
        idbox = QLineEdit("",self)
        sitebox = QLineEdit("",self)
        
        gridLayout.addWidget(brandbox, 1,1)
        gridLayout.addWidget(idbox, 2,1)
        gridLayout.addWidget(sitebox, 3,1)
        
        buttonST1 = QPushButton("ADD IT", self)
        buttonST1.clicked.connect(lambda: do_thing())
        gridLayout.addWidget(buttonST1, 4,0)
        
        self.groupBox.setLayout(gridLayout)
        
        def do_thing():
            brand1 = brandbox.text()
            id1 = idbox.text()
            site1 = sitebox.text()
            
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pw12",
            database="bonk"
            )
            
            mycursor = mydb.cursor(buffered=True)
            
            ins = (brand1, id1, site1)

            cod = "INSERT INTO brands(brand, brand_id, site) VALUES(%s, %s, %s)"

            mycursor.execute(cod, ins)
            
            mydb.commit()
            
            print ("Entry inserted: ", ins)

 
myapp = QApplication(sys.argv)
window = Window()
 
 
myapp.exec_()
sys.exit()

app = QApplication(sys.argv)                                                                        

app.exec_()