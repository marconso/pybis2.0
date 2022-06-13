from PyQt5.QtWidgets import (
    QWidget, QPushButton, QComboBox, QGridLayout, QDateTimeEdit
)
from PyQt5.QtCore import QDateTime, QDate


class WidgetDownload(QWidget):
    def __init__(self):
        super().__init__()

        self.drawLayout()

    def drawLayout(self):
        grid_combobox = QGridLayout()
        grid_buttons = QGridLayout()
        main_layout = QGridLayout(self)

        self.cbbxServer = QComboBox()
        self.cbbxData = QComboBox()
        self.cbbxLocal = QComboBox()
        self.cbbxLocal_ = QComboBox()

        grid_combobox.addWidget(self.cbbxServer, 0, 0)
        grid_combobox.addWidget(self.cbbxData, 1, 0)
        grid_combobox.addWidget(self.cbbxLocal, 0, 1)
        grid_combobox.addWidget(self.cbbxLocal_, 1, 1)

        self.btnDownload = QPushButton('Download')
        self.btnView = QPushButton('Preview')
        self.btnStop = QPushButton('Stop')

        grid_buttons.addWidget(self.btnDownload, 0, 0)
        grid_buttons.addWidget(self.btnView, 0, 1)
        grid_buttons.addWidget(self.btnStop, 0, 2)

        self.dtMin = QDateTimeEdit(QDate(2020, 1, 1))
        self.dtMin.setDateRange(QDate(2020, 1, 1), QDate.currentDate())
        self.dtMin.setDisplayFormat('yyyy-MM-dd')

        self.dtMax = QDateTimeEdit(QDate.currentDate())
        self.dtMax.setDateRange(QDate(2020, 1, 1), QDate.currentDate())
        self.dtMax.setDisplayFormat('yyyy-MM-dd')

        grid_buttons.addWidget(self.dtMin, 3, 2)
        grid_buttons.addWidget(self.dtMax, 3, 3)

        main_layout.addLayout(grid_combobox, 0, 0)
        main_layout.addLayout(grid_buttons, 1, 0)
