from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from views.db_results_view import Ui_db_results
from controllers. DB_Product_Window import DB_Product_Window
from controllers.Excel_Window import Excel_Window

class DB_Results_Window(QMainWindow, Ui_db_results):
    """
    controlling class for db_results_view
    """

    def __init__(self, parent=None, results=None):
        super(DB_Results_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Résultats de la recherche")
        self.results = results
        self.excel_window = None
        self.product_windows = []
        self._init_ui()

    ## METHODS OF THE CLASS ##

    def table_result_clicked(self, line, column):
        """Open the DB window of the product """
        product = self.results[line]
        product_window = DB_Product_Window(product=product)
        product_window.show()
        self.product_windows.append(product_window)

    def button_extract_clicked(self):
        """Extract the result to an Excel file"""
        self.excel_window = Excel_Window(results=self.results)
        self.excel_window.show()


    ## GRAPHIC METHODS ##

    def _init_ui(self):
        """Initialize the user interface"""
        self.label_result.setText(str(len(self.results)) + " résultats")
        for line, result in enumerate(self.results):
            self.table_result.setRowCount(line+1)
            self.table_result.setItem(line, 0, QTableWidgetItem(result["_id"]))
            self.table_result.setItem(line, 1, QTableWidgetItem(result["description"]))