from PySide6.QtWidgets import QApplication, QWidget , QVBoxLayout, QPushButton, QGroupBox, QGridLayout
import sys
from PySide6.QtGui import QIcon, QFont
 
 
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Grid Layout")
        self.setGeometry(300,200,500,400)
 
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
        self.groupBox = QGroupBox("Please Choose One Language")
        self.groupBox.setFont(QFont("Sanserif", 13))
        gridLayout = QGridLayout()
 
        button = QPushButton("C++", self)
        button.setIcon(QIcon("cpp.png"))
        gridLayout.addWidget(button, 0,0)
 
 
        button1 = QPushButton("CSS", self)
        button1.setIcon(QIcon("css.png"))
        gridLayout.addWidget(button1, 0, 1)
 
        button2 = QPushButton("javascript", self)
        button2.setIcon(QIcon("javascript.png"))
        gridLayout.addWidget(button2, 1, 0)
 
        button3 = QPushButton("C#", self)
        button3.setIcon(QIcon("csharp.png"))
        gridLayout.addWidget(button3, 1, 1)
 
        button4 = QPushButton("Python", self)
        button4.setIcon(QIcon("pythonicon.png"))
        gridLayout.addWidget(button4, 2, 0)
 
        button5 = QPushButton("Java", self)
        button5.setIcon(QIcon("java.png"))
        gridLayout.addWidget(button5, 2, 1)
 
        self.groupBox.setLayout(gridLayout)
 
 
 
 
 
myapp = QApplication(sys.argv)
window = Window()
 
 
myapp.exec_()
sys.exit()