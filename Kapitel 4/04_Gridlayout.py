from PyQt5.QtWidgets import *

class fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout")

        layout=QGridLayout()

        label1=QLabel("Vorname")
        label2=QLabel("Nachname")
        input1=QLineEdit()
        input2=QLineEdit()

        layout.addWidget(label1,0,0)
        layout.addWidget(input1,0,1)
        layout.addWidget(label2,1,0)
        layout.addWidget(input2,1,1)

        center= QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        self.show()

app= QApplication([])
win= fenster()
app.exec()