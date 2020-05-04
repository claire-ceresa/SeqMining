from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from views.result_view import Ui_NCBI_Result
from functions.NCBI_functions import *

class Result(QtWidgets.QMainWindow, Ui_NCBI_Result):
    """
    controlling class for result_view
    """

    def __init__(self, parent=None, request=None):
        super(Result, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Resultats de la recherche")
        self.init_ui(request)

    def init_ui(self,request):
        self.edit_request.setText(request)
        self.button_search_clicked()

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
