from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow
from request_view import Ui_MainWindow
from Bio import Entrez


class Request(QMainWindow, Ui_MainWindow):
    """
    controlling class for request_view
    """
    def __init__(self, parent=None):
        super(Request, self).__init__(parent)
        self.setupUi(self)
        self.filters = [self.layout_widget]
        self.fill_combobox(self.combobox_name)

    def fill_combobox(self, combobox):
        database = Entrez.einfo(db="nucleotide")
        database_info = Entrez.read(database)
        field_list = database_info["DbInfo"]["FieldList"]
        field_list_sorted = sorted(field_list, key=lambda x: x["FullName"])
        for name in field_list_sorted:
            combobox.addItem(name["FullName"])

    def button_add_clicked(self):

        layout = QtWidgets.QHBoxLayout()
        layout.setObjectName("layout_" + str(len(self.filters)))

        combobox = QtWidgets.QComboBox()
        self.fill_combobox(combobox)
        edit = QtWidgets.QLineEdit()
        button_add = self.button_add

        layout.addWidget(combobox)
        layout.addWidget(edit)
        layout.addWidget(button_add)

        self.layout_filters.addLayout(layout)
        self.filters.append(layout)

        print(layout.count())
