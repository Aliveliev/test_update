from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from updater import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.resize(250, 250)

        button = QPushButton('Update', self)
        button.move(50,50)
        button.clicked.connect(self.update)

        button = QPushButton('Exit', self)
        button.move(50,100)
        button.clicked.connect(self.close)

        self.show()

    def update(self):
        updateNow()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = MainWindow()

    sys.exit(app.exec_())