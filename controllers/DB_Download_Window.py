from PyQt5 import QtWidgets
from views.db_download_view import Ui_db_result

class DB_Download_Window(QtWidgets.QDialog, Ui_db_result):
    """
    controlling class for request_view
    """

    def __init__(self, parent=None, results=None):
        super(DB_Download_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Résultat du téléchargement")
        self.results = results
        self._init_ui()

    def _init_ui(self):
        self._init_label()
        self._init_table()

    def _init_label(self):
        saved = self.get_number_saved()
        label_saved = str(saved) + " résultats enregistrés sur " + str(len(self.results))
        self.label_result.setText(label_saved)

    def _init_table(self):
        errors = self.get_errors()
        if len(errors) > 0:
            self.table_error.setRowCount(len(errors))
            for line, error in enumerate(errors):
                self.table_error.setItem(line, 0, QtWidgets.QTableWidgetItem(error["id_saved"]))
                self.table_error.setItem(line, 1, QtWidgets.QTableWidgetItem(error["error"]))
            self.table_error.resizeColumnToContents(0)
        else:
            self.table_error.hide()

    def get_number_saved(self):
        saved = 0
        for result in self.results:
            if result["error"] is None:
                saved = saved + 1
        return saved

    def get_errors(self):
        errors = []
        for result in self.results:
            if result["error"] is not None:
                errors.append(result)
        return errors
