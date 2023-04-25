from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from PyQt5.QtGui import *


class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel 6/Showmap.ui", self)
        self.show()
        
        self.anzeigen.clicked.connect(self.map)
        self.windows = []
    
    def map (self):
        link=f"https://www.google.ch/maps/place/{self.lat.text()},{self.lon.text()}"
        QDesktopServices.openUrl(QUrl(link))


app = QApplication([])
win = UIFenster()
app.exec_()

