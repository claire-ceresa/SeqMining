from PyQt5 import QtWidgets
from views.db_search_view import Ui_DB_Search

class DB_Search_Window(QtWidgets.QMainWindow, Ui_DB_Search):
    """
    controlling class for principal_view
    """

    def __init__(self, parent=None, connexion=None):
        super(DB_Search_Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Rechercher sur la base de données locale")
        self.mongoDB_connexion = connexion
        self._init_ui()

    def _init_ui(self):
        self.label_date_et.hide()
        self.edit_date_2.hide()
        self.label_download_et.hide()
        self.edit_download_2.hide()

    def button_search_clicked(self):
        print("search")

    def combobox_date_changed(self, text):
        if text == "entre":
            self.label_date_et.show()
            self.edit_date_2.show()
        else:
            self.label_date_et.hide()
            self.edit_date_2.hide()

    def combobox_download_changed(self, text):
        if text == "entre":
            self.label_download_et.show()
            self.edit_download_2.show()
        else:
            self.label_download_et.hide()
            self.edit_download_2.hide()

