from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


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
        self.map = QPushButton("Auf Karte zeigen")
        self.load = QPushButton("Laden")

        layout.addRow("Vorname:",self.VornameLineEdit)
        layout.addRow("Name:",self.nameLineEdit)
        layout.addRow("Geburtstag:",self.Datum)
        layout.addRow("Adresse:",self.adress)
        layout.addRow("Postleitzahl",self.PLZ)
        layout.addRow("Ort:",self.ort)
        layout.addRow("Land",self.countries)
        layout.addRow(self.map)
        layout.addRow(self.load)
        layout.addRow(self.save)


        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        save = QAction("Save",self)
        quit = QAction("Quit",self)
        filemenu.addAction(save)
        filemenu.addAction(quit)
        quit.triggered.connect(self.quit)
        save.triggered.connect(self.speichern)
        filemenu =menubar.addMenu("View")
        map = QAction("Auf Karte Anzeigen",self)
        map.triggered.connect(self.karte)
        filemenu.addAction(map)

        

        
        
    



        center= QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()
    def createConnects(self):
        self.save.clicked.connect(self.speichern)
        self.map.clicked.connect(self.karte)
        self.load.clicked.connect(self.laden)
    
    def speichern(self):
        
        pfad, filter = QFileDialog.getSaveFileName(self,"Datei Speichern","","Text Dateien (*.txt)")
        
        file = open(pfad,"w", encoding="utf-8")
        file.write(f"{self.VornameLineEdit.text()},{self.nameLineEdit.text()},{self.Datum.text()},{self.adress.text()},{self.PLZ.text()},{self.ort.text()},{self.countries.currentText()}")
        file.close()

    def quit (self):
        print("Fenster geschlossen")
        self.close()
    def karte (self):
        link = f"https://www.google.ch/maps/place/{self.adress.text()}+{self.PLZ.text()}+{self.ort.text()}"
        QDesktopServices.openUrl(QUrl(link))
    
    def laden (self):
        path , filter = QFileDialog.getOpenFileName(self,"Datei Öffnen","","Text Dateien (*.txt)")
        file = open(path,"r",encoding="utf-8")
        data=file.read()
        list=data.split(",")
        self.VornameLineEdit.setText(list[0])
        self.nameLineEdit.setText(list[1])
        self.Datum.setDate(QDate.fromString(list[2],"dd/MM/yyyy"))
        self.adress.setText(list[3])
        self.PLZ.setText(list[4])
        self.ort.setText(list[5])
        self.countries.setCurrentText(list[6])
        file.close()
app= QApplication([])
win= fenster()
app.exec()
