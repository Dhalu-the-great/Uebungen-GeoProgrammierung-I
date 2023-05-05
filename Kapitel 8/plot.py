from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanevas
import matplotlib.pyplot as plt
import numpy as np


class fenster(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Funktion")

        layout =QBoxLayout(QBoxLayout.TopToBottom)

        figure=plt.figure(figsize=(16,9))
        self.canevas = FigureCanevas(figure)

        self.button=QPushButton("f(x)")
        self.button2=QPushButton("sin(x)")

        layout.addWidget(self.canevas)
        layout.addWidget(self.button)
        layout.addWidget(self.button2)


    def plot1(self):
        plt.clf()
        x=np.linspace(-5,5,50)
        y=x**2
        plt.plot(x,y,"bo-")
        plt.axis("equal")
        self.canevas.draw()

    def plot2(self):
        plt.clf()
        x=np.linspace(-5,5,50)
        y=abs(np.sin(x))
        plt.plot(x,y,"bo-")
        plt.axis("equal")
        self.canevas.draw()


app = QApplication([])
win = fenster()
app.exec_()
