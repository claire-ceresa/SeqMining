from PyQt5 import QtWidgets
from views.principal_view import Ui_Principal_Window
from controllers.NCBI_Search_Window import NCBI_Search_Window
from controllers.DB_Search_Window import DB_Search_Window
from functions.other_functions import *
from objects.MongoDB_Connexion import MongoDB_Connexion

class Principal(QtWidgets.QMainWindow, Ui_Principal_Window):
    """
    controlling class for principal_view
    """

    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("SeqMining")
        self.connected_to_internet = True
        self.mongoDB_connexion = MongoDB_Connexion()
        self.window_ncbi = NCBI_Search_Window(connexion=self.mongoDB_connexion)
        self.window_db = DB_Search_Window(connexion=self.mongoDB_connexion)
        self._set_properties()
        self._init_ui()

    def _set_properties(self):
        """Set the properties of the object"""
        internet = connected_to_internet("https://www.ncbi.nlm.nih.gov/nucleotide")
        if not internet["connected"]:
            self.connected_to_internet = False

    # METHODS OF THE CLASS #

    def button_ncbi_clicked(self):
        """Open the NCBI window"""
        self.window_ncbi.show()

    def button_db_clicked(self):
        """Open the DB window"""
        self.window_db.show()

    def button_analyses_clicked(self):
        """Open the Analyses window"""
        # TODO : create the analyses
        print("analyses")

    # GRAPHIC METHODS #

    def _init_ui(self):
        """Initialise the interface"""
        self._init_label_internet()
        self._init_label_db()

    def _init_label_internet(self):
        """Initialise the label of connexion to internet"""
        if self.connected_to_internet:
            self.label_connex_internet.setText("Connecté à internet")
            self.label_connex_internet.setStyleSheet("color: rgb(0, 150, 0);")
        else:
            self.button_ncbi.setEnabled(False)
            self.label_connex_internet.setText("Pas connecté à internet")
            self.label_connex_internet.setStyleSheet("color: rgb(255, 0, 0);")

    def _init_label_db(self):
        """Initialise the label of connexion to the database"""
        if self.mongoDB_connexion.connected_to_server:
            self.label_connex_db.setText("Connecté à la base de données")
            self.label_connex_db.setStyleSheet("color: rgb(0, 150, 0);")
        else:
            self.label_connex_db.setText("Pas connecté à la base de données")
            self.label_connex_db.setStyleSheet("color: rgb(255, 0, 0);")
