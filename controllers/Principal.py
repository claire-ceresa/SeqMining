from PyQt5 import QtWidgets
from views.principal_view import Ui_Principal_Window
from controllers.Result import Result


class Principal(QtWidgets.QMainWindow, Ui_Principal_Window):
    """
    controlling class for request_view
    """

    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("SeqMining")
        self.window_ncbi = Result()

    def button_ncbi_clicked(self):
        self.window_ncbi.show()
