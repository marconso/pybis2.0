import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class pyBis(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('pyBIS2.0')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pybis = pyBis()
    app.exec()
