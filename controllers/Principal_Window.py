from PyQt5 import QtWidgets
from views.principal_view import Ui_Principal_Window
from controllers.NCBI_Result_Window import NCBI


class Principal(QtWidgets.QMainWindow, Ui_Principal_Window):
    """
    controlling class for principal_view
    """

    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("SeqMining")
        self.window_ncbi = NCBI()

    # METHODS OF THE CLASS #

    def button_ncbi_clicked(self):
        """Open the NCBI window"""
        self.window_ncbi.show()
