import os
import tempfile
import json
from PySide6.QtWidgets import (
    QWidget, QPushButton, QComboBox, QGridLayout, QDateTimeEdit, QLabel,
    QTableWidget, QSpinBox, QFormLayout, QGroupBox
)
from PySide6.QtCore import QDate


class WidgetDownload(QWidget):

    confjson = os.path.join(os.path.dirname(__file__), '../config/conf.json')

    def __init__(self):
        super().__init__()

        self.drawLayout()
        self.data = self.loadConfig(self.confjson)
        self.load_combobox()

    def load_combobox(self):
        self.cbbxServer.addItems(sorted(self.data['SERVER']))
        self.cbbxData.addItems(
            sorted(self.data['SERVER'][self.cbbxServer.currentText()])
        )
        self.cbbxSubData.addItems(
            sorted(self.data['SERVER']
            [self.cbbxServer.currentText()]
            [self.cbbxData.currentText()])
        )

        self.cbbxLocal.addItems(sorted(self.data['DELIMITATION']))

        self.cbbxServer.currentTextChanged.connect(self.update_items_data)
        self.cbbxData.currentTextChanged.connect(self.update_items_sub_data)
        self.cbbxLocal.currentTextChanged.connect(
            self.update_items_delimitation
        )

    def update_items_delimitation(self, text):
        self.cbbxLocal_.clear()
        if text != "BRASIL":
            self.cbbxLocal_.show()
            self.select_sub_reg.show()
        else:
            self.select_sub_reg.hide()
            self.cbbxLocal_.hide()
        self.cbbxLocal_.addItems(sorted(self.data['DELIMITATION'][text]))

    def update_items_data(self, server):
        self.cbbxData.clear()
        self.cbbxData.addItems(sorted(self.data['SERVER'][server]))
        try:
            self.cbbxSubData.addItems(sorted(
                self.data['SERVER']
                [self.cbbxServer.currentText()]
                [self.cbbxSubData.currentText()])
            )
        except KeyError:
            pass

    def update_items_sub_data(self, data):
        self.cbbxSubData.clear()
        try:
            self.cbbxSubData.addItems(sorted(
                self.data['SERVER']
                [self.cbbxServer.currentText()][data])
            )
        except KeyError:
            pass

    def loadConfig(self, filejson):
        with open(filejson, 'r') as fjson:
            data = json.load(fjson)
            return data

    def drawLayout(self):
        group_options_download = QGroupBox('Download options')
        group_buttons = QGroupBox('Run options')
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

        self.cbbxServer = QComboBox(editable=True)

        self.cbbxData = QComboBox(editable=True)
        self.cbbxSubData = QComboBox(editable=True)

        self.cbbxLocal = QComboBox(editable=True)
        self.cbbxLocal_ = QComboBox(editable=True)
        self.cbbxLocal_.hide()

        self.dtMin = QDateTimeEdit(QDate(2010, 1, 1))
        self.dtMin.setDateRange(QDate(2010, 1, 1), QDate.currentDate())
        self.dtMin.setDisplayFormat('yyyy-MM-dd')
        self.dtMax = QDateTimeEdit(QDate.currentDate())
        self.dtMax.setDateRange(QDate(2010, 1, 1), QDate.currentDate())
        self.dtMax.setDisplayFormat('yyyy-MM-dd')

        layout_config_api.addWidget(QLabel('Select server'), 0, 0, 1, 2)
        layout_config_api.addWidget(self.cbbxServer, 1, 0, 1, 2)

        layout_config_api.addWidget(QLabel('Dataset'), 2, 0)
        layout_config_api.addWidget(self.cbbxData, 3, 0)

        layout_config_api.addWidget(QLabel('Table'), 4, 0)
        layout_config_api.addWidget(self.cbbxSubData, 5, 0)

        layout_config_api.addWidget(QLabel('Delimitation'), 2, 1)
        layout_config_api.addWidget(self.cbbxLocal, 3, 1)

        self.select_sub_reg = QLabel('Select your region')
        self.select_sub_reg.hide()

        layout_config_api.addWidget(self.select_sub_reg, 4, 1)
        layout_config_api.addWidget(self.cbbxLocal_, 5, 1)

        layout_config_api.addWidget(QLabel('Period'), 6, 0)
        layout_config_api.addWidget(self.dtMin, 7, 0)
        layout_config_api.addWidget(self.dtMax, 7, 1)

        self.btnDownload = QPushButton('Download')
        self.btnView = QPushButton('Preview')
        self.btnStop = QPushButton('Stop')

        layout_buttons.addWidget(self.btnDownload, 0, 1)#, 2, 1)
        layout_buttons.addWidget(self.btnView, 0, 2)#, 2, 1)
        layout_buttons.addWidget(self.btnStop, 0, 3)#, 2, 1)

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

        main_layout.addWidget(group_options_download, 0, 0, 1, 0)

        main_layout.addWidget(group_buttons, 1, 0, 1, 0)

        main_layout.addWidget(group_table, 2, 0, 1, 2)
