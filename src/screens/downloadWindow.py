import tempfile
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QComboBox, QGridLayout, QDateTimeEdit, QLabel,
    QTableWidget, QSpinBox, QFormLayout, QGroupBox
)
from PyQt5.QtCore import QDate


class WidgetDownload(QWidget):
    def __init__(self):
        super().__init__()

        self.drawLayout()

    def drawLayout(self):
        group_options_download = QGroupBox('Download options')
        group_buttons = QGroupBox('Magick')
        group_options_pyspark = QGroupBox('Pyspark options')
        group_table = QGroupBox('Table preview')

        layout_config_api = QGridLayout()
        layout_selector = QFormLayout()
        layout_buttons = QGridLayout()
        layout_table = QGridLayout()

        group_options_download.setLayout(layout_config_api)
        group_options_pyspark.setLayout(layout_selector)
        group_buttons.setLayout(layout_buttons)
        group_table.setLayout(layout_table)

        main_layout = QGridLayout(self)

        self.cbbxServer = QComboBox()

        self.cbbxData = QComboBox()
        self.cbbxSubData = QComboBox()

        self.cbbxLocal = QComboBox()
        self.cbbxLocal_ = QComboBox()

        self.dtMin = QDateTimeEdit(QDate(2020, 1, 1))
        self.dtMin.setDateRange(QDate(2020, 1, 1), QDate.currentDate())
        self.dtMin.setDisplayFormat('yyyy-MM-dd')
        self.dtMax = QDateTimeEdit(QDate.currentDate())
        self.dtMax.setDateRange(QDate(2020, 1, 1), QDate.currentDate())
        self.dtMax.setDisplayFormat('yyyy-MM-dd')

        layout_config_api.addWidget(QLabel('Select server'), 0, 0, 1, 2)
        layout_config_api.addWidget(self.cbbxServer, 1, 0, 1, 2)

        layout_config_api.addWidget(QLabel('Data'), 2, 0)
        layout_config_api.addWidget(self.cbbxData, 3, 0)

        layout_config_api.addWidget(QLabel('Sub-Data'), 4, 0)
        layout_config_api.addWidget(self.cbbxSubData, 5, 0)

        layout_config_api.addWidget(QLabel('Select your region'), 2, 1)
        layout_config_api.addWidget(self.cbbxLocal, 3, 1)

        layout_config_api.addWidget(QLabel('Select your sub-region'), 4, 1)
        layout_config_api.addWidget(self.cbbxLocal_, 5, 1)

        layout_config_api.addWidget(QLabel('Set interval time'), 6, 0)
        layout_config_api.addWidget(self.dtMin, 7, 0)
        layout_config_api.addWidget(self.dtMax, 7, 1)

        self.btnDownload = QPushButton('Download')
        self.btnView = QPushButton('Preview')
        self.btnStop = QPushButton('Stop')

        layout_buttons.addWidget(self.btnDownload, 1, 0)
        layout_buttons.addWidget(self.btnView, 2, 0)
        layout_buttons.addWidget(self.btnStop, 3, 0)

        self.spinCores = QSpinBox()
        self.spinMemory = QSpinBox()
        self.selectFolder = QPushButton(tempfile.gettempdir())

        layout_selector.addWidget(QLabel('Cores'))
        layout_selector.addWidget(self.spinCores)
        layout_selector.addWidget(QLabel('RAM'))
        layout_selector.addWidget(self.spinMemory)
        layout_selector.addWidget(QLabel('Temp dir'))
        layout_selector.addWidget(self.selectFolder)

        self.table = QTableWidget(20, 200)

        layout_table.addWidget(self.table, 0, 0)

        main_layout.addWidget(group_options_download, 0, 0)

        main_layout.addWidget(group_buttons, 0, 1)#, 1, 2)

        main_layout.addWidget(group_table, 2, 0, 1, 2)
