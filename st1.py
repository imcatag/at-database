import os
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QFont




        
class Window(QWidget):

    s = 'bruh'
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("bonk")
        self.setGeometry(620,100,500,200)
 
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
        self.groupBox.setFont(QFont("Sanserif", 13))
        gridLayout = QGridLayout()
        
        labelSPACING = QLabel()
        labelSPACING.setText("WRITE DATABASE NAMES WITH A SPACE IN BETWEEN")
        gridLayout.addWidget(labelSPACING, 0,0)
        
        textbox = QLineEdit("",self)
        textbox.returnPressed.connect(lambda: do_thing())
        
        gridLayout.addWidget(textbox, 1,0)
        
        buttonST1 = QPushButton("SHOW THEM TABLES", self)
        buttonST1.clicked.connect(lambda: do_thing())
        gridLayout.addWidget(buttonST1, 2,0)
        
        self.groupBox.setLayout(gridLayout)
        
        def do_thing():
            value = textbox.text()
            os.system("python st.py " + value)
            
    
 
 
myapp = QApplication(sys.argv)
window = Window()
 
 
myapp.exec_()
sys.exit()

app = QApplication(sys.argv)                                                                        

app.exec_()