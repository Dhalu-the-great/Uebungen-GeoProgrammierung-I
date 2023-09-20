from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from PyQt5.QtGui import *

class Medienwahl(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("_Projekte Sommer/Medienwahl.ui", self)
        self.show()

        self.Ok.clicked.connect(self.laden)
        self.windows = []
    
    def laden(self):
        win=Checkliste()
        win.show()
        self.windows.append(win)
        self.close()
    

class Checkliste(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("_Projekte Sommer/Checkliste.ui", self)
        self.show()


app = QApplication([])
win = Medienwahl()
app.exec_()
