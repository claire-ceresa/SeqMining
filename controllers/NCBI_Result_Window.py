import os
from math import *
from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from functions.graphics_function import *
from views.result_view import Ui_NCBI_Result
from functions.NCBI_functions import *
from controllers.NCBI_Request_Window import Request
from controllers.NCBI_Product_Window import NCBI_Product_Window
from objects.Excel import Excel


class NCBI(QtWidgets.QMainWindow, Ui_NCBI_Result):
    """
    controlling class for result_view
    """

    def __init__(self, parent=None):
        super(NCBI, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Rechercher sur NCBI Nucleotide")
        self.init_ui()
        self.request = None
        self.window_product = None

    def init_ui(self):
        """Actions to initialise the window"""
        self.label_error.hide()
        self.label_selectall.mouseReleaseEvent = self.select_all
        self.label_deselectall.mouseReleaseEvent = self.deselect_all
        self.label_help.mouseReleaseEvent = self.open_help

    # METHODS OF THE CLASS #

    def button_search_request_clicked(self):
        """Show the result of the NCBI request"""
        QtWidgets.QApplication.setOverrideCursor(Qt.WaitCursor)
        self.table.clearContents()
        self.table.setRowCount(0)
        request = self.edit_request.text()
        if len(request) > 0:
            self.request = request
            self.set_result_interface()
        else:
            create_messageBox("Attention !", "Remplissez la requête !")
        QtWidgets.QApplication.restoreOverrideCursor()

    def button_search_id_clicked(self):
        QtWidgets.QApplication.setOverrideCursor(Qt.WaitCursor)
        id = self.edit_id.text()
        if len(id) > 0:
            self.window_product = NCBI_Product_Window(id=id)
            if self.window_product.product.valid:
                self.window_product.show()
            else:
                create_messageBox("Erreur", "Identifiant inconnu !")
        else:
            create_messageBox("Attention", "Veuillez entrer un identifiant GenBank")
        QtWidgets.QApplication.restoreOverrideCursor()

    def button_extract_all_clicked(self):
        print("all")

    def button_extract_select_clicked(self):
        """Copy the results in an Excel file"""
        rows = self.get_row_checked()
        datas = {'column_names': ["Identifiant", "Titre"], 'rows': rows}
        copy = self.create_excel(datas)
        if copy["done"]:
            create_messageBox("Succes !", "Le fichier a été crée !")
        else:
            create_messageBox("Erreur ! ", "Une erreur est survenue !\n" + copy["error"])

    def row_table_clicked(self, row, column):
        """Open the online Product Window"""
        QtWidgets.QApplication.setOverrideCursor(Qt.WaitCursor)
        id_widget = self.table.item(row, 0)
        id = id_widget.text()
        self.window_product = NCBI_Product_Window(id=id)
        self.window_product.show()
        QtWidgets.QApplication.restoreOverrideCursor()

    def combobox_nb_changed(self):
        """Change the number of result shown in the table"""
        QtWidgets.QApplication.setOverrideCursor(Qt.WaitCursor)
        self.set_result_interface()
        QtWidgets.QApplication.restoreOverrideCursor()

    def combobox_page_changed(self, index):
        QtWidgets.QApplication.setOverrideCursor(Qt.WaitCursor)
        self.set_result_interface()
        QtWidgets.QApplication.restoreOverrideCursor()

    def set_result_interface(self):
        max = int(self.combobox_nb.currentText())
        if self.combobox_page.currentText() is '':
            page = 1
        else:
            page = int(self.combobox_page.currentText())
        start = (page - 1) * max
        result = get_result_request(request=self.request, retmax=max, retstart=start)
        count = int(result["Count"])
        self.print_results(start=start, max=max, count=count)
        self.set_combobox_pages(count=count, max=max, actual=page)
        if count == '0' and "ErrorList" in result:
            self.print_errors(result)
        else:
            self.fill_in_result_table(result)

    # METHODS OF QLabel as BUTTONS #

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

    def fill_in_result_table(self, result):
        """
        Fill the table with the result of the request
        :param list_ids: list of the ids of the result
        """
        self.label_error.hide()
        list_ids = result["IdList"]
        number_row = len(list_ids)
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
        self.table.resizeColumnToContents(0)

    def print_results(self, start, max, count):
        start_to_print = start + 1
        max_to_print = max + start
        if max < count:
            self.label_result.setText(
                " Resultats : " + str(start_to_print) + " à " + str(max_to_print) + " sur " + str(count))
        else:
            self.label_result.setText(" Resultats : " + str(count))

    def print_errors(self, result):
        """
        Print the errors of the NCBI request
        :param result: list ErrorList of the SeqIO object
        """
        self.label_error.show()
        errors = result["ErrorList"]
        error = "Les termes suivants n'ont pas été trouvés : "
        for key, value in errors.items():
            if len(value) > 0:
                error = error + str(value[0]) + " "
        error = error + "\n"
        self.label_error.setText(error)

    def set_combobox_pages(self, count, max, actual):
        nb_page = ceil(count / max)
        self.label_on.setText("sur " + str(nb_page))
        if nb_page > 1:
            pages = list(range(1, nb_page + 1))
        else:
            pages = [1]
        fill_combobox(self.combobox_page, pages)
        self.combobox_page.setCurrentText(str(actual))

    # OTHER FUNCTIONS #

    def get_info_result(self):
        nb_to_print = self.combobox_nb.currentText()
        actual_page = self.combobox_page.currentText()

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
