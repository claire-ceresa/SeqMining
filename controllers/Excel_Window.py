import os
from PyQt5.QtWidgets import QMainWindow, QComboBox, QFileDialog
from views.excel_view import Ui_excel_window
from functions.graphics_function import *
from objects.DB_Product import DB_Product
from objects.Excel import Excel

class Excel_Window(QMainWindow, Ui_excel_window):
    """
    controlling class for excel_view
    """

    corresp_var_method = {
        'Identifiant GenBank': 'get_id',
        'Description': 'get_description',
        'Taille': 'get_length',
        'Espèce': 'get_species',
        'Sequence': 'get_sequence'
    }

    def __init__(self, parent=None, results=None):
        super(Excel_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Exporter vers un fichier Excel")
        self.results = results
        self._create_cell_combobox(0)

    def button_add_clicked(self):
        count = self.table.columnCount()
        if count < len(self.corresp_var_method):
            self.table.setColumnCount(count + 1)
            self._create_cell_combobox(column=count)

    def button_export_clicked(self):
        datas_to_export = self.get_data_to_export()
        try:
            filename = get_save_filename("Excel")
            file = Excel(filename)
            worksheet = file.add_worksheet()
            file.add_data(worksheet, datas_to_export)
            file.close()
        except Exception as e:
            self.label_created.setText("Le fichier n'a pas été crée !\n" + str(e))
        else:
            self.label_created.setText("Le fichier a été crée !")

    def _create_cell_combobox(self, column):
        """Create a QComboBox in the header cell"""
        combobox = QComboBox()
        fill_combobox(combobox, list(self.corresp_var_method))
        self.table.setCellWidget(0, column, combobox)
        self.table.resizeColumnsToContents()

    def get_data_to_export(self):
        headers = []
        nb_columns = self.table.columnCount()
        for column in range(0, nb_columns):
            item = self.table.cellWidget(0, column)
            variable_name = item.currentText()
            headers.append(variable_name)

        datas = []
        for result in self.results:
            line = []
            product = DB_Product(data=result)
            for header in headers:
                method = self.corresp_var_method[header]
                variable_value = getattr(product, method)()
                line.append(variable_value)
            datas.append(line)

        return {"column_names":headers, "rows":datas}
