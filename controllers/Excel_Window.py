import operator
import os
from PyQt5.QtWidgets import *
from views.excel_view import Ui_Excel


class Excel_Window(QDialog, Ui_Excel):
    """
    controlling class for excel_view
    """

    def __init__(self, parent=None, ids=None):
        super(Excel_Window, self).__init__(parent)
        self.setupUi(self)
        self.ids = ids
        self.setWindowTitle("Creation d'un fichier Excel")
        # self._create_cell_combobox(column=0)
        # self._fill_in_combobox_worksheet()

    # METHODS OF THE CLASS #

    def button_add_clicked(self):
        """Add a column to the table"""
        count = self.table.columnCount()
        self.table.setColumnCount(count + 1)
        self._create_cell_combobox(column=count)

    def button_export_clicked(self):
        """Create the Excel file and export the datas"""
        datas_to_export = self._get_datas()
        desktop_path = os.environ['USERPROFILE'] + '\Desktop\\'
        name = QFileDialog.getSaveFileName(self, 'Enregister', desktop_path, "Excel (*.xlsx)")
        filename = name[0]

        if len(filename) > 0:
            exportation = self._export_datas(filename, datas_to_export)
            if exportation["done"]:
                message = "Le fichier a bien ete cree !"
            else:
                message = "Un probleme est survenu. Le fichier n'a pas ete cree !\n" + str(exportation["error"])
            self.label_created.setText(message)
