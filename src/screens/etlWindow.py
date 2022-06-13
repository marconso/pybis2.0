from PyQt5.QtWidgets import QWidget, QPushButton


class WidgetEtl(QWidget):
    def __init__(self):
        super().__init__()

        btn = QPushButton('texto', self)
        btn.clicked.connect(lambda: print('testando evento'))
