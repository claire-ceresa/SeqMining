from datetime import datetime
from PyQt5 import QtWidgets
from views.db_product_view import Ui_db_product

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
        self._init_groupbox_gen()

    def _init_label_title(self):
        self.label_id.setText(self.product["id"])
        self.label_descr.setText(self.product["description"])
        date_string = self.product["download_date"].strftime("%d-%m-%Y")
        self.label_download.setText("Téléchargé le " + date_string)
        self.edit_seq.setPlainText(self.product["seq"])

    def _init_groupbox_gen(self):
        for key, value in self.product["annotations"].items():
            variable = key.capitalize()
            variable = variable.replace("_", " ")
            try:
                value_string = self.creation_widget(value)
                to_print = variable + ' : ' + value_string
                print(to_print)
            except Exception as e:
                print(e)

    def creation_widget(self, variable):
        if type(variable) is str:
            return variable

        elif type(variable) is int:
            return str(variable)

        elif type(variable) is datetime:
            return variable.strftime("%d-%m-%Y")

        elif type(variable) is list:
            return str(" , ".join(variable))

        elif type(variable) is dict:
            for key, value in variable.items():
                value_string = self.creation_widget(value)
                return str(key + "->" + value_string)

        else:
            print(type(variable))
            return ''
