from PyQt5.QtWidgets import *

class fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout")

        layout=QVBoxLayout()



        center= QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

app= QApplication([])
win= fenster()
app.exec()