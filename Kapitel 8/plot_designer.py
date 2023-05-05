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
        loadUi("Kapitel 8/plot.ui",self)

        figure=plt.figure(figsize=(16,9))
        self.canevas=FigureCanevas(figure)
        self.formLayout.removeWidget(self.widget)
        self.formLayout.addWidget(self.canevas)
        self.button1.clicked.connect(self.plot)

        self.show()

    def plot(self):
        plt.clf()
        minima=self.min.text()
        maxima=self.max.text()
        werte=self.anz.text()
        minima=minima.replace("sin","np.sin")
        minima=minima.replace("cos","np.cos")
        minima=minima.replace("e","np.e")
        minima=minima.replace("pi","np.pi")
        maxima=maxima.replace("sin","np.sin")
        maxima=maxima.replace("cos","np.cos")1-
        maxima=maxima.replace("e","np.e")
        maxima=maxima.replace("pi","np.pi")
        werte=werte.replace("sin","np.sin")
        werte=werte.replace("cos","np.cos")
        werte=werte.replace("e","np.e")
        werte=werte.replace("pi","np.pi")

        try:
            x=np.linspace(eval(minima),eval(maxima),eval(werte))

        except:
            QMessageBox.critical(self,"Fehler","Bitte Eingabe Überprüfen")
            return
        f=self.funktion.text()
        f=f.replace("sin","np.sin")
        f=f.replace("cos","np.cos")
        f=f.replace("e","np.e")
        f=f.replace("pi","np.pi")
        f=f.replace("^","**")
        try:
            y=eval(f)
        except:
            QMessageBox.critical(self,"Fehler","Bitte Eingabe Überprüfen")
            return

        plt.plot(x,y,"bo-")
        plt.axis("equal")
        self.canevas.draw()






app = QApplication([])
win = fenster()
app.exec_()
