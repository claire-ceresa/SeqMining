from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from functions.graphics_function import *
from views.result_view import Ui_NCBI_Result
from functions.NCBI_functions import *
from controllers.Request import Request


class NCBI(QtWidgets.QMainWindow, Ui_NCBI_Result):
    """
    controlling class for result_view
    """

    def __init__(self, parent=None, request=None):
        super(NCBI, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Resultats de la recherche")
        self.init_ui()
        self.request = None

    def init_ui(self):
        self.label_error.hide()
        self.label_selectall.mouseReleaseEvent = self.select_all
        self.label_deselectall.mouseReleaseEvent = self.deselect_all
        self.label_help.mouseReleaseEvent = self.open_help

    def button_search_clicked(self):
        self.table.clearContents()
        self.table.setRowCount(0)
        request = self.edit_request.text()
        if len(request) > 0:
            result = get_result_request(request=request)
            count = result["Count"]
            self.label_result.setText(count + " resultats trouvés !")
            if count == '0' and "ErrorList" in result:
                self.label_error.show()
                error = "Les termes suivants n'ont pas été trouvés : "
                for key, value in result["ErrorList"].items():
                    if len(value) > 0:
                        error = error + str(value[0]) + " "
                error = error + "\n"
                self.label_error.setText(error)
            else:
                list_id = result["IdList"]
                self.fill_in_result_table(list_id)
        else:
            create_messageBox("Attention !", "Remplissez la requête !")

    def fill_in_result_table(self, list_ids):
        self.label_error.hide()
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

