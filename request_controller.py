from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow
from request_view import Ui_MainWindow
from NCBI_functions import *
from graphics_function import *
from functools import partial


class Request(QMainWindow, Ui_MainWindow):
    """
    controlling class for request_view
    """

    def __init__(self, parent=None):
        super(Request, self).__init__(parent)
        self.setupUi(self)
        self.field_list_nucleotide = get_field_list("nucleotide")
        self.init_ui()

    def init_ui(self):
        fill_combobox(self.combobox_0, self.field_list_nucleotide)
        self.button_remove_0.clicked.connect(partial(self.button_remove_clicked, 0))

    def button_add_clicked(self):
        position = self.layout_filters.count()
        self.add_layout_filter(position)

    def button_remove_clicked(self, number):
        self.remove_layout_filter(number)

    def add_layout_filter(self, position):
        layout = QtWidgets.QHBoxLayout()
        layout.setObjectName("layout_widget_" + str(position))

        combobox = QtWidgets.QComboBox()
        combobox.setObjectName("combobox_" + str(position))
        fill_combobox(combobox, self.field_list_nucleotide)

        edit = QtWidgets.QLineEdit()
        edit.setObjectName("edit_value_" + str(position))

        button_remove = QtWidgets.QToolButton()
        button_remove.setText("-")
        button_remove.setObjectName("button_remove_" + str(position))
        button_remove.clicked.connect(partial(self.button_remove_clicked, position))

        button_add = self.button_add

        layout.addWidget(combobox)
        layout.addWidget(edit)
        layout.addWidget(button_remove)
        layout.addWidget(button_add)

        self.layout_filters.addLayout(layout)

    def remove_layout_filter(self, position):
        if self.layout_filters.count() > 1:
            layout = self.layout_filters.itemAt(position)
            number_item = layout.count()
            for index in reversed(range(number_item)):
                widget = layout.itemAt(index).widget()
                if widget is not self.button_add:
                    widget.setParent(None)
                else:
                    layout_before = self.layout_filters.itemAt(position-1)
                    layout_before.addWidget(self.button_add)
            layout.setParent(None)