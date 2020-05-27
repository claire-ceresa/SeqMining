from PyQt5 import QtWidgets
from views.db_results_view import Ui_db_results


class DB_Result_Window(QtWidgets.QMainWindow, Ui_db_results):
    """
    controlling class for principal_view
    """

    def __init__(self, parent=None, results=None):
        super(DB_Result_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Résultats de la recherche")
        self.results = results
        self._init_ui()

    def _init_ui(self):
        for line, result in enumerate(self.results):
            self.table_result.setRowCount(line+1)
            self.table_result.setItem(line, 0, QtWidgets.QTableWidgetItem(result["_id"]))
            self.table_result.setItem(line, 1, QtWidgets.QTableWidgetItem(result["description"]))

