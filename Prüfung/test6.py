from PyQt5.QtWidgets import *

class fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.createLayout()
        self.createConnects()

    def createLayout(self):
        self.setWindowTitle("Währungsumrechner")

        layout=QFormLayout()
        self.umrechnen=QPushButton("Umrechnen")
        self.CHF=QLineEdit()
        self.EUR=QLabel()

        layout.addRow("Schweizer Franken",self.CHF)
        layout.addRow("Euro:",self.EUR)
        layout.addRow(self.umrechnen)


    

        center= QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()
    def createConnects(self):
        self.umrechnen.clicked.connect(self.rechner)

    def rechner (self):
        self.EUR.setText(str((int((self.CHF.text()))/100)*87.60))

app= QApplication([])
win= fenster()
app.exec()