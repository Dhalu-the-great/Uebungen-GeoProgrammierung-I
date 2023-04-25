from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from PyQt5.QtGui import *
from random import randint

class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel 6/Layout.ui", self)
        self.show()

        self.ok.clicked.connect(self.click)
        self.windows = []

    def click(self):
        if self.ja.checkState()and self.nein.checkState()==False:
            win=Fenster()
            win.show()
            self.windows.append(win)

        elif self.ja.checkState()and self.nein.checkState():
            win=Fenster2()
            win.show()
            self.windows.append(win)
        elif self.ja.checkState()==False and self.nein.checkState()==False:
            win=Fenster2()
            win.show()
            self.windows.append(win)
        else:
            for i in range(1):
                win = Window()
                win.show()
                self.windows.append(win)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel 6/dummy.ui", self)
        self.ende.clicked.connect(self.fin)
        self.hilfe.clicked.connect(self.aide)

        self.windows = []

    def fin (self):
        self.close()
        for i in range(2):
                win = Window()
                win.show()
                self.windows.append(win)
    
    def aide (self):
        link="https://www.fhnw.ch/de/die-fhnw/it-support"
        QDesktopServices.openUrl(QUrl(link))
        
    
        
class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel 6/success.ui", self)

class Fenster2(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel 6/fail.ui", self)
        self.retry.clicked.connect(self.ende)

    def ende(self):
        self.close()



app = QApplication([])
win = UIFenster()
app.exec_()
