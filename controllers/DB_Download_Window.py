from PyQt5 import QtWidgets
from views.db_download_view import Ui_db_result


class DB_Download_Window(QtWidgets.QDialog, Ui_db_result):
    """
    controlling class for db_download_view
    """

    def __init__(self, parent=None, results=None):
        super(DB_Download_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Résultat du téléchargement")
        self.results = results
        self.number_saved = 0
        self.errors = []
        self._init_properties()
        self._init_ui()

    # GRAPHIC METHODS #

    def _init_properties(self):
        """Set the number of result saved and the errors"""
        for result in self.results:
            if result["error"] is None:
                self.number_saved = self.number_saved + 1
            else:
                self.errors.append(result)

    def _init_ui(self):
        """Initialize the user interface"""
        self._init_label()
        self._init_table()

    def _init_label(self):
        """Initialize the label with the number of result saved"""
        label_saved = str(self.number_saved) + " résultats enregistrés sur " + str(len(self.results))
        self.label_result.setText(label_saved)

    def _init_table(self):
        """Fill in the table with the errors"""
        if len(self.errors) > 0:
            self.table_error.setRowCount(len(self.errors))
            for line, error in enumerate(self.errors):
                self.table_error.setItem(line, 0, QtWidgets.QTableWidgetItem(error["id"]))
                self.table_error.setItem(line, 1, QtWidgets.QTableWidgetItem(error["error"]))
            self.table_error.resizeColumnToContents(0)
        else:
            self.table_error.hide()