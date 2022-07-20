#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from src.screens.managerWindow import VerticalTabWidget
from src.screens.downloadWindow import WidgetDownload
from src.screens.etlWindow import WidgetEtl


class pyBis(QMainWindow):
    def __init__(self):
        super().__init__()

        tabs = VerticalTabWidget()
        tabs.addTab(WidgetDownload(), 'Download')
        tabs.addTab(WidgetEtl(), 'Etl')

        self.setCentralWidget(tabs)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pybis = pyBis()
    app.exec()
