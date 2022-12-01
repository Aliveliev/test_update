from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from updater import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.resize(250, 250)

        button = QPushButton('Update', self)
        button.move(50,50)
        button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        updateNow()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = MainWindow()

    sys.exit(app.exec_())