from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from views.result_view import Ui_NCBI_Result
from functions.NCBI_functions import *
from controllers.Request import Request

class Result(QtWidgets.QMainWindow, Ui_NCBI_Result):
    """
    controlling class for result_view
    """

    def __init__(self, parent=None, request=None):
        super(Result, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Resultats de la recherche")
        self.init_ui()
        self.request = None

    def init_ui(self):
        self.label_selectall.mouseReleaseEvent = self.select_all
        self.label_deselectall.mouseReleaseEvent = self.deselect_all
        self.label_help.mouseReleaseEvent = self.open_help

    def button_search_clicked(self):
        self.table.clearContents()
        self.table.setRowCount(0)
        request = self.edit_request.text()
        list_ids = get_list_ids(request=request)
        if len(list_ids) > 0:
            self.fill_in_result_table(list_ids)
        else:
            self.label_result.setText("Aucun resultat trouvé !")

    def fill_in_result_table(self, list_ids):
        number_row = len(list_ids)
        self.label_result.setText(str(number_row) + " resultats trouvés !")
        self.table.setRowCount(number_row)
        str_ids = ','.join(list_ids)
        summary = get_summary(str_ids)
        for row, id in enumerate(summary):
            accession = QtWidgets.QTableWidgetItem(id["AccessionVersion"])
            accession.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            accession.setCheckState(Qt.Unchecked)
            title = QtWidgets.QTableWidgetItem(id["Title"])
            self.table.setItem(row, 0, accession)
            self.table.setItem(row, 1, title)

    def select_all(self, event):
        number_row = self.table.rowCount()
        for row in range(number_row):
            widget = self.table.item(row, 0)
            widget.setCheckState(Qt.Checked)

    def deselect_all(self, event):
        number_row = self.table.rowCount()
        for row in range(number_row):
            widget = self.table.item(row, 0)
            widget.setCheckState(Qt.Unchecked)

    def open_help(self, event):
        dialog = Request()
        if dialog.exec() == 0:
            self.request = dialog.get_request()
        dialog.deleteLater()
        self.edit_request.setText(self.request)

