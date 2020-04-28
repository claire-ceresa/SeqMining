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
        self.list_layout_widget = [self.layout_widget_0]
        self.init_ui()

    def init_ui(self):
        fill_combobox(self.combobox_field_0, self.field_list_nucleotide)
        self.button_remove_0.clicked.connect(partial(self.button_remove_clicked, 0))

    def button_add_clicked(self):
        position = len(self.list_layout_widget)
        self.add_layout_filter(position)

    def button_remove_clicked(self, number):
        try:
            self.remove_layout_filter(number)
        except Exception as e:
            print(e)

    def button_create_clicked(self):
        return

    def add_layout_filter(self, position):
        layout = QtWidgets.QHBoxLayout()
        layout.setObjectName("layout_widget_" + str(position))

        combobox_field = QtWidgets.QComboBox()
        combobox_field.setObjectName("combobox_field_" + str(position))
        fill_combobox(combobox_field, self.field_list_nucleotide)

        combobox_link = QtWidgets.QComboBox()
        combobox_link.setObjectName("combobox_link_" + str(position))
        fill_combobox(combobox_link, ["AND", "OR","NOT"])

        edit = QtWidgets.QLineEdit()
        edit.setObjectName("edit_value_" + str(position))

        button_remove = QtWidgets.QToolButton()
        button_remove.setText("-")
        button_remove.setObjectName("button_remove_" + str(position))
        button_remove.clicked.connect(partial(self.button_remove_clicked, position))

        button_add = self.button_add

        layout.addWidget(combobox_link)
        layout.addWidget(combobox_field)
        layout.addWidget(edit)
        layout.addWidget(button_remove)
        layout.addWidget(button_add)

        self.layout_filters.addLayout(layout)
        self.list_layout_widget.append(layout)

    def remove_layout_filter(self, number):
        name_layout = "layout_widget_" + str(number)
        layout = next(l for l in self.list_layout_widget if l.objectName() == name_layout)
        position_layout = self.list_layout_widget.index(layout)

        if position_layout > 0:
            number_item = layout.count()

            for index in reversed(range(number_item)):

                widget = layout.itemAt(index).widget()
                if widget is not self.button_add:
                    widget.setParent(None)
                else:
                    layout_before = self.list_layout_widget[position_layout-1]
                    layout_before.addWidget(self.button_add)

            layout.setParent(None)
            del self.list_layout_widget[position_layout]
