from PyQt5.QtWidgets import *

class fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout")

        layout=QVBoxLayout()

        Button1=QPushButton("Button 1")
        Button2=QPushButton("Button 2")
        Button3=QPushButton("Button 3")
        Button4=QPushButton("Button 4")
        Button5=QPushButton("Button 5")
        label=QLabel("Hello World")
        linedit=QLineEdit()
        kalender=QCalendarWidget()

        layout.addWidget(Button1)
        layout.addWidget(Button2)
        layout.addWidget(Button3)
        layout.addWidget(Button4)
        layout.addWidget(Button5)
        layout.addWidget(label)
        layout.addWidget(linedit)
        layout.addWidget(kalender)

        center= QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()


app= QApplication([])
win= fenster()
app.exec()