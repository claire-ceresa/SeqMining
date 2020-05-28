from datetime import datetime
from PyQt5 import QtWidgets, QtGui
from views.db_product_view import Ui_db_product
from functions.graphics_function import *
from functions.other_functions import *

class DB_Product_Window(QtWidgets.QMainWindow, Ui_db_product):
    """
    controlling class for principal_view
    """

    def __init__(self, parent=None, product=None):
        super(DB_Product_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(product["id"])
        self.product = product
        self._init_ui()

    def _init_ui(self):
        self._init_label_title()
        self._init_generalities()

    def _init_label_title(self):
        self.label_id.setText(self.product["id"])
        self.label_descr.setText(self.product["description"])
        date_string = self.product["download_date"].strftime("%d-%m-%Y")
        self.label_download.setText("Téléchargé le " + date_string)
        self.edit_seq.setPlainText(self.product["seq"])

    def _init_generalities(self):
        try:
            parent = self.tree_widget
            for key, value in self.product["annotations"].items():
                self.creation_tree(parent, key, value)
        except Exception as e:
            print(e)
        self.tree_widget.resizeColumnToContents(0)
        self.tree_widget.resizeColumnToContents(1)

    def creation_tree(self, parent, key, value):
        child = QtWidgets.QTreeWidgetItem(parent)
        string_key = key.replace("_", " ")
        child.setText(0, string_key.capitalize())

        if isinstance(value, list) and isinstance(value[0], dict):
            parent = child
            for index, element in enumerate(value):
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setText(0, str(index+1))
                new_parent = child
                if isinstance(element, dict):
                    for key,value in element.items():
                        self.creation_tree(new_parent,key, value)

        elif isinstance(value, dict):
            parent = child
            for key, value in value.items():
                self.creation_tree(parent, key, value)

        else:
            child.setText(1, get_string(value))


    def creation_text(self, variable):
        if type(variable) is str:
            return variable

        elif type(variable) is int:
            return str(variable)

        elif type(variable) is datetime:
            return variable.strftime("%d-%m-%Y")

        elif type(variable) is list:
            if type(variable[0]) is str:
                return str(" , ".join(variable))
            else:
                return self.creation_text(variable)

        elif type(variable) is dict:
            for key, value in variable.items():
                value_string = self.creation_text(value)
                return str(key + "->" + value_string)

        else:
            print(type(variable))
            return ''
