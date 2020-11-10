from PyQt5.QtWidgets import QMainWindow
from views.principal_view import Ui_Principal_Window
from controllers.NCBI_Search_Window import NCBI_Search_Window
from controllers.DB_Search_Window import DB_Search_Window
from controllers.Gestion_Window import Gestion_Window
from functions.other_functions import *
from objects.MongoDB_Connexion import MongoDB_Connexion


class Principal(QMainWindow, Ui_Principal_Window):
    """
    controlling class for principal_view
    """

    def __init__(self, parent=None):
        super(Principal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("SeqMining")
        self.connected_to_internet = self._check_connexion_to_internet()
        self.connected_to_db = self._check_connexion_to_db()
        self.window_ncbi = None
        self.window_db = None
        self.window_gestion = None
        self._init_ui()

    # METHODS OF THE CLASS #

    def button_ncbi_clicked(self):
        """Open the NCBI window"""
        self.window_ncbi = NCBI_Search_Window()
        self.window_ncbi.show()

    def button_db_clicked(self):
        """Open the DB window"""
        self.window_db = DB_Search_Window()
        self.window_db.show()

    def button_gestion_clicked(self):
        """Open the gestion window"""
        self.window_gestion = Gestion_Window()
        self.window_gestion.show()

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
        if self.connected_to_db:
            self.label_connex_db.setText("Connecté à la base de données")
            self.label_connex_db.setStyleSheet("color: rgb(0, 150, 0);")
        else:
            self.label_connex_db.setText("Pas connecté à la base de données")
            self.label_connex_db.setStyleSheet("color: rgb(255, 0, 0);")

    # CONNEXION FUNCTIONS #

    def _check_connexion_to_db(self) :
        """Return state of connexion to db"""
        connexion = MongoDB_Connexion()
        state = connexion.connected_to_server()
        connexion.close()
        return state

    def _check_connexion_to_internet(self):
        """Return state of connexion to internet"""
        internet = connected_to_internet("https://www.ncbi.nlm.nih.gov/nucleotide")
        return internet["connected"]
