import os
from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from functions.graphics_function import *
from views.result_view import Ui_NCBI_Result
from functions.NCBI_functions import *
from controllers.Request import Request
from objects.Excel import Excel


class NCBI(QtWidgets.QMainWindow, Ui_NCBI_Result):
    """
    controlling class for result_view
    """

    def __init__(self, parent=None, request=None):
        super(NCBI, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Rechercher sur NCBI Nucleotide")
        self.init_ui()
        self.request = None

    def init_ui(self):
        """Actions to initialise the window"""
        self.label_error.hide()
        self.label_selectall.mouseReleaseEvent = self.select_all
        self.label_deselectall.mouseReleaseEvent = self.deselect_all
        self.label_help.mouseReleaseEvent = self.open_help

    # METHODS OF THE CLASS #

    def button_search_clicked(self):
        """Show the result of the NCBI request"""
        self.table.clearContents()
        self.table.setRowCount(0)
        request = self.edit_request.text()
        if len(request) > 0:
            result = get_result_request(request=request)
            count = result["Count"]
            self.label_result.setText(count + " resultats trouvés !")
            if count == '0' and "ErrorList" in result:
                errors = result["ErrorList"]
                self.print_errors(errors)
            else:
                list_id = result["IdList"]
                self.fill_in_result_table(list_id)
        else:
            create_messageBox("Attention !", "Remplissez la requête !")

    def button_extract_clicked(self):
        """Copy the results in an Excel file"""
        rows = self.get_row_checked()
        datas = {'column_names': ["Identifiant", "Titre"], 'rows': rows}
        copy = self.create_excel(datas)
        if copy["done"]:
            create_messageBox("Succes !", "Le fichier a été crée !")
        else:
            create_messageBox("Erreur ! ", "Une erreur est survenue !\n" + copy["error"])

    def select_all(self, event):
        """Select all the lines of the table"""
        number_row = self.table.rowCount()
        for row in range(number_row):
            widget = self.table.item(row, 0)
            widget.setCheckState(Qt.Checked)

    def deselect_all(self, event):
        """Deselect all the lines of the table"""
        number_row = self.table.rowCount()
        for row in range(number_row):
            widget = self.table.item(row, 0)
            widget.setCheckState(Qt.Unchecked)

    def open_help(self, event):
        """Open the window to construct the NCBI request"""
        request_window = Request()
        if request_window.exec() == 0:
            self.request = request_window.get_request()
        request_window.deleteLater()
        self.edit_request.setText(self.request)

    # GRAPHIC METHODS #

    def fill_in_result_table(self, list_ids):
        """
        Fill the table with the result of the request
        :param list_ids: list of the ids of the result
        """
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

    def print_errors(self, errors):
        """
        Print the errors of the NCBI request
        :param result: list ErrorList of the SeqIO object
        """
        self.label_error.show()
        error = "Les termes suivants n'ont pas été trouvés : "
        for key, value in errors.items():
            if len(value) > 0:
                error = error + str(value[0]) + " "
        error = error + "\n"
        self.label_error.setText(error)

    # OTHER FUNCTIONS #

    def get_row_checked(self):
        """
        Get the rows where checkState is True
        :return: a list of the rows
        where row = [id, title]
        """
        number_row = self.table.rowCount()
        checked = []
        for row in range(number_row):
            widget = self.table.item(row, 0)
            is_checked = widget.checkState()
            if is_checked == 2:
                id = widget.text()
                title = self.table.item(row, 1).text()
                row = [id, title]
                checked.append(row)
        return checked

    def create_excel(self, datas):
        """
        Create the Excel file with the result of the NCBI request
        :param datas : dictionnary {'column_names':[], 'rows':[[]]}
        :return: a dictionnary {'done':bool, 'error':string}
        """
        try:
            desktop_path = os.environ['USERPROFILE'] + '\Desktop\\'
            name = QtWidgets.QFileDialog.getSaveFileName(self, 'Enregister', desktop_path, "Excel (*.xlsx)")
            filename = name[0]
            excel = Excel(title=filename)
            worksheet = excel.add_worksheet("Résultats")
            excel.add_data(worksheet=worksheet, datas=datas)
            excel.close()
        except Exception as e:
            return {'done': False, 'error': str(e)}
        else:
            return {'done': True, 'error': None}







