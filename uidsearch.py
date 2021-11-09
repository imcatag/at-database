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
        labelId.setText("id")
        gridLayout.addWidget(labelId, 1,0)
        
        idbox = QLineEdit("",self)
        gridLayout.addWidget(idbox, 1,1)
        idbox.returnPressed.connect(lambda: do_thing())

        buttonST1 = QPushButton("SEARCH", self)
        buttonST1.clicked.connect(lambda: do_thing())
        gridLayout.addWidget(buttonST1, 8,0)
        
        self.groupBox.setLayout(gridLayout)
        
        def do_thing():
            id1 = idbox.text()
            
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pw12",
            database="bonk"
            )
            
            mycursor = mydb.cursor(buffered=True)
            
            mycursor.execute("SELECT * FROM STOCK WHERE unique_id = \'" + id1 + "\'")
            
            results = mycursor.fetchall()
            
            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM information_schema.columns WHERE table_name= \'stock\'")

            curs2 = mycursor.fetchall()

            #print (headers)

            head = ['snkr_id', 'price', 'deadstock', 'size', 'sup_id', 'unique_id']


            print(tabulate(results, headers=head, tablefmt='psql'))


 
myapp = QApplication(sys.argv)
window = Window()
 
 
myapp.exec_()
sys.exit()

app = QApplication(sys.argv)                                                                        

app.exec_()