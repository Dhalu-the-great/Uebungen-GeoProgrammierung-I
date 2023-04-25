from PyQt5.QtWidgets import *

class fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fenster")

        self.widget=QWidget()
        layouth=QHBoxLayout(self.widget)
        
        
        self.Frage=QLabel("Ist dieses Datum in Ordnung?")
        self.kalender=QCalendarWidget()
        self.Ja=QPushButton("Ja")
        self.Nein=QPushButton("Nein")
        self.Abbrechen=QPushButton("Abbrechen")
        layouth.addWidget(self.Ja)
        layouth.addWidget(self.Nein)
        layouth.addWidget(self.Abbrechen)
        layout=QFormLayout()
        self.setLayout(layout)

        layout.addRow(self.kalender)
        layout.addRow(self.Frage)
        layout.addRow(self.widget) 

        
        




        center= QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

app= QApplication([])
win= fenster()
app.exec()