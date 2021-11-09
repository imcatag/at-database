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
        
        labelBrand = QLabel()
        labelBrand.setText("brand")
        gridLayout.addWidget(labelBrand, 2,0)
        
        labelName = QLabel()
        labelName.setText("name")
        gridLayout.addWidget(labelName, 3,0)
        
        labelColortype = QLabel()
        labelColortype.setText("colortype")
        gridLayout.addWidget(labelColortype, 4,0)

        idbox = QLineEdit("",self)
        brandbox = QLineEdit("",self)
        namebox = QLineEdit("",self)
        colortypebox = QLineEdit("",self)

        gridLayout.addWidget(idbox, 1,1)
        gridLayout.addWidget(brandbox, 2,1)
        gridLayout.addWidget(namebox, 3,1)
        gridLayout.addWidget(colortypebox, 4,1)
        
        buttonST2 = QPushButton("SELECT", self)
        buttonST2.clicked.connect(lambda: do_thing_select())
        gridLayout.addWidget(buttonST2, 6,0)
        
        self.groupBox.setLayout(gridLayout)
        
        def do_thing_select():
            id1 = idbox.text()
            brand1 = brandbox.text()
            name1 = namebox.text()
            colortype1 = colortypebox.text()
            
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
            
            if brand1.strip():
                if not movetoand:
                    cond += (" WHERE brand = \'" + brand1 + "\'")
                    movetoand = True
                else:
                    cond += (" AND brand = \'" + brand1 + "\'")
            
            if name1.strip():
                if not movetoand:
                    cond += (" WHERE name =  \'" + name1 + "\'")
                    movetoand = True
                else:
                    cond += (" AND name = \'" + name1 + "\'")
                
            if colortype1.strip():
                if not movetoand:
                    cond += (" WHERE colortype = \'" + colortype1 + "\'")
                    movetoand = True
                else:
                    cond += (" AND colortype = \'" + colortype1 + "\'")
                
            mycursor = mydb.cursor(buffered=True)

            mycursor.execute("SELECT * FROM sneakers " + cond + " ORDER BY name ASC")
            #print("SELECT * FROM sneakers " + cond + " ORDER BY name ASC")

            head = ['snkr_id', 'brand', 'name', 'colortype']
            
            results = mycursor.fetchall()

            print(tabulate(results, headers=head, tablefmt='psql'))
 
myapp = QApplication(sys.argv)
window = Window()
 
 
myapp.exec_()
sys.exit()

app = QApplication(sys.argv)                                                                        

app.exec_()