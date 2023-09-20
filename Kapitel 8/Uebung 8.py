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

        self.createLayout()
        self.createConnects()

    def createLayout(self):
        self.setWindowTitle("Polynom Funktion Plotter")
        layout=QFormLayout()

        self.button=QPushButton("Plotten")
        self.grad=QLineEdit()
        self.min=QLineEdit()
        self.max=QLineEdit()
        self.werte=QLineEdit()
        self.koef=QLineEdit()
        self.farben=QComboBox()
        self.farben.addItems(["Schwarz","Rot","Blau","Grün"])


        layout.addRow("Grad",self.grad)
        layout.addRow("X Min",self.min)
        layout.addRow("X Max",self.max)
        layout.addRow("Anzahl Werte",self.werte)
        layout.addRow("Koefizzienten",self.koef)
        layout.addRow(self.farben)
        layout.addRow(self.button)

        center= QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

    def createConnects(self):
        self.button.clicked.connect(self.plot)

    def plot(self):
        plt.close()
        if type(eval(self.koef.text()))!=list:
            QMessageBox.critical(self,"Fehler","Die koeffizienten müssen richtig formatiert werden [x1,x2,x3,...,xn]")
        
        else:
            f=np.poly1d(eval(self.koef.text()))
            
            if eval(self.min.text())>eval(self.max.text()):
                QMessageBox.critical(self,"Fehler","min wert muss kleiner als max wert sein")
            elif eval(self.werte.text())<0 or type(eval(self.werte.text()))!= int:
                QMessageBox.critical(self,"Fehler","Anzahl Werte muss eine positive ganze zahl sein")
            elif eval(self.grad.text())!= len(f):
                QMessageBox.critical(self,"Fehler","Die anzahl koeffizente muss dem grad entsprechen")
            else:
                try:
                    c=self.farben.currentText()
                    c=c.replace("Schwarz","k")
                    c=c.replace("Rot","r")
                    c=c.replace("Grün","g")
                    c=c.replace("Blau","b")
                    x=np.linspace(int(self.min.text()),int(self.max.text()),int(self.werte.text()))
                    y=f(x)
                    plt.plot(x,y,c+"o-")
                    plt.axis("equal")
                    plt.show()
                
                except:
                    QMessageBox.critical(self,"Fehler","Bitte Eingabe Überprüfen")
        





app = QApplication([])
win = fenster()
app.exec_()

print("hello world")