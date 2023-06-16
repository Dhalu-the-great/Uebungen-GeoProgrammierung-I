from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os

class fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        
        self.createLayout()
        self.createConnects()

    def createLayout(self):
        self.setWindowTitle("GUI-Programmierung")

        layout =QFormLayout()

        self.nameLineEdit = QLineEdit()
        self.VornameLineEdit = QLineEdit()
        self.save = QPushButton("Save")
        self.Datum = QDateEdit()
        self.adress = QLineEdit()
        self.PLZ = QLineEdit()
        self.ort = QLineEdit()
        self.countries = QComboBox()
        self.countries.addItems(["Schweiz","Deutschland","Österreich"])

        layout.addRow("Vorname:",self.VornameLineEdit)
        layout.addRow("Name:",self.nameLineEdit)
        layout.addRow("Geburtstag:",self.Datum)
        layout.addRow("Adresse:",self.adress)
        layout.addRow("Postleitzahl",self.PLZ)
        layout.addRow("Ort:",self.ort)
        layout.addRow("Land",self.countries)
        layout.addRow(self.save)

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        save = QAction("Save",self)
        quit = QAction("Quit",self)
        quit.triggered.connect(self.quit)
        save.triggered.connect(self.speichern)

        filemenu.addAction(save)
        filemenu.addAction(quit)
        
    



        center= QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()
    def createConnects(self):
        self.save.clicked.connect(self.speichern)
    
    def speichern(self):
        file = open("Output.txt","w", encoding="utf-8")
        file.write(f"{self.VornameLineEdit.text()},{self.nameLineEdit.text()},{self.Datum.text()},{self.adress.text()},{self.PLZ.text()},{self.ort.text()},{self.countries.currentText()}")
        file.close()
    def quit (self):
        print("Fenster geschlossen")
        self.close()
app= QApplication([])
win= fenster()
app.exec()