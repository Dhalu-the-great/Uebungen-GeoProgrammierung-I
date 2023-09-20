from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from PyQt5.QtGui import *
import random

class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        file = open("Prüfung GP1/weisheiten.txt","r", encoding="utf-8")
        content=file.read()
        text=content.split("\n")
        file.close()
        inhalt=random.choice(text)
        self.layout=QVBoxLayout()
        self.Button1=QPushButton("OK")
        self.text=QLabel(inhalt)
        
        
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.Button1)

        self.center= QWidget()
        self.center.setLayout(self.layout)

        self.setCentralWidget(self.center)

        self.Button1.clicked.connect(self.ende)

        self.show()

    def ende (self):
        self.close()



        






app = QApplication([])
win = UIFenster()
app.exec_()