from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanevas
import matplotlib.pyplot as plt
import numpy as np
import math


class fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.createLayout()
        self.createConnects()

    def createLayout(self):
        self.setWindowTitle("Traglast Berechner")
        layout=QFormLayout()

        self.button=QPushButton("Berechnen")
        self.laenge=QLineEdit()
        self.breite=QLineEdit()
        self.hoehe=QLineEdit()
        self.FmaxBew=QLineEdit()
        self.FmaxBet=QLineEdit()
        self.Durchmesser=QLineEdit()
        self.unterseite=QLineEdit()
        self.anzahl=QLineEdit()
        self.maxF=QLabel()

        layout.addRow("Laenge[mm]",self.laenge)
        layout.addRow("Breite[mm]",self.breite)
        layout.addRow("Hoehe[mm]",self.hoehe)
        layout.addRow("Fmax Beton[N/mm2]",self.FmaxBet)
        layout.addRow("Fmax Bewehrung [N/mm2]",self.FmaxBew)
        layout.addRow("Durchmesser[mm]",self.Durchmesser)
        layout.addRow("Unterseite[mm]",self.unterseite)
        layout.addRow("Anzahl",self.anzahl)
        layout.addRow("Maximale Kraft F [N]",self.maxF)

        layout.addRow(self.button)

        center= QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

    def createConnects(self):
        self.button.clicked.connect(self.calculate)

    def calculate(self):
        self.maxF.setText(str(((((int(self.hoehe.text()))-
                                  (int(self.unterseite.text()))-
                                  (((((((((int(self.Durchmesser.text()))/2)**2)*math.pi)*(int(self.anzahl.text())))*(int(self.FmaxBew.text())))/(int(self.FmaxBet.text())))/int(self.breite.text()))/2))
                                  /1000)*
                                  (((((((int(self.Durchmesser.text()))/2)**2)*math.pi)*(int(self.anzahl.text())))*(int(self.FmaxBew.text())))))*
                                  (((int(self.laenge.text()))/3)/1000)))
        print("Hello world")

app = QApplication([])
win = fenster()
app.exec_()
