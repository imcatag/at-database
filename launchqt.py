import os
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QFont


def launch1():
    os.system("python 1.py")
    
def launch2():
    os.system("python 2.py")

def launch3():
    os.system("python 3.py")
    
def launch4():
    os.system("python 4.py")
    
def launch5():
    os.system("python 5.py")
    
def launch6():
    os.system("python 6.py")
    
def launch7():
    os.system("python 7.py")
    
def launch8():
    os.system("python 8.py")
    
def launch9():
    os.system("python 9.py")
    
def launch10():
    os.system("python 10.py")
    
def launch11():
    os.system("python 11.py")
   
def reset():
    os.system("python reset.py")

def st():
    os.system("python st1.py")
    
def cbr():
    os.system("python cbr.py")
    
def csn():
    os.system("python csn.py")
    
def desc():
    os.system("python describetables.py")
    
def addtostock():
    os.system("python addtostock.py")
    
def uidsearch():
    os.system("python uidsearch.py")
    
def delstock():
    os.system("python delstock.py")
    
def selsneak():
    os.system("python selsneak.py")

def openthedoc():
    os.system("google-chrome-stable bonk.pdf &> /dev/null") 
    
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("bonk")
        self.setGeometry(100,100,500,400)
 
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
        self.groupBox = QGroupBox("Choose. NOW.")
        self.groupBox.setFont(QFont("Roboto", 13))
        gridLayout = QGridLayout()
 
        button1 = QPushButton("1", self)
        button1.clicked.connect(launch1)
        gridLayout.addWidget(button1, 1,0)

        button2 = QPushButton("2", self)
        button2.clicked.connect(launch2)
        gridLayout.addWidget(button2, 2,0)
        
        button3 = QPushButton("3", self)
        button3.clicked.connect(launch3)
        gridLayout.addWidget(button3, 3,0)
        
        button4 = QPushButton("4", self)
        button4.clicked.connect(launch4)
        gridLayout.addWidget(button4, 4,0)
        
        button5 = QPushButton("5", self)
        button5.clicked.connect(launch5)
        gridLayout.addWidget(button5, 5,0)
        
        button6 = QPushButton("6", self)
        button6.clicked.connect(launch6)
        gridLayout.addWidget(button6, 6,0)
        
        button7 = QPushButton("7", self)
        button7.clicked.connect(launch7)
        gridLayout.addWidget(button7, 7,0)
        
        button8 = QPushButton("8", self)
        button8.clicked.connect(launch8)
        gridLayout.addWidget(button8, 8,0)
        
        button9 = QPushButton("9", self)
        button9.clicked.connect(launch9)
        gridLayout.addWidget(button9, 9,0)

        button10 = QPushButton("10", self)
        button10.clicked.connect(launch10)
        gridLayout.addWidget(button10, 10,0)
        
        #button11 = QPushButton("11", self)
        #button11.clicked.connect(launch11)
        #gridLayout.addWidget(button11, 11,0)
        
        labelQUERRIES = QLabel()
        labelQUERRIES.setText("QUERRIES")
        gridLayout.addWidget(labelQUERRIES, 0,0)
         
        labelDATABASE = QLabel()
        labelDATABASE.setText("DATABASE")
        gridLayout.addWidget(labelDATABASE, 0,1)

        buttonRESET = QPushButton("RESET", self)
        buttonRESET.clicked.connect(reset)
        gridLayout.addWidget(buttonRESET, 1,1)
        
        buttonST = QPushButton("SHOW TABLES", self)
        buttonST.clicked.connect(st)
        gridLayout.addWidget(buttonST, 2,1)
        
        buttonCBR = QPushButton("CREATE BRAND", self)
        buttonCBR.clicked.connect(cbr)
        gridLayout.addWidget(buttonCBR, 3,1)
        
        buttonCSN = QPushButton("CREATE SNEAKER", self)
        buttonCSN.clicked.connect(csn)
        gridLayout.addWidget(buttonCSN, 4,1)
        
        buttonADD = QPushButton("ADD SNEAKER TO STOCK", self)
        buttonADD.clicked.connect(addtostock)
        gridLayout.addWidget(buttonADD, 5,1)
        
        buttonDELSTOCK = QPushButton("SELECT / DELETE FROM STOCK", self)
        buttonDELSTOCK.clicked.connect(delstock)
        gridLayout.addWidget(buttonDELSTOCK, 6,1)
        
        buttonSELSNEAK = QPushButton("SELECT FROM SNEAKERS", self)
        buttonSELSNEAK.clicked.connect(selsneak)
        gridLayout.addWidget(buttonSELSNEAK, 7,1)
        
        buttonOPENDOCS = QPushButton("OPEN DOCUMENTATION", self)
        buttonOPENDOCS.clicked.connect(openthedoc)
        gridLayout.addWidget(buttonOPENDOCS, 8,1)

        buttonUID = QPushButton("UNIQUE ID SEARCH", self)
        buttonUID.clicked.connect(uidsearch)
        gridLayout.addWidget(buttonUID, 9,1)
        
        buttonCSN = QPushButton("DESCRIBE TABLES", self)
        buttonCSN.clicked.connect(desc)
        gridLayout.addWidget(buttonCSN, 10,1)
        
        self.groupBox.setLayout(gridLayout)
 
 
 

 
myapp = QApplication(sys.argv)
window = Window()
 
 
myapp.exec()
sys.exit()

app = QApplication(sys.argv)

app.exec_()