from PyQt5.QtWidgets import QMainWindow, QComboBox
from views.excel_view import Ui_excel_window

class Excel_Window(QMainWindow, Ui_excel_window):
    """
    controlling class for excel_view
    """

    corresp_var_colname = {
        'id': 'Identifiant GenBank',
        'description': 'Description',

    }

    def __init__(self, parent=None):
        super(Excel_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Exporter vers un fichier Excel")
        self._create_cell_combobox(0)

    def button_add_clicked(self):
        print("add")

    def button_export_clicked(self):
        print("export")

    def _create_cell_combobox(self, column):
        """Create a QComboBox in the header cell"""
        combo = QComboBox()
        combo.addItem("")
        #
        # for attribute in attributes:
        #     if attribute in self.corresp_var_colname:
        #         combo.addItem(self.corresp_var_colname[attribute])
        #     else:
        #         combo.addItem(attribute)

        combo.addItem("URL")
        self.table.setCellWidget(0, column, combo)
        self.table.resizeColumnsToContents()

