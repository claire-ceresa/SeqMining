import pandas as pd
from PyQt5.QtWidgets import QDialog
from views.db_import_view import Ui_DB_Import
from controllers.DB_Download_Window import DB_Download_Window
from functions.graphics_function import *
from functions.db_functions import *

class DB_Import_Window(QDialog, Ui_DB_Import):
    """
    controlling class for db_import_view
    """

    def __init__(self, parent=None):
        super(DB_Import_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Importer")
        self.widgets = []
        self.products = None
        self._init_ui()

    def _init_ui(self):
        filename = get_filename("Excel", open=True)
        self.products = pd.read_excel(filename)
        for column in self.products.columns:
            label_name = create_label(text=column)
            combobox_variables = create_combobox(
                ['', 'id', 'function', 'subfunction', 'links', 'comments', 'applications', 'reference'])
            layout = create_layout(widgets= [label_name, combobox_variables], horizontal=True)
            self.widgets.append({'label':label_name, 'combobox':  combobox_variables})
            self.layout_variables.addLayout(layout)

    def button_import_clicked(self):
        variables = {}
        modified = []
        variable_id = None
        for layout in self.widgets:
            if layout['combobox'].currentText() != '':
                variables[layout['label'].text()] = layout['combobox'].currentText()
                if layout['combobox'].currentText() == 'id':
                    variable_id = layout['label'].text()
        for index, product in self.products.iterrows():
            id = product[variable_id]
            db_product = get_one_product(id)
            if 'coraliotech' in db_product:
                    coraliotech_dict = db_product['coraliotech']
            else:
                    coraliotech_dict = {'function': '', 'subfunction': '', 'links': [], 'comments': [], 'applications': [], 'reference': ''}
            for name_variable, variable in variables.items():
                if not pd.isna(product[name_variable]) and variable != 'id':
                    if variable in ['function', 'subfunction', 'reference']:
                        coraliotech_dict[variable] = product[name_variable]
                    else:
                        coraliotech_dict[variable].append(product[name_variable])
            update = update_one_product({'id': id}, {'coraliotech': coraliotech_dict})
            modified.append(update)
        modified_window = DB_Download_Window(parent=self, results=modified)
        modified_window.show()

