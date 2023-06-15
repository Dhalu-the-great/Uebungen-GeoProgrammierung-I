class person():
    def __init__(self,Name="Hans-Peter",Alter=35,Adresse="FHNW"):
        self.name=Name
        self.alter=Alter
        self.adresse=Adresse

    def __str__(self):
        return f"Name: {self.name}, Alter: {self.alter}, Adresse: {self.adresse}"
    
    def print_info(self):
        print("Name: "+str(self.name)+", Alter: "+str(self.alter)+", Adresse: "+str(self.adresse))

fabian=person("Gross Fabian",21,"Hofackerstrasse 7")
fabian.print_info()
print(fabian)


class V2():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __sub__ (self,other):
        return V2(self.x-other.x,self.y-other.y)
    
    def __add__ (self,other):
        return V2(self.x+other.x,self.y+other.y)
    
    def __str__ (self):
        return f"X={self.x},Y={self.y}"

v1=V2(3,5)
v2=V2(7,9)
v3=v1-v2
v4=v3+v2

print(v3,v4)


class Shape():
    def __init__ (self,Name):
        self.name=Name
        def area(self):
            return None
        def umfang (self):
            return None
        def __str__ (self):
            return f"{self.name}"


class Rechteck(Shape):
    def __init__(self,x1,x2,y1,y2):
        super().__init__("Rechteck")
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2

    def area (self):
        return (self.x2-self.x1)*(self.y2-self.y1)
    

r1=Rechteck(2,4,3,6)
print(r1.area())

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanevas
import matplotlib.pyplot as plt
import numpy as np



class fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("prüfungsvorbereitung/gui.ui",self)

        self.setWindowTitle("Ui Dreck")

        self.pushButton.clicked.connect(self.drucken)
        self.pushButton_2.clicked.connect(self.load)
    
        self.show()

    def load (self):
        path , filter = QFileDialog.getOpenFileName(self,"Datei Öffnen","","Text Dateien (*.txt)")
        file = open(path,"r",encoding="utf-8")
        data=file.read()
        print(data)
    
    def drucken(self):
        print(self.lineEdit.text())



app = QApplication([])
win = fenster()
app.exec_()

